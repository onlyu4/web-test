from selenium import webdriver

#获取浏览器对象
driver = webdriver.Chrome()

#最大化浏览器
driver.maximize_window()

#隐式等待
driver.implicitly_wait(30)


#打开url
url = "http://www.jszwfw.gov.cn/jsjis/front/login.do"
driver.get(url)

#输入用户名
driver.find_element_by_css_selector("#grusername").send_keys("177895881216")


#输入密码
driver.find_element_by_css_selector("#grpwd").send_keys("adjaklhfgjd")


#点击登录按钮
driver.find_element_by_css_selector("#grloginform > div.login_mc_a > a.login_lg").click()

#找到提示窗口
information = driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div:nth-child(2) > div").text
print(information)

#点击提示信息
driver.find_element_by_css_selector("body > div.panel.window.messager-window > div.messager-body.panel-body.panel-body-noborder.window-body > div.messager-button > a").click()

