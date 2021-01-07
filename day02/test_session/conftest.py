'''
fixture 作用域为session级别时，
1.公共的方法放到conftest.py文件中.
2.pytest是根据文件名字找到这些方法的，不需要import.
3.整个执行过程，测试前置和后置执行一次。执行顺序按照文件的先后顺序,eg:conftest.py->test_add.py->test_modify.py
4.conftest.py 一个工程可以存在多个，对所在目录及其子目录生效。
5.运行test_session就可以运行这个文件夹下的所有.py文件

'''

import pytest

# 测试前置和后置
@pytest.fixture(scope='session')
def login():
    print("登录系统")
    yield
    print("退出登录")