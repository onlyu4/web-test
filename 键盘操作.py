
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
from selenium.webdriver.common.keys import Keys

#打开注册页面
url = "http://www.beidaihe.com.cn/demolregist"
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get(url)

#输入用户名admin1   删除1
username = driver.find_element_by_css_selector("#body_step1 > div > div:nth-child(1) > input")
username.send_keys("admin1")
username.send_keys(Keys.BACK_SPACE)
#全选用户名
username.send_keys(Keys.CONTROL,"a")

#复制用户名
username.send_keys(Keys.CONTROL,"c")

#粘贴到电子邮箱
e_mail = driver.find_element_by_css_selector("#body_step1 > div > div:nth-child(5) > input")
e_mail.send_keys(Keys.CONTROL,"v")