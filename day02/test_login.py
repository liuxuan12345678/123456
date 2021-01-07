import pytest
import requests

@pytest.fixture(params= [{"mobilephone":15006007018,"pwd":"","aa":"密码不能为空"},
          {"mobilephone":"","pwd":123456,"aa":"手机号不能为空"},
          {"mobilephone":"","pwd":"","aa":"手机号不能为空"},
          {"mobilephone":12345,"pwd":123456,"aa":"用户名或密码错误"}])
def login_data(request):
    return request.param

def test_login(login_data):
    url = "http://jy001:8081/futureloan/mvc/api/member/login"
    r = requests.post(url, data=login_data)
    print(r.text)
    print(f"密码为：{login_data['pwd']}")
    assert r.json()['msg'] == login_data['aa']
    # r.json()['msg']断言所需的内容，从r.text返回的结果中提取
    # 通常需要print(r.text)观察之后，再决定断言哪个K值比较合适

