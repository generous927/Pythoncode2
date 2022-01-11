#coding=utf-8
from selenium import webdriver
import time


driver = webdriver.Chrome(r'D:\chromedriver.exe')#叫做webDriver的实例对象
driver.implicitly_wait(10)#等待时间


#打开网站
driver.get('http://music.baidu.com/top/new')


div = driver.find_element_by_id("songListWrapper")
ul = div.find_element_by_tag_name("ul")
liList = ul.find_elements_by_tag_name("li")

for li in liList:
    upTags = li.find_elements_by_class_name("up")
    if upTags:

        title = li.find_element_by_class_name("song-title")



        titleStr = title.find_element_by_tag_name("a").text

        authorsStr = li.find_element_by_class_name("author_list").text


        print('{:10s}:{}'.format(titleStr,authorsStr))

driver.quit()