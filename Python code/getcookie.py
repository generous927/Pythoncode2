# import requests,json
# from pprint import pprint
# def login():
#     url_json = 'http://10.159.62.247/oa-console/user/login_pc.do'
#     data_json = json.dumps({'userPasswd':'123456',
#                             'userName':'%E9%99%B6%E8%8F%8A%E7%90%B4'
#                            })
#     r_json = requests.post(url_json,data_json)
#
#
#     pprint(r_json.text)
#     print(r_json.cookies)
#
# login()



    # data = {
    #     'userPasswd':'123456',
    #     'userName':'%E9%99%B6%E8%8F%8A%E7%90%B4'
    # }
    # headers = {
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
    #     "Content-Type": "application/json;charset=UTF-8",
    #     "Referer": "http://10.159.62.247/oa/login"
    # }
#     r = requests.post(
#         url='http://10.159.62.247/oa-console/user/login_pc.do',
#         data=data,
#         headers=headers)
#
#     print(r)
#     print(r.cookies)
#
# login()

import requests,json
from pprint import pprint
def login():
    url_json = 'http://10.159.62.247/oa-console/user/login_pc.do'
    data_json = json.dumps({'userPasswd':'0FA00516C7FA7350DED84B110C438F04',
                            'userName':'F9D663C7AC34273E81598DF8C44F9AB3'
                           })
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
        "Content-Type": "application/json;charset=UTF-8",
        "Referer": "http://10.159.62.247/oa/login"
    }
    r_json = requests.post(
                url=url_json,
                data=data_json,
                headers=headers)

    print(r_json)
    pprint(r_json.text)
    print(r_json.cookies)

login()