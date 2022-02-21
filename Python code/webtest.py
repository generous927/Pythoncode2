#coding=utf-8
from selenium import webdriver
import time

# driver = webdriver.Chrome(r'D:\chromedriver\chromedriver.exe')#叫做webDriver的实例对象
# driver.implicitly_wait(10)#等待时间
driver = webdriver.Chrome(r'D:\chromedriver\chromedriver.exe')
#打开网址
driver.get('http://121.42.15.146:9090/mtx/')
#点击登录并进入登录页面
driver.find_element_by_link_text('登录').click()
#输入用户名
driver.find_element_by_name('accounts').send_keys('shamotest1')
#输入密码
driver.find_element_by_name('pwd').send_keys('123456')
#点击登录按钮,class如果包含了空格，需要使用空格分隔的一部分进行定位
driver.find_element_by_class_name('btn-loading-example').click()