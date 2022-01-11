#coding=utf-8
from selenium import webdriver
import time


driver = webdriver.Chrome(r'D:\chromedriver.exe')#叫做webDriver的实例对象
driver.implicitly_wait(10)#等待时间

#打开网站
driver.get('http://www.51job.com')

driver.find_element_by_id('kwdselectid').send_keys('python')
driver.find_element_by_id('work_position_input').click()

cityEles = driver.find_elements_by_css_selector('#work_position_click_center_right em')

for one in cityEles:
    cityName = one.text
    selected = one.get_attribute('class')

    if cityName == u'南京':
        if selected != 'on':
            one.click()

    else:
        if selected == 'on':
            one.click()


driver.find_element_by_id('work_position_click_bottom_save').click()

driver.find_element_by_css_selector('.ush button').click()

jobs = driver.find_elements_by_css_selector('#resultList div.el')

for job in jobs:
    if 'title' in job.get_attribute('class'):
        continue
    filelds = job.find_elements_by_tag_name('span')
    strField = [fileld.text for fileld in filelds]
    print('|'.join(strField))

driver.quit()
