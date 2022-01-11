#coding=utf-8
from selenium import webdriver
import time

driver = webdriver.Chrome(r'D:\chromedriver.exe')#叫做webDriver的实例对象
driver.implicitly_wait(10)#等待时间

driver.get('http://www.51job.com')#打开网址

ele1 = driver.find_element_by_id('kwdselectid')#叫做webElement对象

ele1.send_keys('python')

ele2 = driver.find_element_by_id('work_position_input')

ele2.click()

time.sleep(1)#需要加time，推迟调用线程的运行

eles = driver.find_elements_by_css_selector(
    '#work_position_click_center_right_list_000000 em[class=on]')

for ele in eles:
    ele.click()

driver.find_element_by_id(
    'work_position_click_center_right_list_category_000000_090200').click()

#选择城市
driver.find_element_by_id('work_position_click_bottom_save').click()

#点击搜索
driver.find_element_by_css_selector('.ush   button').click()

#搜索结果分析
jobs = driver.find_elements_by_css_selector('#resultList div[class=el]')

for job in jobs:
    fields = job.find_elements_by_tag_name('span')
    stringFilelds = [field.text for field in fields]
    print('|'.join(stringFilelds))



driver.quit()

