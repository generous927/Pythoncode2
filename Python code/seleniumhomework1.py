#coding=utf-8
from selenium import webdriver
from pprint import pprint
import time
import re

driver = webdriver.Chrome(r'D:\chromedriver.exe')#叫做webDriver的实例对象
driver.implicitly_wait(10)#等待时间


#打开网站
driver.get('http://www.weather.com.cn/html/province/jiangsu.shtml')

#定位元素，取其文本并进行切片处理
cityWeather = driver.find_element_by_id("forecastID").text.split("℃\n")
pprint(cityWeather)

#切片比较最低温度
lowestweather = 100
lowestcity = []
for one in cityWeather:
    one = one.replace(u'℃','')
    print(one)
    # one = re.sub("\D","",one)#只保留字符串中的纯数字，才能强制转换成int型
    curweather = int(one.split('\n')[-1].split('/')[-1])
    if curweather < lowestweather:
        lowestweather = curweather
        lowestcity.append(one.split('\n')[-2])
    elif curweather == lowestweather:
        lowestcity.append(one.split('\n')[-2])



print('温度最低为%s℃，城市有%s'%(lowestweather,''.join(lowestcity)))

driver.quit()