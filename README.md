HassBox的state_grid集成与ARC-MX的sgcc_electricity_new（https://github.com/ARC-MX/sgcc_electricity_new）粗暴的结合一起，主打一个能用就行。
逻辑是用sgcc_electricity_new的识别来登录国网，然后用state_grid的接口来调数据。
账号密码登录。
使用方式：将整个state_grid复制到custom_components内就行
初次添加集成会自动安装onnx依赖，速度有点慢。另外不是很建议haos用，但用也能用吧。
要是有添加不了的情况自己改一改代码就行。
大佬的UI设计也都是能用的：
<img width="1183" height="925" alt="image" src="https://github.com/user-attachments/assets/6de4abc9-03ef-4f1d-9fb3-3a90fbc0320f" />
集成添加账号样式：
<img width="639" height="484" alt="image" src="https://github.com/user-attachments/assets/713d9dce-d68c-4534-8ca4-beb5c5bf7cf3" />
创建的实体：
<img width="500" height="1179" alt="image" src="https://github.com/user-attachments/assets/0ab22ba5-1bb4-4119-bfc5-610b02eec19b" />
