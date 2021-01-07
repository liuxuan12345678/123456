'''
自动管理Cookie
requests中的Session类，能够自动获取和管理Cookie
'''

import  requests
s = requests.session()
print("登录前的cookie",s.cookies)

# 登录接口 Login
# 使用session发送请求
loginData = {
    "account":"2780487875@qq.com",
    "password":"qq2780487875"
}
r = s.post("https://www.bagevent.com/user/login", data = loginData)
# print(r.text)
print("登录后的cookie",s.cookies)

# dashboard 接口
r = s.get("https://www.bagevent.com/account/dashboard")
# print(r.text)
print("dashboard接口的cookie",s.cookies)


# 退出登录 logout
r = s.get("https://www.bagevent.com/user/login_out")
# print(r.text)
print("退出后的cookie",s.cookies)

# RequestsCookiejar转成字典
d = requests.utils.dict_from_cookiejar(s.cookies)
print(d)

