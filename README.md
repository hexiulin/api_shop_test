# 电商系统接口自动化测试框架 (API Test Framework)

## 📖 项目简介
本项目基于 `Python + Pytest + Requests + Allure` 构建，针对电商系统核心业务流程（登录、商品、购物车、订单流转）进行接口自动化测试。采用 Excel 数据驱动模式，实现了测试数据与代码逻辑的完全解耦，并具备完善的环境重置、上下文变量流转、多场景隔离执行及全链路日志记录能力。

## 🛠️ 技术栈
*   **测试框架**：Pytest
*   **请求库**：Requests
*   **数据驱动**：Openpyxl (Excel)
*   **测试报告**：Allure Report
*   **日志系统**：Logging

## 📁 目录结构
```text
api_shop_test/
├── conftest.py        # 全局配置，自动重置测试环境数据
├── run.py             # 统一调度入口，按业务流分组启动测试
├── config.py          # 环境变量与全局配置（URL、账号等）
├── pytest.ini         # Pytest 核心配置文件
├── data/              # 存放 Excel 测试用例数据
├── report/            # Allure 原始数据与生成的 HTML 报告
├── testcases/         # 核心测试用例执行脚本
└── utils/             # 公共工具包（Excel解析、日志封装、安全解析等）
