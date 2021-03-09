from  selenium import webdriver

#获取浏览器对象
driver = webdriver.Chrome()

#打开url
url = "http://www.baidu.com"
driver.get(url)

#查找输入框  输入北京天气
input_box = driver.find_element_by_name("wd").send_keys("北京天气")


#点击百度一下
search = driver.find_element_by_id("su")
search.click()

