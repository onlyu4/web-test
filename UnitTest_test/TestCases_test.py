'''
案例：
    测试求和测试函数
'''

#导包
import unittest


#编写求和函数
def Sum_Up(x,y):
    return x + y


#定义测试类并继承
class Test_Sum_Up(unittest.TestCase):
    #定义测试方法 以test开头
    def test_sum_up(self):
        #调用要测试的函数
        result = Sum_Up(3,5)
        print(f"结果为：{result}")

    def test_sum_up2(self):
        result = Sum_Up(1,20)
        print(f"结果为:{result}")


