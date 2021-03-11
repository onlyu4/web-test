
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
from selenium import webdriver
from time import sleep


#获取浏览器对象
driver = webdriver.Chrome()

#打开注册页面
url = "http://www.beidaihe.com.cn/demolregist"
driver.get(url)
#最大化浏览器
sleep(3)
driver.maximize_window()

#调整浏览器窗口大小
sleep(3)
driver.set_window_size(300,200)

#调整浏览器窗口位置
sleep(3)
driver.set_window_position(100,200)
#输入手机号
sleep(3)
driver.find_element_by_css_selector("#body_step1 > div > div:nth-child(2) > input").send_keys("123456")

#刷新
sleep(3)
driver.refresh()


#后退
sleep(3)
driver.back()

#前进
sleep(3)
driver.forward()

#获取当前页面title
print(driver.title)

#获取当前界面url
print(driver.current_url)

#关闭浏览器对象
driver.quit()


