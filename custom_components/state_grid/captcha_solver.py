"""
验证码识别模块 - 基于国网代码修改
"""
import logging
import base64
import re
import numpy as np
from io import BytesIO
from PIL import Image
logger = logging.getLogger(__name__)
try:
    import onnxruntime
    HAS_ONNX = True
except ImportError:
    HAS_ONNX = False
    logger.warning("ONNX未安装，将使用备用方案")
def base64_to_PIL(base64_str: str) -> Image.Image:
    """Base64转PIL图像"""
    base64_data = re.sub('^data:image/.+;base64,', '', base64_str)
    byte_data = base64.b64decode(base64_data)
    image_data = BytesIO(byte_data)
    return Image.open(image_data)
class CaptchaSolver:
    """验证码识别器"""
    def __init__(self, onnx_file="captcha.onnx"):
        self.onnx_session = None
        if HAS_ONNX:
            try:
                self.onnx_session = onnxruntime.InferenceSession(onnx_file)
                logger.info(f"ONNX模型加载成功: {onnx_file}")
            except Exception as e:
                logger.error(f"ONNX模型加载失败: {e}")
        else:
            logger.warning("ONNX未安装，使用备用验证码识别")
    def _get_boxes(self, prediction, confidence_threshold=0.7):
        """获取边界框 - 从国网代码移植"""
        try:
            feature_map = np.squeeze(prediction)
            conf = feature_map[..., 4] > confidence_threshold
            box = feature_map[conf == True]
            if len(box) == 0:
                return np.array([])
            cls_cinf = box[..., 5:]
            cls = []
            for i in range(len(cls_cinf)):
                cls.append(int(np.argmax(cls_cinf[i])))
            all_cls = list(set(cls))
            output = []
            for curr_cls in all_cls:
                curr_cls_box = []
                for j in range(len(cls)):
                    if cls[j] == curr_cls:
                        box[j][5] = curr_cls
                        curr_cls_box.append(box[j][:6])
                if curr_cls_box:
                    curr_cls_box = np.array(curr_cls_box)
                    output.extend(curr_cls_box)
            return np.array(output) if output else np.array([])
        except Exception as e:
            logger.error(f"获取边界框失败: {e}")
            return np.array([])
    def get_distance(self, image: Image.Image) -> int:
        """获取滑动距离"""
        if not self.onnx_session:
            distance = 180
            logger.info(f"ONNX不可用，使用固定距离: {distance}")
            return distance
        try:
            img = image.resize((416, 416))
            img = img.convert("RGB")
            img = np.array(img).transpose(2, 0, 1)
            img = img.astype(np.float32) / 255.0
            img = np.expand_dims(img, axis=0)
            inputs = {self.onnx_session.get_inputs()[0].name: img}
            prediction = self.onnx_session.run(None, inputs)[0]
            boxes = self._get_boxes(prediction, confidence_threshold=0.3)
            if len(boxes) == 0:
                logger.warning("未检测到滑动块，尝试更低的阈值")
                boxes = self._get_boxes(prediction, confidence_threshold=0.1)
                if len(boxes) == 0:
                    logger.warning("仍未能检测到滑动块，使用估算距离")
                    width, height = image.size
                    distance = int(width * 0.35)
                    logger.info(f"估算距离: {distance}")
                    return distance
            distances = []
            for box in boxes:
                x1 = int(box[0])
                distances.append(x1)
            distance = int(np.mean(distances))
            scale_factor = image.size[0] / 416.0
            distance = int(distance * scale_factor)
            logger.info(f"验证码识别距离: {distance} (原始: {int(np.mean(distances))}, 缩放系数: {scale_factor:.2f})")
            return distance
        except Exception as e:
            logger.error(f"验证码识别失败: {e}")
            try:
                width, height = image.size
                distance = int(width * 0.35)
                logger.info(f"识别失败，使用备用距离: {distance}")
                return distance
            except:
                return 180