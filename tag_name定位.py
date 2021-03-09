from selenium import webdriver
from time import sleep

#获取浏览器对象
driver = webdriver.Chrome()


# 打开url
url = "http://www.baidu.com"
driver.get(url)

#找到文本输入框的tag_name
input_box = driver.find_element_by_tag_name("input")

#输入北京天气
input_box.send_keys("北京天气")


#点击百度一下
button = driver.find_element_by_id("su").click()

sleep(3)

#关闭浏览器
driver.close()