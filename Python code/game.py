# import random
# print("*"*30)
# print("欢迎进入澳门赌场")
# print("*"*3)
#
# username = input('请输入您的名字：')
# money = 0
# answer = input('确定进入游戏吗（y/n）？')
#
# if answer=="y":
#     # 判断游戏币是否充足
#     while money<2:
#         n = int(input('金币不足，请充值（100元30币，充值必须是100的倍数）：'))
#         # 充值金额的判断
#         if n%100==0 and n>0:
#             money=(n//100)*30
#     print('当前剩余游戏币是：{},玩一局游戏扣除2个币'.format(money))
#
#     print('进入游戏..........')
#     while True:
#         # 模拟骰子 产生骰子的值
#         t1 = random.randint(1,6)
#         t2 = random.randint(1, 6)
#         money -= 2
#
#         print('系统洗牌完毕，请猜大小：')
#         guess = input('请输入大或者小：')
#
#         if (t1 + t2 >6 and guess == '大') or (t1 + t2 <= 6 and guess == '小'):
#             print('恭喜{}！本局游戏获奖励1个游戏币！'.format(username))
#             money += 1
#         else:
#             print('很遗憾！本局游戏输啦==')
#         answer = input('是否继续再来一局游戏，您当前的金币为{}，要扣除2枚游戏币？（y/n）'.format(money))
#         if answer != "y" or money < 2:
#             print('退出游戏啦啦啦啦')
#             break



a = "hello world"
print(a[-1:-6:-1])
print(a[0:5])
print(a[::-1])
print(a[-7:-10:-1])
print(a[2:8])

