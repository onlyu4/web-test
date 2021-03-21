from selenium import webdriver

#获取浏览器对象
driver = webdriver.Chrome()

#最大化浏览器
driver.maximize_window()

#隐式等待
driver.implicitly_wait(30)


#打开url
url = "https://www.suning.com/?utm_source=baidu&utm_medium=brand&utm_campaign=title&utm_term=brand"
driver.get(url)
#找到登录按钮并点击
driver.find_element_by_link_text("请登录").click()
driver.find_element_by_link_text("账户登录").click()

#输入用户名
driver.find_element_by_xpath('//*[@id="userName"]').send_keys("177895881216")
#输入密码
driver.find_element_by_xpath('//*[@id="password"]').send_keys("adjaklhfgjd")
#点击登录按钮


