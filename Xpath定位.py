
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
from  time import sleep

#获取浏览器对象
driver = webdriver.Chrome()
url = "http://www.beidaihe.com.cn/demolregist"

#打开浏览器
driver.get(url)

#使用绝对路径定位用户名填写admin
driver.find_element_by_xpath("/html/body/div/div/div[2]/form[1]/div/div/div[1]/input").send_keys("admin")

sleep(3)

#使用相对路径定位密码填写 123456
driver.find_element_by_xpath('//*[@id="password"]').send_keys("123456")
'''
#xpath常用的定位策略
    路径:
        绝对路径
        相对路径
    路径结合属性
    路径结合逻辑
    路径结合层级
    在工作中，如果能使用相对路径一定不用绝对路径
'''
