from  selenium import webdriver

#创建浏览器对象
driver = webdriver.Chrome()

#最大化浏览器
driver.maximize_window()

#打开百度 搜索北京天气
url = "http://www.baidu.com"
driver.get(url)
driver.find_element_by_id("kw").send_keys("北京天气")

#点击搜索按钮
driver.find_element_by_id("su").click()

#设置js语句
js = "window.scrollTo(0,1000)"

#执行js语句
driver.execute_script(js)