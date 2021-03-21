
#                    _ooOoo_
#                   o8888888o
#                   88" . "88
#                   (| -_- |)
#                    O\ = /O
#                ____/`---'\____
#              .   ' \\| |// `.
#               / \\||| : |||// \
#             / _||||| -:- |||||- \
#               | | \\\ - /// | |
#             | \_| ''\---/'' | |
#              \ .-\__ `-` ___/-. /
#           ___`. .' /--.--\ `. . __
#        ."" '< `.___\_<|>_/___.' >'"".
#       | | : `- \`.;`\ _ /`;.`/ - ` : | |
#         \ \ `-. \_ __\ /__ _/ .-` / /
# ======`-.____`-.___\_____/___.-`____.-'======
#                    `=---='
#
# .............................................
#          佛祖保佑             永无BUG
#  佛曰:
#          写字楼里写字间，写字间里程序员；
#          程序人员写程序，又拿程序换酒钱。
#          酒醒只在网上坐，酒醉还来网下眠；
#          酒醉酒醒日复日，网上网下年复年。
#          但愿老死电脑间，不愿鞠躬老板前；
#          奔驰宝马贵者趣，公交自行程序员。
#          别人笑我忒疯癫，我笑自己命太贱；
#          不见满街漂亮妹，哪个归得程序员？

import unittest
import  time
from selenium import webdriver

#定义测试类
class Test_login(unittest.TestCase):
    driver = None
    #定义初始化方法
    @classmethod
    def setUp(cls):
        #获取浏览器对象
        cls.driver = webdriver.Chrome()

        #浏览器窗口最大化
        cls.driver.maximize_window()

        #设置隐式等待
        cls.driver.implicitly_wait(30)

        #打开url
        url = "http://www.jszwfw.gov.cn/jsjis/front/login.do"
        cls.driver.get(url)

    #设置关闭方法

    def tearDown(self):
        self.driver.quit()
    def test_login(self):

        #找到用户名输入框
        self.driver.find_element_by_css_selector("#grusername").send_keys("17310958352")

        #找到密码输入框
        self.driver.find_element_by_css_selector("#grpwd").send_keys("zhangsan")

        #找到登陆按钮并点击
        self.driver.find_element_by_css_selector("#grloginform > div.login_mc_a > a.login_lg").click()

        #找出提示信息并点击确定
        information = self.driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div:nth-child(2) > div").text
        print(information)

    def test_pwd(self):
        # 找到密码输入框
        self.driver.find_element_by_css_selector("#grpwd").send_keys("zhangsan")

        # 找到登陆按钮并点击
        self.driver.find_element_by_css_selector("#grloginform > div.login_mc_a > a.login_lg").click()

        # 找出提示信息并点击确定
        information = self.driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div:nth-child(2) > div").text
        print(information)
