# 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

# a = ['1','2','3','4']

# list = []
# for i in a:
#     # print(i)
#     for j in a:
#         for k in a:
#             if i==j or k== i or k==j:
#                 continue
#             else:
#                 list.append(i+j+k)
# print(len(list))
# print(list)



# for i in range(1,10):
#     for j in range(1,i+1):
#             print(j,'*',i,'=',i*j,end='\t')
#     print('')



'''题目：企业发放的奖金根据利润提成。
利润(I)低于或等于10万元时，奖金可提10%；
利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，
可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；
60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
程序分析：请利用数轴来分界，定位。
'''
# i = int(input('请输入利润：'))
#
# if i <= 10:
#     money = i*0.1
# elif i > 10 and i <20:
#     money = ((i-10)*0.075)+(10*0.1)
# elif i >= 20 and i < 40:
#     money = (10*0.075)+(10*0.1)+((i-20)*0.05)
# elif i >= 40 and i < 60:
#     money =(10*0.075)+(10*0.1)+(20*0.05)+((i-40)*0.03)
# elif i >= 60 and i < 100:
#     money = (10*0.075)+(10*0.1)+(20*0.05)+(20*0.03)+((i-60)*0.015)
# elif i >= 100:
#     money =(10*0.075)+(10*0.1)+(20*0.05)+(20*0.03)+(60*0.015)+((i - 60) * 0.01)
# print(money)




# i = int(input('净利润:'))
# arr = [1000000, 600000, 400000, 200000, 100000, 0]
# rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
# r = 0
# for idx in range(0, 6):
#     if i > arr[idx]:
#         r += (i - arr[idx]) * rat[idx]
#         print((i - arr[idx]) * rat[idx])
#         i = arr[idx]
# print(r)

'''
给定一个整数n，执行以下条件操作：
如果n是奇数，打印Weird
如果n是偶数并且在包含的范围内2到5，打印Not Weird
如果n是偶数并且在包含的范围内6到20，打印Weird
如果n甚至大于20， 打印Not Weird
'''


# n = int(input('请输入整数n：'))
# if n%2==1 and n>=1 and n<=100:
#     print('Weird')
# elif n%2 == 0 and n>2 and n<5:
#     print('Not Weird')
# elif n%2 == 0 and n>6 and n<20:
#     print('Weird')
# elif n > 20 and n<=100:
#     print('Not Weird')
# else:
#     print('输入错误！')


'''
已知一个字符串为 “hello_world_yoyo”, 如何得到一个队列 [“hello”,”world”,”yoyo”]
'''

# l = 'hello_world_yoyo'
# list = l.split('_')
# print(list)

'''
有个列表 [“hello”, “world”, “yoyo”]如何把把列表里面的字符串联起来，得到字符串 “hello_world_yoyo”
'''

list = ['hello', 'world', 'yoyo']
# l = "_".join(list)
# print(l)


# j = ''
# for l in list:
#    j = j+'_'+l
#
# print(j)
# print(j.lstrip('_'))

'''
把字符串 s 中的每个空格替换成”%20”
输入：s = “We are happy.”
输出：”We%20are%20happy.”
'''
# s = 'We are happy.'
# print(s.replace(' ','%20'))

'''
打印99乘法表
'''

for i in range(1,10):
    for j in range(1,i+1):
        print('{}*{}={}'.format(j,i,i*j),end=' ')
    print('')