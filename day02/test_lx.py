import pytest
import requests

@pytest.fixture(params=[{"data":{"mobilephone":18012345678, "pwd":123456},
                         "expect":{"User-Agent": "python-requests/2.25.0"}},
                        {"data": {"mobilephone": 18012345678, "pwd": 12345},
                         "expect": {"User-Agent": "python-requests/2.25.0"}}])
def register_data(request): # request 是pytest中的关键字，固定写法
    return request.param  #通过request.param返回每一组数据，固定写法

# 数据驱动测试
# 登录功能的测试脚本
def test_register(register_data):
    url = "http://www.httpbin.org/post"
    print(f"注册功能，测试数据为：{register_data['data']}")

    r = requests.post(url, data=register_data['data'])
    print(r.json())

    assert r.json()['headers']['User-Agent'] == register_data['expect']['User-Agent']
