'''
测试前置和后置：模块级和函数级

1. 方法名固定的写法
'''

def setup_module():
    print("测试前置：模块级，模块开始前执行一次")

def teardown_module():
    print("测试后置：模块级，模块结束后执行一次")

def setup_function():
    print("测试前置：函数级，每个用例开始前执行")

def teardown_function():
    print("测试前置：函数级，每个用例结束后执行")

def test_case001():
    print("测试用例1：密码为空")

def test_case002():
    print("测试用例2：手机号为空")
