#!/usr/bin/env python
#coding:utf-8

import codecs
import requests,json
url="http://10.159.62.247/oa/login"
headers={'Content-Type':'application/json;charset=UTF-8'}
request_param={
    "login_username":"陶菊琴",
    "login_pass":"123456"
}
response=requests.get(url,data=json.dumps(request_param), headers=headers)
token = response.json('token')
print(token)

# response.encoding = 'utf-8'
# print(response.text)

# print (response.text).encode('gbk','ignore')























# import requests
#
# header = { # 登录抓包获取的头部
# "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
# "Accept": "*/*",
# "Accept-Language": "zh-CN,zh;q=0.9",
# "Accept-Encoding": "gzip, deflate",
# "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
# "X-Requested-With": "XMLHttpRequest",
# "Content-Length": "423",
# "Connection": "keep-alive"
# }
#
# body = {"key1": "value1",
# "key2": "value2"} # 这里账号密码就是抓包的数据
#
# s = requests.session()
# login_url = "http://xxx.login" #　自己找带token网址
# login_ret = s.post(login_url, headers=header, data=body)
