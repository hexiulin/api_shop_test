import pytest
import requests
from config import BASE_URL, ADMIN_USER, ADMIN_PWD


@pytest.fixture(scope="session",autouse=True)
def reset_test_env():
    print("\n\n==========正在重置测试环境数据 ==========")
    #登录管理员账号
    login_url=f"{BASE_URL}/login"
    login_data={"username":ADMIN_USER,"password":ADMIN_PWD}

    try:
        login_res=requests.post(login_url,json=login_data).json()
        admin_token=login_res["token"]
        #调用重置接口
        reset_url="http://43.133.227.52/api/reset"
        headers={"Authorization":f"Bearer {admin_token}"}
        reset_res=requests.post(reset_url,headers=headers).json()
        print(f"========== 环境重置成功: {reset_res.get('message')} ==========\n")

    except Exception as e:
        print(f"==========环境重置失败，请检查后端服务: {e} ==========")

