import pytest
import requests

@pytest.fixture(params=[{"data":{"mobilephone":18012345678, "pwd":123456},
                         "expect":{"status":0, "code":"20110", "data":None, "msg":"手机号码已被注册"}},
                        {"data": {"mobilephone": 18012345678, "pwd": 12345},
                         "expect": {"status": 0, "code": "20108", "data": None, "msg": "密码长度必须为6~18"}}])
def register_data(request): # request 是pytest中的关键字，固定写法
    return request.param  #通过request.param返回每一组数据，固定写法

# 数据驱动测试
# 登录功能的测试脚本
def test_register(register_data):
    url = "http://jy001:8081/futureloan/mvc/api/member/register"
    print(f"注册功能，测试数据为：{register_data['data']}")
    r = requests.post(url, data=register_data['data'])
    print(r.text)
    print(r.json())

    assert r.json()['msg'] == register_data['expect']['msg']
    assert r.json()['status'] == register_data['expect']['status']
    assert r.json()['code'] == register_data['expect']['code']