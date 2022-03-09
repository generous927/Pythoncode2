#coding=utf-8
from appium import webdriver
import time,traceback

#配置
desired_caps = {}
desired_caps['platformName'] = 'Android'#所测设备的系统
desired_caps['platformVersion'] = '10'#系统版本
desired_caps['deviceName'] = 'test'#设备名称，可随意
desired_caps['app'] = r'C:\Users\Administrator\Desktop\toutiao_3.7.2.apk'#如果手机上不曾安装要测的apk，需要加上此参数，运行时会自动安装
desired_caps['appPackage'] = 'io.manong.developerdaily'#测试软件的包名，通过工具查看
desired_caps['appActivity'] = 'io.toutiao.android.ui.activity.LaunchActivity'#启动时打开的界面LaunchActivity，工具可查看
desired_caps['unicodeKeyboard'] = True#如果要在界面上输入汉字，加参数
desired_caps['resetKeyboard'] = True
desired_caps['noReset'] = True
desired_caps['newCommandTimeout'] = 6000
# desired_caps['automationName'] = 'uiautomator2'




#启动Remote RPC
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

try:
    driver.implicitly_wait(10)#找不到元素的时候可以循环去找

    #根据id找到元素并点击，id和html元素的id不同，id是元素的唯一标志的属性，前提是id不重复
    driver.find_element("io.manong.developerdaily:id/tab_bar_plus").click()
    time.sleep(1)
    eles = driver.find_elements("io.manong.developerdaily:id/tv_tab_title")
    for one in eles:
        one.click()
    time.sleep(1)
    # 输入用户名、密码
    ele = driver.find_element("io.manong.developerdaily:id/edt_phone")
    ele.send_keys('18912996796')
    ele = driver.find_element("io.manong.developerdaily:id/edt_password")
    ele.send_keys('123456t')
    time.sleep(2)
    # 点击登录
    driver.find_element('io.manong.developerdaily:id/btn_login').click()
    pass
except:
    print(traceback.format_exc())
    input(' ** ** Press toquit...')
    driver.quit()