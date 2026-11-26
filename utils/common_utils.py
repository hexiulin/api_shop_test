import json


def safe_parse(data_str):
    #  如果为空，直接返回 None
    if not data_str or not isinstance(data_str,str):
        return None

    try:
        # JSON 解析
        fixed_str=data_str.replace("'",'"')
        return json.loads(fixed_str)
    except json.JSONDecodeError:
        #解析失败，返回原字符串
        return data_str

