from selenium import webdriver
import time

#获取浏览器对象
driver = webdriver.Chrome()

#打开url
url = "http://www.baidu.com"
driver.get(url)

#查找输入框元素
input_box = driver.find_element_by_id("kw")

#输入搜索内容
input_box.send_keys("北京天气")

#查找百度一下元素
button = driver.find_element_by_id("su")

time.sleep(3)

#点击百度一下
button.click()
print("完成")