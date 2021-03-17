
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
'''
    警告框操作
    点击alert按钮
    输入用户名
'''
from  selenium import webdriver
from  time import sleep

#获取浏览器对象
driver = webdriver.Chrome()

#最大化浏览器
driver.maximize_window()

#打开网页
url = "file:///C:/Users/17310/AppData/Local/Temp/baiduyunguanjia/onlinedit/cache/e2818bcab6b8539c4be231b327c2cd44/%E6%B3%A8%E5%86%8CA.html"
driver.get(url)
sleep(3)

#找到alert按钮并点击
driver.find_element_by_css_selector("#alerta").click()
sleep(3)


#切换到弹出框
al = driver.switch_to.alert

#打印弹出框信息
print(f"弹出框消息：{al.text}")

#点击同意
al.accept()

sleep(3)


#输入用户名admin
driver.find_element_by_css_selector("#userA").send_keys("admin")

