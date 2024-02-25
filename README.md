# StatementGenerator

## 项目描述
StatementGenerator 是一个用于生成支付网关交易流水的工具，当前仅支持PayPal的交易数据，未来计划支持更多的支付平台。它允许用户快速生成交易流水记录，并输出为PDF格式。

## 演示
这里是项目的演示图:

![Demonstration](/images/output.png "演示图片")

## 技术栈
- Python 3.11.4

## 安装指南
要安装和使用StatementGenerator，请按照以下步骤操作：

1. 确保您的系统已安装Python 3.11或更高版本。
2. 克隆仓库到本地或下载源代码。
3. `pip install requirements.txt`安装依赖
4. 确保程序在Windows运行并安装了chrome

## 使用说明
1. 在项目根目录下找到 `config.ini` 文件。
2. 修改 `config.ini` 中的配置项，包括落款邮箱、要生成的交易数量以及日期范围。
3. 打开终端或命令提示符。
4. 进入项目根目录。
5. 运行命令 `python main.py`。
6. 生成的PDF将会保存在 `result` 目录中。
7. 流水数据以及商家账户号均为随机生成且格式仿照原statement格式

## 贡献指南
欢迎其他开发者对StatementGenerator项目做出贡献。如果您有任何功能请求或想要贡献代码，请先开一个issue或pull request。

## 问题报告
如果您在使用StatementGenerator时遇到问题，请通过Issues提交您的问题。尽可能详细描述问题场景和步骤，以便我们可以复现并解决它。

## 支持与捐款
如果您觉得这个项目有用并想要支持它，可以考虑捐款。您的支持将非常感激。

![Donation](/images/收款.jpg "捐款")
# usdt trc20：TB5T5myn4U2ZzKguK5juZKzTGTWxxwkizP

## 
