#coding=utf-8
# tmp = input("你在干嘛啊？")
# game = "学习"
# while tmp != game:
#     print("还不快去学习！")
#     tmp = input("再给你一次机会，想好了再说？")
# print("干得漂亮！")

# import random
#
# tip = input("咱来猜一个范围在0-100之间的数字，请输入：")
# num = random.randint(0,100)
# print(num)
# while tip != num:
#     # print(type(tip))
#     # print(type(num))
#     if tip.isdigit():
#         if int(tip) > num:
#             print("大了大了")
#             tip = input("继续")
#         elif int(tip) == num:
#             break
#         else:
#             print("小了小了")
#             tip = input("继续")
#     else:
#         tip = input("请输入正确的数字哦！")
#
# print("恭喜你，猜对了！")


num = input("请输入您的分数：")

if num.isdigit():
    if num > 100:
        print("您的输入错误！")
        num = input("请输入1-100之间的分数：")
    elif num < 100:
        print("您的输入错误！")
        num = input("请输入1-100之间的分数：")
    else:
        if 100 >= num > 90:
            print("A")
        elif 90 >= num > 80:
            print("B")
        elif 80 >= num > 60:
            print("C")
        elif 60 >= num >= 0:
            print("D")
else:
    print("请输入数字！")
    num = input("请重新输入：")







# while int(num) > 100 :
#     if num.isdigit():
#         if 100 >= num > 90:
#             print("A")
#         elif 90 >= num > 80:
#             print("B")
#         elif 80 >= num > 60:
#             print("C")
#         elif 60 >= num >= 0:
#             print("D")
#     else:
#         print("请输入正确的分数！")
#         num = int(input("请重新输入您的分数："))


