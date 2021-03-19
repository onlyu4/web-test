import unittest
from TestCases_test import Test_Sum_Up

#实例化unittest.testsuite()
suite = unittest.TestSuite()

#调用suite添加方法    方法1
suite.addTest(Test_Sum_Up("test_sum_up"))
suite.addTest(Test_Sum_Up("test_sum_up2"))



#执行测试套件
runner = unittest.TextTestRunner()
runner.run(suite)