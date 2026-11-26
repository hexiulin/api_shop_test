import os
import shutil
import subprocess

import pytest


if __name__ == '__main__':

    #每次点运行前，先清空一下旧报告数据
    if os.path.exists("./report/html_report"):
        shutil.rmtree("./report/html_report")
    groups=["支付流","取消流","删除流"]
    for group in groups:
        print(f"\n==========开始执行：{group} ==========")
        os.environ["TEST_GROUP"] = group
        # 用 subprocess 启动一个全新的 Pytest 进程,不会有内存缓存
        subprocess.run(["pytest","-vs"])

    os.system("allure generate ./report/json_report -o ./report/html_report --clean")
