import json
from websocket import create_connection

# 1、建立连接
ws = create_connection("ws://43.248.79.180:10040/")

# 2、获取连接状态
print("获取连接状态：", ws.getstatus())

# 3、发送请求参数
ws.send('{"T":"Req","ID":1,"A":"User.Login","P":{"udid":"test_001","pkgType":"Moye.Standalone.Test.Main","data":{"type":"test"},"lang":"zh"}}')

# 4、获取返回结果
result = ws.recv()
print("接收结果：", result)

# 5、关闭连接
ws.close()
