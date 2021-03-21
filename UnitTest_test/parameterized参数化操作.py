import unittest
from parameterized import parameterized
'''
parameterized插件应用
测试多组数据
'''

def  test(x,y):
    return x+y

#定义测试类
#单个数据测试

# class Test(unittest.TestCase):
#     def test_sum_up(self):
#         re = test(1,2)
#         print(re)

class Test_sum_up(unittest.TestCase):
    #单组数据
    # @parameterized.expand(["1","2","3"])
    # def test_sum_up(self,num):
    #     print(f"mun:{num}")

    #多组数据
    list = [(1,2,3),(2,1,5)]
    @parameterized.expand(list)
    def test_sum_up(self, a, b, res):
        exp = test(a, b)
        if exp == res:
            print("测试通过")
        else:
            print(f"测试失败：测试用例{a, b}，实际结果为{exp},预计结果为{res}")