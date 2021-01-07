import requests

url = "http://jy001:8081/futureloan/mvc/api/member/register"
listes = [{"mobilephone":"15006008111","pwd":"","regname":"","aa":"密码不能为空","bb":"sign01"},
         {"mobilephone":"","pwd":"85846215","regname":"","aa":"手机号不能为空","bb":"sign02"},
         {"mobilephone":"","pwd":"","regname":"","aa":"手机号不能为空","bb":"sign031"},
         {"mobilephone":"18006007167","pwd":"","regname":"YY","aa":"密码不能为空","bb":"sign04"}]
for listt in listes:
    r = requests.post(url,data=listt)
    print(listt["bb"])
    assert r.json()['msg']==listt["aa"]






'''
ss = {"mobilephone":"15006008111","pwd":"","regname":""}
r = requests.post(url,data=ss)
print(r.text)
assert r.json()['msg']=="密码不能为空"

ss = {"mobilephone":"","pwd":"85846215","regname":""}
r = requests.post(url,data=ss)
print(r.text)
assert r.json()['msg']=="手机号不能为空"

ss = {"mobilephone":"","pwd":"","regname":""}
r = requests.post(url,data=ss)
print(r.text)
assert r.json()['msg']=="手机号不能为空"

ss = {"mobilephone":"18006007167","pwd":"","regname":"YY"}
r = requests.post(url,data=ss)
print(r.text)
assert r.json()['msg']=="密码不能为空"
'''



