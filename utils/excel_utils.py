import os
import openpyxl

def read_excel(file_name="data/api_shop.xlsx", sheet_name="Sheet1"):
    #动态获取当前文件的绝对路径，拨两次洋葱回到项目根目录
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    #自动拼接出excel路径
    file_path =os.path.join(base_dir,file_name)

    workbook=openpyxl.load_workbook(file_path)
    worksheet=workbook[sheet_name]

    data =[]
    #动态获取表头
    keys=[str(cell.value).strip() if cell.value is not None else cell.value for cell in worksheet[2]]

    current_group = os.environ.get("TEST_GROUP")

    for row in worksheet.iter_rows(min_row=3,values_only=True):
        d_data=dict(zip(keys,row))
        #如果读取的is_true字段是true，则append
        if d_data["is_true"]:

            if current_group:
                if current_group not in str(d_data.get("group")):
                    continue
            data.append(d_data)
    return data

