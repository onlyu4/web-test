from selenium import webdriver
import time

#获取谷歌浏览器对象
driver = webdriver.Chrome()

#打开百度
driver.get("http://www.baidu.com")
driver.find_element_by_id("kw")



#退出对象
#driver.quit()
