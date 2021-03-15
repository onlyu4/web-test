
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
from selenium.webdriver.support.select import Select
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
#driver.implicitly_wait(30)
url = "file:///C:/Users/17310/Downloads/%E6%B3%A8%E5%86%8CA.html"
driver.get(url)

'''
    使用css定位

#定位上海
driver.find_element_by_css_selector("#selectA > option:nth-child(2)").click()
#暂停两秒
sleep(2)
#定位广州
driver.find_element_by_css_selector("#selectA > option:nth-child(3)").click()
'''
#使用select定位
#select类时通过select标签控制的
el = driver.find_element_by_css_selector("#selectA")
select =Select(el)
select.select_by_index(1)   #通过下标方式访问
sleep(3)
#定位上海
select.select_by_index(2)       #通过下标方式访问

#停止2秒

#定位广州