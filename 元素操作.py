
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

''''
需求：1、打开浏览器进入注册页面
      2、在电话号栏输入123456
      3、间隔三秒后修改为987654
      4、点击注册按钮
'''
#导包
from selenium import webdriver
from  time import sleep

#获取浏览器对象
driver = webdriver.Chrome()

#打开注册页面
url = "http://www.beidaihe.com.cn/demolregist"
driver.get(url)

#填写手机号
phone_number = driver.find_element_by_xpath('//*[@id="body_step1"]/div/div[2]/input').send_keys("123456")
print(phone_number.s)
#停止三秒
sleep(3)

#修改手机号

driver.find_element_by_xpath('//*[@id="body_step1"]/div/div[2]/input').clear()
new_phone_number = driver.find_element_by_xpath('//*[@id="body_step1"]/div/div[2]/input').send_keys("987654")
print(new_phone_number)

#点击注册按钮
tap = driver.find_element_by_id("next").click()

sleep(3)

#关闭浏览器
driver.close()