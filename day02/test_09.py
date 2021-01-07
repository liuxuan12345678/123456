'''
mark标记：
1. skip 跳过用例不执行；skipif 满足条件，则跳过用例
2. 自定义的标记:接口自动化(api)，功能自动化(func)，界面自动化，冒烟测试(smoke)。
    通过自定义标记，标记用例属于哪一类。需要在配置文件（pytest.ini）中定义标记。注：配置文件中的分号(;)表示注解
    比如版本转测试，需要进行冒烟测试，只执行带有冒烟标记的用例

    以下标记直接写在（addopts = -v --html=report/report.html --self-contained-html --reruns=3）之后，
    eg: addopts = -v --html=report/report.html --self-contained-html --reruns=3 -m=api
    -m=smoke 执行带smoke标记的用例
    -m=func
    -m="smoke and func" 执行带smoke标记和func标记的用例
    -m="smoke or func" 执行带smoke标记或func标记的用例
    -m="not smoke" 执行不带smoke标记的用例
'''

import pytest
version = 'V1R1'

@pytest.mark.smoke
def test_case01():
    print("用例1")

@pytest.mark.skip("跳过原因：缺陷，改动比较大，作为以后版本的需求来实现")
def test_case02():
    print("用例2")

@pytest.mark.skipif(version == 'V1R1',reason='V1R1版本不支持，如果是V1R1版本，则跳过')
def test_case03():
    print("用例3")

@pytest.mark.func
def test_case04():
    print("用例4")

def test_case05():
    print("用例5")

@pytest.mark.func  # 标记写在类上面，表示类下面所有的方法都被标记
class TestClass:
    @pytest.mark.smoke
    def test_case06(self):
        print("用例6")

    @pytest.mark.smoke  # 对类下面的所有用例生效
    def test_case07(self):
        print("用例7")

    @pytest.mark.api
    def test_case08(self):
        print("用例8")

    def test_case09(self):
        print("用例9")

    @pytest.mark.api
    def test_case10(self):
        print("用例10")
