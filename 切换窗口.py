
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

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)
url = "http://www.baidu.com"
driver.get(url)

#获取当前窗口句柄
current =driver.current_window_handle
print(f"当前窗口句柄为：{current}")

#点击首页新闻链接
driver.find_element_by_link_text("贴吧").click()

#获取所有句柄
handels = driver.window_handles
print(f"所有句柄为：{handels}")

#遍历列表
for i in handels:
    #如果列表中有和当前窗口不相等的句柄就切换到那个窗口
    if i != current:
        driver.switch_to.window(i)
        driver.find_element_by_css_selector("#tiebaCustomPassLogin > div.tieba-login-wrapper > div.tang-pass-footerBar > a").click()