# print(10//3)

#幂函数
# print(pow(2,3))

#海龟绘图法
# from turtle import *
# forward(100)
# left(120)
# forward(100)
# left(120)
# forward(100)

#转译符
# print("\"hello,world!\" she said")

#索引
# fourth = input('Year:')[3]
# print(fourth)

# 将以数指定年、月、日的日期打印出来
months = [
    'Jan',
    'Feb',
    'Mar',
    'Apr',
    'May',
    'Jun',
    'Jul',
    'Aug',
    'Sep',
    'Oct',
    'Nov',
    'Dec'
]
# 一个列表，其中包含数1～31对应的结尾
endings = ['st', 'nd', 'rd'] + 17 * ['th'] \
 + ['st', 'nd', 'rd'] + 7 * ['th'] \
 + ['st']

print(endings)
year = input('Year: ')
month = input('Month (1-12): ')
day = input('Day (1-31): ')
month_number = int(month)
day_number = int(day)
# 别忘了将表示月和日的数减1，这样才能得到正确的索引
month_name = months[month_number-1]

# print(month_name)
ordinal = day + endings[day_number-1]
# print(ordinal)
print(month_name + ' ' + ordinal + ', ' + year)



