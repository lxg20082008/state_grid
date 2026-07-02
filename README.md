# State Grid Home Assistant 集成

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/hacs/integration)

这是一个用于 Home Assistant 的X网 (State Grid) 集成，支持通过账号密码登录获取用电数据。

## 功能特性

- ✅ 支持X网账号密码登录
- ✅ 自动验证码识别 (使用 ONNX 模型)
- ✅ 获取实时用电数据
- ✅ 获取月度账单信息
- ✅ 获取账户余额
- ✅ 支持多户号管理
- ✅ 中英文界面支持

## 与原版（bilezhou）的差异

原版来自 [**bilezhou** https://github.com/bilezhou/state_grid](https://github.com/bilezhou/state_grid) 

| 项目 | 内容 | 详情 |
|------|------|------|
| 1 | 重构: 按HACS要求重构项目结构 | - 将集成代码移至 custom_components/state_grid/ 目录<br>- 添加 hacs.json 配置文件<br>- 添加中英文翻译文件 (translations/)<br>- 更新 manifest.json 添加 issue_tracker 和 codeowners<br>- 添加 MIT LICENSE<br>- 添加 .gitignore 文件 |
| 2 | 修复: 解决500错误问题 | - 添加 persistent_notification 导入到 data_client.py<br>- 修复翻译文件字段名: username -> account<br>- 添加缺失的 abort 原因翻译: single_instance_allowed |
| 3 | 统一: 使用'State Grid'作为集成名称 | - 更新hacs.json中的名称为'State Grid'<br>- 更新manifest.json中的名称为'State Grid'<br>- 更新README.md标题为'State Grid Home Assistant 集成' |
| 4 | 修复: 解决ONNX依赖安装问题 | - 从manifest.json中移除onnxruntime作为必需依赖<br>- 使ONNX成为可选依赖，集成在没有ONNX时使用基础验证码识别<br>- 更新README.md说明可选依赖<br>- 改进captcha_solver.py的错误处理 |
| 5 | 改进: 添加调试日志和错误处 | - 在config_flow.py中添加调试日志<br>- 改进ONNX导入错误处理<br>- 添加更好的异常处理 |

## 安装方法

### 通过 HACS (推荐)

1. 在 HACS 中添加自定义仓库：
   - 仓库地址: `https://github.com/lxg20082008/state_grid`
   - 类别: 集成 (Integration)

2. 在 HACS 中搜索 "State Grid" 并安装

3. 重启 Home Assistant

### 手动安装

1. 下载最新版本: [Releases](https://github.com/lxg20082008/state_grid/releases)
2. 将 `custom_components/state_grid` 文件夹复制到您的 Home Assistant 配置目录的 `custom_components` 文件夹中
3. 重启 Home Assistant

## 配置

1. 在 Home Assistant 中，进入 **配置** → **设备与服务**
2. 点击 **添加集成**
3. 搜索 **"X网"** 或 **"State Grid"**
4. 输入您的X网账号和密码
5. 点击提交完成配置

## 创建的实体

集成将创建以下传感器实体：

- **账户余额** (`sensor.state_grid_balance`)
- **今日用电量** (`sensor.state_grid_daily_ele`)
- **本月用电量** (`sensor.state_grid_monthly_ele`)
- **本年用电量** (`sensor.state_grid_yearly_ele`)
- **峰时用电量** (`sensor.state_grid_peak_ele`)
- **谷时用电量** (`sensor.state_grid_valley_ele`)
- **平段用电量** (`sensor.state_grid_normal_ele`)
- **尖峰用电量** (`sensor.state_grid_sharp_ele`)

## 截图

### 集成配置界面
![配置界面](https://github.com/user-attachments/assets/713d9dce-d68c-4534-8ca4-beb5c5bf7cf3)

### 创建的实体
![实体列表](https://github.com/user-attachments/assets/0ab22ba5-1bb4-4119-bfc5-610b02eec19b)

### 仪表板示例
![仪表板](https://github.com/user-attachments/assets/6de4abc9-03ef-4f1d-9fb3-3a90fbc0320f)

## 技术要求

- Home Assistant 2024.1.0 或更高版本
- Python 3.9 或更高版本
- 网络连接 (需要访问X网 API)

## 依赖项

集成会自动安装以下依赖：
- `numpy`
- `Pillow`

**可选依赖**:
- `onnxruntime>=1.17.0` - 用于高级验证码识别（如果安装失败，集成将使用基础识别方案）

## 故障排除

### 常见问题

1. **无法加载配置向导 (500 错误)**
   - 确保已安装所有依赖
   - 检查网络连接
   - 重启 Home Assistant

2. **登录失败**
   - 确认账号密码正确
   - 检查网络连接
   - 尝试手动登录X网 APP 确认账号状态

3. **数据不更新**
   - 检查集成配置
   - 查看 Home Assistant 日志
   - 重启集成

### 查看日志

在 Home Assistant 配置 → 日志中查看相关错误信息。

## 开发

### 项目结构
```
state_grid/
├── custom_components/
│   └── state_grid/
│       ├── __init__.py
│       ├── config_flow.py
│       ├── data_client.py
│       ├── sensor.py
│       ├── manifest.json
│       ├── translations/
│       │   ├── en.json
│       │   └── zh-Hans.json
│       └── utils/
│           ├── crypt.py
│           ├── logger.py
│           └── store.py
├── hacs.json
├── LICENSE
└── README.md
```

### 贡献

欢迎提交 Issue 和 Pull Request！

## 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 致谢

- 感谢 [HassBox] 的原始集成
- 感谢 [ARC-MX](https://github.com/ARC-MX/sgcc_electricity_new) 的验证码识别模型
- 感谢所有贡献者和用户

## 版本历史

- **v0.1.3** (2025-12-15): 修复 ONNX 依赖问题，使其成为可选依赖
- 2026-04-15 ：针对登录错误，增加了随机延迟，尤其是针对登陆错误后重试过快做了延迟处理，增加了登录错误的log输出，内容上更加明确。

## 支持

如果您遇到问题或有建议，请：
1. 查看 [Issues](https://github.com/lxg20082008/state_grid/issues)
2. 创建新的 Issue
3. 或通过其他方式联系维护者

---

**注意**: 本项目仅供学习和研究使用，请遵守X网的相关规定和服务条款。
