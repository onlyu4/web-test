
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

driver.get("http://www.beidaihe.com.cn/demolregist")


#获取文本框大小
size = driver.find_element_by_css_selector("#body_step1 > div > div:nth-child(1) > input").size
print(f"文本框的大小为：{size}")
#获取页面第一个超文本链接内容
text = driver.find_element_by_css_selector("a").text
print(f"第一个超文本链接为：{text}")



#获取页面上第一个超文本链接地址
url = driver.find_element_by_css_selector("#reloadcodelogin").get_attribute("href")
print(f"第一个超文本链接的url为：{url}")
#判断span元素是否可见
display = driver.find_element_by_css_selector("span").is_displayed()
print(f"span标签是否可见：{display}")

#判断注册按钮是否可用
enable = driver.find_element_by_css_selector("#next").is_enabled()
print(f"注册按钮是否可用:{enable}")

#判断性别是否选中
select = driver.find_element_by_css_selector("#body_step1 > div > div:nth-child(6) > label:nth-child(2) > input[type=radio]").is_selected()
print(f"性别是否选中：{select}")