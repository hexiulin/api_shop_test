import os

import jsonpath
import pytest
import requests
import json
import allure
from config import BASE_URL
from utils.logger import logger
from utils.common_utils import safe_parse
from utils.excel_utils import read_excel

class TestRunner:
    data=read_excel()
    #提取后数据需要初始化一个全局的属性来保存，可以使用{}空字典
    all={}
    print(data)

    @allure.feature("电商核心业务流程")
    @pytest.mark.parametrize("case", data)
    def test_shop_test(self,case):
        #动态生成用例（格式：编号—场景—标题）
        allure.dynamic.story(case["feature"])#子模块
        allure.dynamic.title(f"用例{case['id']}-{case['title']}")
        all_vars =self.all

        #把字典转换成json字符串
        case_str=json.dumps(case)
        #遍历保存的变量（比如TOKEN）
        for key,value in all_vars.items():
            old_str = "{{" + key + "}}"
            case_str=case_str.replace(old_str,str(value))
        #把替换后的字符串，重新安全地变回 Python 字典
        case=json.loads(case_str)

        #解析数据
        method=case["method"]
        url=f"{BASE_URL}/"+case["path"]
        headers = safe_parse(case.get("headers"))
        params = safe_parse(case.get("params"))
        data = safe_parse(case.get("data"))
        json_data = safe_parse(case.get("json"))
        files = safe_parse(case.get("files"))

        request_data={
            "method":method,
            "url":url,
            "headers":headers,
            "params":params,
            "data":data,
            "json":json_data,
            "files":files
        }

        with allure.step(f"发送请求: {method} {url}"):

            logger.info(f"正在发送请求:{method} {url}|参数:{request_data}")#记录请求日志
            res=requests.request(**request_data)
            logger.info(f"接口响应:{res.text}")# 记录响应日志

            # 把请求参数和响应内容附加到报告里（方便排查 Bug）
            allure.attach(str(request_data), "请求数据", allure.attachment_type.TEXT)
            allure.attach(res.text, "响应结果", allure.attachment_type.TEXT)

        with allure.step("校验响应结果"):
            try:
                if case["check"]:
                    ret = jsonpath.jsonpath(res.json(), case["check"])
                    assert ret is not False, "缺少字段"
                    if case["expected"]:
                        assert str(ret[0]) == str(case["expected"])
                else:
                    assert case["expected"] in res.text
            except AssertionError as e:
                logger.error(f"用例[{case['id']}]断言失败！原因：{e}")
                raise e

        with allure.step("提取后置参数"):
            #JSON提取
            if case["jsonExData"]:
                for key,value in eval(case["jsonExData"]).items():
                    value=jsonpath.jsonpath(res.json(), value)[0]
                    all_vars[key]=value

