# Microsoft Rewards Bing搜索自动化工具

这个工具可以自动执行Bing搜索，帮助您赚取Microsoft Rewards积分。

## 功能特性

- 自动执行Bing搜索
- 模拟人类浏览行为（随机滚动、延迟）
- 支持自定义搜索次数
- 模块化配置
- 详细日志记录
- 自动或手动驱动程序管理

## 安装依赖

```bash
pip install -r requirements.txt
```

## 配置

编辑 `config.py` 文件来自定义设置：

- `KEYWORDS`: 搜索关键词列表
- `DEFAULT_SEARCH_COUNT`: 默认搜索次数
- `BROWSER_OPTIONS`: 浏览器选项
- 各种延迟和超时设置

## 使用方法

1. 确保已下载 `msedgedriver.exe` 并放置在 `channel/` 文件夹中
2. 运行脚本：
   ```bash
   python main.py [搜索次数]
   ```
   如果不指定搜索次数，默认使用33次。

3. 脚本会打开登录页面，请手动登录Microsoft账户
4. 按Enter键开始自动搜索

## 项目结构

```
.
├── main.py          # 主程序
├── config.py        # 配置文件
├── requirements.txt # 依赖列表
├── channel/         # 驱动程序目录
│   └── msedgedriver.exe
└── README.md        # 说明文档
```

## 注意事项

- 请遵守Microsoft Rewards的使用条款
- 过度自动化可能导致账户被限制
- 建议间隔运行，避免连续大量搜索
- 网络问题时会自动回退到本地驱动程序

## 许可证

MIT License