import unittest
from selenium import webdriver
from time import sleep
import time

'''
    目标：
        输入正确的用户名密码，验证码为空
        断言：提示信息是否为，验证码不能为空
        要求：如果断言出错，截图保存
'''

class Test_Login(unittest.TestCase):
    #定义初始化方法
    def setUp(self):

        #获取浏览器驱动
        self.driver = webdriver.Chrome()

        #最大化浏览器
        self.driver.maximize_window()

        #隐式等待
        self.driver.implicitly_wait(30)

    # 定义结束方法
    def tearDown(self):
        self.driver.quit()

    #定义测试方法，验证码为空
    def test_login(self):
        # 打开url
        url = "http://www.jszwfw.gov.cn/jsjis/front/login.do"
        self.driver.get(url)

        #找到用户名输入框输入13011112222
        self.driver.find_element_by_css_selector("#grusername").send_keys("13011112222")

        #找到密码输入框输入123456
        self.driver.find_element_by_css_selector("#grpwd").send_keys("123456")

        #找到登录按钮并点击
        self.driver.find_element_by_css_selector("#grloginform > div.login_mc_a > a.login_lg").click()

        #找到弹出框
        al =self.driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body").text
        print(al)
        # sleep(5)


         #断言
        exp = "请填写图形验证码"
        try:
            self.assertEqual(al,exp)
        except AssertionError:
            self.driver.get_screenshot_as_file("./error.png")
            #抛出异常
            raise
