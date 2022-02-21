# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *

auto_setup(__file__,devices='android://127.0.0.1:5037/MQS7N19524003765',logdir=True)


from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

touch(Template(r"D:\learn\airtestcode\Airtestrun.air\tpl1644473193503.png", record_pos=(-0.189, 0.243), resolution=(1080, 2340)))

sleep(2.0)

poco(text='歌单').click()

