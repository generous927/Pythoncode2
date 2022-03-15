# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             if( i != k ) and (i != j) and (j != k):
#                 print (i,j,k)


# name=input('Please enter your name:')


# print('hello',name)
# print('''line1
# line2
# line3''')


# age = 20
# if age >= 18:
# 	print("adult")
# elif age >=6:
# 	print("teenager")
# else:
# 	print('kid')


# s = input('birth:')
# birth = int(s)
# if birth < 2000:
# 	print('00前')
# else:
# 	print('00后')


# print ('--请输入您的身高体重，为您计算BMI值--')
# weight=float(input('your weight:'))
# height=float(input('your height:'))
# bmi=weight/(height**2)
# print('您的BMI指标是%.1f'%(bmi))
# if bmi <18.5:
# 	print('您的体重偏轻！')
# elif 18.5 <=bmi<25:
# 	print('您的体重正常！')
# elif 25<=bmi<28:
# 	print('您的体重偏重！')
# elif 28<=bmi<32:
# 	print('您的体重过重！')
# else:
# 	print('您太重了！')


# sum = 0
# for x in range(101):
# 	sum = sum + x
# print(sum)


# names = ['Micheal','Bob','Tracy']
# for name in names:
# 	print(name)


# sum = 0
# n = 99
# while n > 0:
# 	sum = sum + n
# 	n = n - 2
# print(sum)

# n = 1
# while n <= 100:
# 	print(n)
# 	n = n + 1
# print('END')

# n=1
# while n<=100:
# 	if n>10:
# 		break
# 	print(n)
# 	n=n+1
# print('END')

# list = range(0, 101, 1)
# for s in range(len(list)):
#     print(list[s])



# n = 0
# while n < 10:
# 	n = n + 1
# 	print(n)


# n = 0
# while n < 10:
# 	n = n + 1
# 	if n % 2 ==0:
# 		continue
# 	print(n)


# str_list=['a','a','a','b','a','c']
# s=set(str_list)
# d=dict.fromkeys(s,0)
# for i in s:
# 	d[i]=str_list.count(i)
# 	print(d)


# n=0
# for x in range(1,101):
# 	n=n+x
# 	print(n)

# print sum(range(1,101))


# sum = 0
# for x in range(101):
# 	sum += x
# 	print(sum)



# def my_abs(x):
# 	if x>=0:
# 		return(x)
# 	else:
# 		return(-x)
# print(my_abs(-9))

# try:
#     week = int(input("请输入："))
#     if type(week)==int:
#         print('这是周{}'.format(week))
#     else:
#         print('请重新输入！')
# except:
#     print("输入有误，请重新输入")

# while True:
#     try:
#         s = int(input("请输入1~7："))
#         weekday = ['星期一','星期二','星期三','星期四','星期五','星期六','星期日']
#         date = weekday[s-1]
#         print(date)
#         break
#     except:
#         print('输入的数据类型有误！')



# 这是开始
# counter = 100
# miles = 1000.0
# name = "John"
# print("",counter,'\n',miles,'\n',name)
#
# print('Hello World!')


# 三引号的用法
# i = '''This is my first python code
#         what's this?
#         it's a test code!
#    '''

# 指定自然字符串，字符串前加上R或r
# s = r"Newlines are indicated by \n"
# print(i,s)

# format的运用
# age = 25
# name = 'Swaroop'
# print('{0} is {1} years old'.format(name,age))
# print('Why is {0} playing with that python?'.format(name))

# i = 5
# print(i)
# i = i + 1
# print(i)
# s = '''This is a multi-line string.
# This is the second line.'''
# print(s)

# 运算符的优先级
# length = 5
# breadth = 2
# area = length * breadth
# print('Area is', area)
# print('Perimeter is',2 * (length + breadth))

# 控制流：if
# number = 23
# guess = int(input('Enter an integer: '))
# if guess == number:
#     print('Congratulations,you guessed it.')
#     print('(but you do not win any prizes!)')
# elif guess < number:
#     print('No,it is a little higher than that')
# else:
#     print('No,it is s little lower than that')
# print('Done')

# while
# number = 23
# running = True
# while running:
#     guess=int(input('Enter an integer:'))
#     if guess == number:
#         print('Congratulations, you guessed it.')
#         running = False
#     elif guess < number:
#         print('No,it is a little higher.')
#     else:
#         print('No,it is a little lower.')
# else:
#     print('the while loop is over.')
# print('done')


# for
# for i in range(1,5):
#     print(i)
# else:
#     print('The for loop is over')
#
# for s in range(0,-10,-1):
#     print(s)

# i = (input("Enter your name:"))
# for s in range(len(i)):
#     print(i[s])
# else:
#     print('Congratulations you get it!')


# break
# while True:
#     s = (input('Enter something :'))
#     if s == 'quit':
#         break
#     print('Length of the string is',len(s))
# print('Done')

# continue的缩进
# continue
# while True:
#     s = input('Enter something :')
#     if s == 'quit':
#         break
#     if len(s) < 3:
#         print('Too small')
#         continue
#     print('Input is of sufficent length')


# for letter in 'Python':     # 第一个实例
#    if letter == 'h':
#       continue
# print('当前字母 :', letter)

# 函数
# def sayHello():
#     print('Hello world!')
# sayHello()
# sayHello()

# def printMax(a,b):
#     if a > b:
#         print(a,'is maximum')
#     elif a == b:
#         print(a,'is equel to',b)
#     else:
#         print(b,'is maximnum')
#
# printMax(3,4)
#
# x = 5
# y = 7
# printMax(x,y)


# 局部变量
# x=50
#
# def func(x):
#     print('x is', x)
#     x=2
#     print('Changed local x to',x)
#
# func(x)
# print('x is still',x)


# 全局变量
# x=50
#
# def func():
#     global x
#
#     print('x is',x)
#     x=2
#     print('Changed global x to',x)
#
# func()
# print('Value of x is',x)


# def func_outer():
#     x = 2
#     print('x is',x)
#
#     def func_inner():
#         nonlocal x
#         x=5
#
#     func_inner()
#     print('Changed local x to',x)
#
# func_outer()


# def get_math_func(type,nn):
#     def square(n):
#         return n*n
#     def cube(n):
#         return n*n*n
#     def factorial(n):
#         result = 1
#         for index in range(2,n+1):
#             result *= index
#         return result
#     if type == "square":
#         return square(nn)
#     elif type == "cube":
#         return cube(nn)
#     else:
#         return factorial(nn)
# print(get_math_func('square',3))
# print(get_math_func('cube',3))
# print(get_math_func('',3))


# 默认参数值
# def say(message,time = 1):
#     print(message * time)
#
# say('Hello')
# say('World',5)

# 关键参数
# def func(a,b = 5,c = 10):
#     print('a is',a,'and b is',b,'and c is',c)
#
# func(3,7)
# func(25,c=24)
# func(c=50,a=100)

# VarArgs参数
# def total(initial = 5,*numbers,**keywords):
#     count = initial
#     for number in numbers:
#         count += number
#     for key in keywords:
#         count += keywords[key]
#     return count
# print(total(10,1,2,3,vegetables=50,fruits=100))

# Keyword-only参数
# def total(initial=5,*numbers,vegetables):
#     count=initial
#     for number in numbers:
#         count += number
#     count += vegetables
#     return count
#
# print(total(10,1,2,3,vegetables=50))
# print(total(10,1,2,3,vegetables=20))

# return,没有return等价于return None
# def maximum(x,y):
#     if x>y:
#         return x
#     else:
#         return y
#
# print(maximum(2,3))


# DocStrings（代码中带有格式的注释）
# def printMax(x,y):
#     '''Prints the maximum of two number.
#
#     The two values must be integers.'''
#     x=int(x)
#     y=int(y)
#
#     if x>y:
#         print(x,'is maximum')
#     else:
#         print(y,'is maximum')
#
# printMax(3,5)
# print(printMax.__doc__)


# 模块
# import sys
#
# print('The command line arguments are:')
# for i in sys.argv:
#     print('111111',i)
#
# print('\n\nThe PYTHONPATH is',sys.path,'\n')


# if __name__=='__main__':
#     print('This program is being run by itself')
# else:
#     print('I am being imported from another module')


# 这是写在mymodule中的函数
# def sayhi():
#     print('Hi,this is  mymodule speaking.')
#
# __version__='0.1'


# import mymodule
#
# mymodule.sayhi()
# print('Version',mymodule.__version__)


# from mymodule import sayhi,__version__
# sayhi()
# print('Version',__version__)


# dir函数，列出模块定义的标识符，属性列表
# import sys
# dir(sys)

# 包
# -<some folder present in the sys.path>/
#    - world/(包)
#        - __init__.py
#        - asia/(子包)
#            - __init__.py
#              - india/(模块)
#                  - __init__.py
#                  - foo.py(函数？？)
#        - afirca/(子包)
#            - __init__.py
#            - madagascar/(模块)
#                - __init__.py
#                - bar.py


# 数据结构
# 列表(list)
# shoplist = ['apple','mango','carrot','banana']
#
# print('I have',len(shoplist),'items to purchase.')
# print('These items are:',end='')
# for item in shoplist:
#     print("1111111")
#     print(item,end='')
# print('\nI also have to buy rice.')
# shoplist.append('rice')
# print('My shopping list is now',shoplist)
# print('I will sort my list now')
# shoplist.sort()
# print('Sorted shopping list is',shoplist)
# print('The first item I will buy is',shoplist[0])
# olditem=shoplist[0]
# del shoplist[0]
# print('I bought the',olditem)
# print('My shopping list is now',shoplist)


# 元组(将对象集合在一起)
# zoo = ('python','elephant','penguin')
# print('Number of animals in the zoo is',len(zoo))
# new_zoo = ('monkey','camel',zoo)
# print('Number of cages in the new zoo is',len(new_zoo))
# print('All animals in new zoo are',new_zoo)
# print('Animals brought from old zoo are',new_zoo[2])
# print('Last anmials brought from old zoo is',new_zoo[2][2])
# print('Number of animals in the new zoo is',len(new_zoo)-1+len(new_zoo[2]))


# 字典
# ab = {'Swaroop':'swaroop@swaroopch.com',
#       'Larry':'larry@wall.org',
#       'Matsumoto':'matz@ruby-lang.org',
#       'Spammer':'spammer@hotmail.com'
# }
#
# print("Swaroop's address is",ab['Swaroop'])
#
# del ab['Spammer']
# print('\nThere are {0} contacts in the address-book\n'.format(len(ab)))
# for name,address in ab.items():
#     print('Contact{0} at {1}'.format(name,address))
# ab['Guido']='guido@python.org'
# if 'Guido' in ab :#OR ab.has_key('Guido')
#     print("\nGuido's address is",ab['Guido'])


# 序列(索成员检验和索引操作符)
# shoplist = ['apple','mango','carrot','banana']
# name = 'swaroop'
#
# #Indexing or 'Subscription' operation
# print('Item 0 is',shoplist[0])
# print('Item 1 is',shoplist[1])
# print('Item 2 is',shoplist[2])
# print('Item 3 is',shoplist[3])
# print('Item -1 is',shoplist[-1])
# print('Item -2 is',shoplist[-2])
# print('Character 0 is',name[0])
# #Slicing on a list
# print('Item 1 to 3 is',shoplist[1:3])
# print('Item 2 to end is',shoplist[2:])
# print('Item 1 to -1 is',shoplist[1:-1])
# print('Item start to end is',shoplist[:])
# #Slicing on a string
# print('characters 1 to 3 is',name[1:3])
# print('characters 2 to end is',name[2:])
# print('characters 1 to -1 is',name[1:-1])
# print('characters start to end is',name[:])


# 集合
# bri = set(['brazil','russia','india'])
# print('india' in bri)
# print('usa' in bri)
# bric=bri.copy()
# bric.add('china')
# print(bric.issubset(bri))
# bri.remove('russia')
# s=bri&bric
# print(s)


# 引用
# print('Simple Assignment')
# shoplist = ['apple','mango','carrot','banana']
# mylist  = shoplist
#
# del shoplist[0]
#
# print('shoplist is',shoplist)
# print('mylist is',mylist)
#
# print('Copy by making a full slice')
# mylist = shoplist[:]
# del mylist[0]
#
# print('shoplist is',shoplist)
# print('mylist is',mylist)


# 字符串
# name = 'Swaroop'
# if name.startswith('Swa'):
#     print('Yes,the string starts with "Swa"')
# if 'a' in name:
#     print('Yes,it contains the string "a"')
# if name.find('war')!=-1:
#     print('Yes,it contains the string "war"')
# delimiter = '_*_'
# mylist = ['Brazil','Russia','India','China']
# print(delimiter.join(mylist))


# 我想写一个能给我所有重要文件建立备份的程序
# 1. 需要备份的文件和目录由一个列表指定。
# 2. 备份应该保存在主备份目录中。
# 3. 文件备份成一个 zip 文件。
# 4. zip 存档的名称是当前的日期和时间。
# 5. 我们使用标准的 zip 命令，它通常默认地随 Linux/Unix 发行版提供。Windows
# 用户可以从GnuWin32项目页安装。注意你可以使用任何存档命令，只要它有命令行界面就可以了
# 那样的话我们可以从我们的脚本中传递参数给它。
# 安装7zip，将7zip.exe放在C盘的Windows目录下；编码格式改为了GBK；format格式化报错

# import os
# import time
# 1.在列表中指定要备份的文件和目录
# source = ['"E:\\A bit of Python"']
# 注意，我们必须在字符串中使用双引号来表示名称
# 2.备份必须存储在主备份目录中
# spaces in it.
# target_dir = 'E:\\Backup'
# 记住改为你自己的目录
# using

# 3.这些文件备份到zip文件中
# 4.zip存档的名称是当前日期和时间
# target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'
# 5.我们使用zip命令将文件放在zip存档中
# zip_command = "7z a %s %s"%(target, ' '.join(source))
# zip_command = "7z {0} {1}".format(target,' '.join(source))
# 运行备份
# print(zip_command)
# if os.system(zip_command) == 0:
#     print('Successful backup to',target)
# else:
#     print('Backup FAILED')


# import os
# import time
# source = ['"E:\\A bit of Python"']
# target_dir = 'E:\\Backup'
# today = target_dir + os.sep + time.strftime('%Y%m%d')
# now = time.strftime('%H%M%S')
# if not os.path.exists(today):
#     os.mkdir(today)
#     print('Successfully created directory',today)
# target = today + os.sep + now + '.zip'
# zip_command = '7z a %s %s'%(target,' '.join(source))
# if os.system(zip_command)==0:
#     print('Successful backup to',target)
# else:
#     print('Backup FAILED')


# import os
# import time
# source = ['"E:\\A bit of Python"']
# target_dir = 'E:\\Backup'
# today = target_dir + os.sep + time.strftime('%Y%m%d')
# now = time.strftime('%H%M%S')
# comment = input('Enter a comment -->')
# if len(comment) == 0:
#     target = today + os.sep + now + '.zip'
# else:
#     target = today + os.sep + now + '_' + comment.replace(' ','_') + '.zip'
# if not os.path.exists(today):
#     os.mkdir(today)
#     print('Successfully created directory',today)
# zip_command = '7z a %s %s'%(target,' '.join(source))
# if os.system(zip_command) == 0:
#     print('Successful backup to',target)
# else:
#     print('Backup FAILED')


# import os
# import time
# source = ['"E:\\A bit of Python"']
# target_dir = 'E:\\Backup'
# today = target_dir + os.sep + time.strftime('%Y%m%d')
# now = time.strftime('%H%M%S')
# comment = input('Enter a comment -->')
# if len(comment) == 0:
#     target = today + os.sep + now + '.zip'
# else:
#     target = today + os.sep + now + '_' +\
#     comment.replace(' ','_') + '.zip'
# if not os.path.exists(today):
#     os.mkdir(today)
#     print('Successfully created directory',today)
# zip_command = "7z a %s %s"%(target,''.join(source))
# if os.system(zip_command) == 0:
#     print('Successful backup to',target)
# else:
#     print('Backup FAILED')
# str = 'this is string '


# 面向对象
# class Person:#创建一个类名
#     pass
# p = Person()#创建一个对象/实例
# print(p)


# class Person:
#     def sayHi(self):
#         print('Hello, how are you?')
# p = Person()
# p.sayHi()


# class Person:
#     def __init__(self, name):
#         self.name = name
#     def sayHi(self):
#         print('Hello, my name is ',self.name)
# p = Person('Swaroop')
# p.sayHi()


# class Robot:
#     '''Represents a robot, with a name.'''
#
#     #A class variable, counting the number of robots
#     population = 0
#
#     def __init__(self,name):
#         '''Initializes the data.'''
#         self.name = name
#         print('(Initialize {0})'.format(self.name))
#
#         #When this person is created, the robot
#         # adds to the population
#         Robot.population += 1
#
#     def __del__(self):
#         '''I am dying.'''
#         print('{0} is being destroyed!'.format(self.name))
#         Robot.population -= 1
#
#         if Robot.population == 0:
#             print('{0} was the last one'.format(self.name))
#         else:
#             print('There are still {0:d} robots working.'.format(Robot.population))
#     def sayHi(self):
#         '''Greeting by the robot.
#
#         Yeah, they can do that.'''
#         print('Greetings, my master call me {0}'.format(self.name))
#     def howMany():
#         '''Prints the current population.'''
#         print('We have {0:d} robots.'.format(Robot.population))
#     howMany = staticmethod(howMany)
#
# droid1 = Robot('R2-D2')
# droid1.sayHi()
# Robot.howMany()
#
# droid2 = Robot('C-3P0')
# droid2.sayHi()
# Robot.howMany()
#
# print("\nRobots can do some work here.\n")
# print("Robots have finished their work.So let's destroy them.")
#
# del droid1
# del droid2
#
# Robot.howMany()


# 继承
# class SchoolMember:
#     """Represent any school member."""
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         print('(Initalize SchoolMember:{0})'.format(self.name))
#
#     def tell(self):
#         """Tell my details."""
#         print('Name:"{0}" Age:"1"'.format(self.name,self.age),end = '')
#
# class Teacher(SchoolMember):
#     """Represent a teacher."""
#     def __init__(self,name,age,salary):
#         SchoolMember.__init__(self,name,age)
#         self.salary = salary
#         print('(Initialized Teacher:{0})'.format(self.name))
#
#     def tell(self):
#         SchoolMember.tell(self)
#         print('Salary:"{0:d}'.format(self.salary))
#
# class Student(SchoolMember):
#     """Represents a student"""
#     def __init__(self,name,age,marks):
#         SchoolMember.__init__(self,name,age)
#         self.marks = marks
#         print('(Initialized Student:{0})'.format(self,name))
#
#     def tell(self):
#         SchoolMember.tell(self)
#         print('Marks:"{0:d}"'.format(self.name))
#
#     def tell(self):
#         SchoolMember.tell(self)
#         print('Marks:"{0:d}"'.format(self.marks))
#
# t = Teacher('Mrs.Shrividya',30,30000)
# s = Student('Swaroop',25,75)
#
# print()  #prints a blank line
# members = [t,s]
# for member in members:
#     member.tell()  #work for both Teacher and Students


# 用户输入
# def reverse(text):
#     return text[::-1]
#
# def is_pailndrome(text):
#     return text == reverse(text)
#
# something = input('Enter text:')
# if (is_pailndrome(something)):
#     print("Yes, it is a palindrome")
# else:
#     print("No,it is not a palindrome")


# 文件
# poem = '''\
# Programming is fun
# When the work is done
# if you wanna make your work also fun:
#      use Python!
# '''
#
# f = open('poem.txt','w') # open for 'w'riting
# f.write(poem) #write text to file
# f.close() #close the file
#
# f = open('poem.txt') #if no mode is specified,'r'ead mode is assumed by defult
# while True:
#     line = f.readline()
#     if len(line) == 0:#Zero lengh indicates EOF
#         break
#     print(line,end='')
# f.close() # close the file


# print('小精灵：您好，欢迎古灵阁，请问您需要帮助吗？需要 or 不需要？\n')
#
# request = input('您的选择：')
#
# if request=='需要':
#
#     print('\n小精灵：请问您需要什么帮助呢？\n1 存取款；\n2 货币兑换；\n3 咨询')
#
#     choice = int(input('您的选择：'))
#
#     if choice == 1:
#
#         print('请您到存取款窗口。谢谢！')
#
#     elif choice == 2:
#
#         print('''
#
# 小精灵：金加隆和人民币的兑换率为1:51.3，即一金加隆=51.3人民币
#
# 小精灵：请问您需要兑换多少金加隆呢？
#
#         ''')
#
#         money = float(input('您要兑换的金加隆数：'))
#
#         print('\n小精灵：好的，我知道了，您需要兑换 ' + str(money) + ' 金加隆。')
#
#         print('小精灵：那么，您需要付给我' + str(money*51.3) + '人民币。')
#
#     else:
#
#         print('\n小精灵：请您去咨询窗口！谢谢！')
#
# else:
#
#     print('\n小精灵：好的！再见！')


# 通过selenium操作浏览器
# from selenium import webdriver
#
#
# driver = webdriver.Chrome()    # Chrome浏览器
# driver.get('https://www.baidu.com')
#
# print(driver.title)
#
# driver.quit()


# 控制浏览器窗口大小
# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.get("http://m.baidu.com")
#
# # 参数数字为像素点
# print("设置浏览器宽480、高800显示")
# driver.set_window_size(480, 800)
# driver.quit()


# #控制浏览器后退、前进
# from selenium import webdriver
#
# driver = webdriver.Chrome()
#
# #访问百度首页
# first_url= 'http://www.baidu.com'
# print("now access %s" %(first_url))
# driver.get(first_url)
#
# #访问新闻页面
# second_url='http://news.baidu.com'
# print("now access %s" %(second_url))
# driver.get(second_url)
#
# #返回（后退）到百度首页
# print("back to  %s "%(first_url))
# driver.back()
#
# # 前进到新闻页
# print("forward to  %s"%(second_url))
# driver.forward()
#
# driver.quit()

# 刷新页面
# driver.refresh()


# 点击和输入
# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.get("https://www.baidu.com")
#
# driver.find_element_by_id("kw").clear()
# driver.find_element_by_id("kw").send_keys("selenium")
# driver.find_element_by_id("su").click()
#
# driver.quit()


# 提交
# from selenium import webdriver
# #
# # driver = webdriver.Chrome()
# # driver.get("https://www.baidu.com")
# #
# # search_text = driver.find_element_by_id('kw')
# # search_text.send_keys('selenium')
# # search_text.submit()
# #
# # driver.quit()


# 其他常用方法
# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.get("http://www.baidu.com")
#
# # 获得输入框的尺寸
# size = driver.find_element_by_id('kw').size
# print(size)
#
# # 返回百度页面底部备案信息
# text = driver.find_element_by_id("cp").text
# print(text)
#
# # 返回元素的属性值， 可以是 id、 name、 type 或其他任意属性
# attribute = driver.find_element_by_id("kw").get_attribute('type')
# print(attribute)
#
# # 返回元素的结果是否可见， 返回结果为 True 或 False
# result = driver.find_element_by_id("kw").is_displayed()
# print(result)
#
# driver.quit()


# 鼠标悬停操作
# from selenium import webdriver
# # 引入 ActionChains 类
# from selenium.webdriver.common.action_chains import ActionChains
#
# driver = webdriver.Chrome()
# driver.get("https://www.baidu.cn")
#
# # 定位到要悬停的元素
# above = driver.find_element_by_link_text("设置")
# # 对定位到的元素执行鼠标悬停操作
# ActionChains(driver).move_to_element(above).perform()

# 键盘
# from selenium import webdriver
# # 引入 Keys 模块
# from selenium.webdriver.common.keys import Keys
#
# driver = webdriver.Chrome()
# driver.get("http://www.baidu.com")
#
# # 输入框输入内容
# driver.find_element_by_id("kw").send_keys("seleniumm")
#
# # 删除多输入的一个 m
# driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)
#
#
# # 输入空格键+“教程”
# driver.find_element_by_id("kw").send_keys(Keys.SPACE)
# driver.find_element_by_id("kw").send_keys("教程")
#
# # ctrl+a 全选输入框内容
# driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'a')
#
# # ctrl+x 剪切输入框内容
# driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'x')
#
# # ctrl+v 粘贴内容到输入框
# driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'v')
#
# # 通过回车键来代替单击操作
# driver.find_element_by_id("su").send_keys(Keys.ENTER)
# driver.quit()


# 断言
# from selenium import webdriver
# from time import sleep
#
#
# driver = webdriver.Chrome()
# driver.get("https://www.baidu.com")
#
# print('Before search================')
#
# # 打印当前页面title
# title = driver.title
# print(title)
#
# # 打印当前页面URL
# now_url = driver.current_url
# print(now_url)
#
# driver.find_element_by_id("kw").send_keys("selenium")
# driver.find_element_by_id("su").click()
# sleep(1)
#
# print('After search================')
#
# # 再次打印当前页面title
# title = driver.title
# print(title)
#
# # 打印当前页面URL
# now_url = driver.current_url
# print(now_url)
#
# # 获取结果数目
# user = driver.find_element_by_class_name('nums').text
# print(user)
#
# driver.quit()


# from turtle import *
# 
# def drawStar(x, y):
#     pu()
#     goto(x, y)
#     pd()
#     # set heading: 0
#     seth(0)
#     for i in range(5):
#         fd(40)
#         rt(144)
# 
# for x in range(0, 250, 50):
#     drawStar(x, 0)
# 
# done()


# !/usr/bin/env python
# coding=utf-8
# 画一棵樱花


# import turtle
# import random
# from turtle import *
# from time import sleep
#
#
# # 画樱花的躯干(60,t)
# def tree(branchLen, t):
#     sleep(0.0005)
#     if branchLen > 3:
#         if 8 <= branchLen <= 12:
#             if random.randint(0, 2) == 0:
#                 t.color('snow')  # 白
#             else:
#                 t.color('lightcoral')  # 淡珊瑚色
#             t.pensize(branchLen / 3)
#         elif branchLen < 8:
#             if random.randint(0, 1) == 0:
#                 t.color('snow')
#             else:
#                 t.color('lightcoral')  # 淡珊瑚色
#             t.pensize(branchLen / 2)
#         else:
#             t.color('sienna')  # 赭(zhě)色
#             t.pensize(branchLen / 10)  # 6
#         t.forward(branchLen)
#         a = 1.5 * random.random()
#         t.right(20 * a)
#         b = 1.5 * random.random()
#         tree(branchLen - 10 * b, t)
#         t.left(40 * a)
#         tree(branchLen - 10 * b, t)
#         t.right(20 * a)
#         t.up()
#         t.backward(branchLen)
#         t.down()
#
#
# # 掉落的花瓣
# def petal(m, t):
#     for i in range(m):
#         a = 200 - 400 * random.random()
#         b = 10 - 20 * random.random()
#         t.up()
#         t.forward(b)
#         t.left(90)
#         t.forward(a)
#         t.down()
#         t.color('lightcoral')  # 淡珊瑚色
#         t.circle(1)
#         t.up()
#         t.backward(a)
#         t.right(90)
#         t.backward(b)
#
#
# def main():
#     # 绘图区域
#     t = turtle.Turtle()
#     # 画布大小
#     w = turtle.Screen()
#     t.hideturtle()  # 隐藏画笔
#     t.getscreen().tracer(5, 0)
#     w.screensize(bg='wheat')  # wheat小麦
#     t.left(90)
#     t.up()
#     t.backward(150)
#     t.down()
#     t.color('sienna')
#
#     # 画樱花的躯干
#     tree(60, t)
#     # 掉落的花瓣
#     petal(200, t)
#     w.exitonclick()
#
#
# main()

# !/usr/bin/env python2
# coding=utf-8


# 小猪佩奇
# import turtle as t
#
# t.pensize(4)
# t.hideturtle()
# t.colormode(255)
# t.color((255, 155, 192), "pink")
# t.setup(840, 500)
# t.speed(10)
#
# # 鼻子
# t.pu()
# t.goto(-100, 100)
# t.pd()
# t.seth(-30)
# t.begin_fill()
# a = 0.4
# for i in range(120):
#     if 0 <= i < 30 or 60 <= i < 90:
#         a = a + 0.08
#         t.lt(3)  # 向左转3度
#         t.fd(a)  # 向前走a的步长
#     else:
#         a = a - 0.08
#         t.lt(3)
#         t.fd(a)
# t.end_fill()
#
# t.pu()
# t.seth(90)
# t.fd(25)
# t.seth(0)
# t.fd(10)
# t.pd()
# t.pencolor(255, 155, 192)
# t.seth(10)
# t.begin_fill()
# t.circle(5)
# t.color(160, 82, 45)
# t.end_fill()
#
# t.pu()
# t.seth(0)
# t.fd(20)
# t.pd()
# t.pencolor(255, 155, 192)
# t.seth(10)
# t.begin_fill()
# t.circle(5)
# t.color(160, 82, 45)
# t.end_fill()
#
# # 头
# t.color((255, 155, 192), "pink")
# t.pu()
# t.seth(90)
# t.fd(41)
# t.seth(0)
# t.fd(0)
# t.pd()
# t.begin_fill()
# t.seth(180)
# t.circle(300, -30)
# t.circle(100, -60)
# t.circle(80, -100)
# t.circle(150, -20)
# t.circle(60, -95)
# t.seth(161)
# t.circle(-300, 15)
# t.pu()
# t.goto(-100, 100)
# t.pd()
# t.seth(-30)
# a = 0.4
# for i in range(60):
#     if 0 <= i < 30 or 60 <= i < 90:
#         a = a + 0.08
#         t.lt(3)  # 向左转3度
#         t.fd(a)  # 向前走a的步长
#     else:
#         a = a - 0.08
#         t.lt(3)
#         t.fd(a)
# t.end_fill()
#
# # 耳朵
# t.color((255, 155, 192), "pink")
# t.pu()
# t.seth(90)
# t.fd(-7)
# t.seth(0)
# t.fd(70)
# t.pd()
# t.begin_fill()
# t.seth(100)
# t.circle(-50, 50)
# t.circle(-10, 120)
# t.circle(-50, 54)
# t.end_fill()
#
# t.pu()
# t.seth(90)
# t.fd(-12)
# t.seth(0)
# t.fd(30)
# t.pd()
# t.begin_fill()
# t.seth(100)
# t.circle(-50, 50)
# t.circle(-10, 120)
# t.circle(-50, 56)
# t.end_fill()
#
# # 眼睛
# t.color((255, 155, 192), "white")
# t.pu()
# t.seth(90)
# t.fd(-20)
# t.seth(0)
# t.fd(-95)
# t.pd()
# t.begin_fill()
# t.circle(15)
# t.end_fill()
#
# t.color("black")
# t.pu()
# t.seth(90)
# t.fd(12)
# t.seth(0)
# t.fd(-3)
# t.pd()
# t.begin_fill()
# t.circle(3)
# t.end_fill()
#
# t.color((255, 155, 192), "white")
# t.pu()
# t.seth(90)
# t.fd(-25)
# t.seth(0)
# t.fd(40)
# t.pd()
# t.begin_fill()
# t.circle(15)
# t.end_fill()
#
# t.color("black")
# t.pu()
# t.seth(90)
# t.fd(12)
# t.seth(0)
# t.fd(-3)
# t.pd()
# t.begin_fill()
# t.circle(3)
# t.end_fill()
#
# # 腮
# t.color((255, 155, 192))
# t.pu()
# t.seth(90)
# t.fd(-95)
# t.seth(0)
# t.fd(65)
# t.pd()
# t.begin_fill()
# t.circle(30)
# t.end_fill()
#
# # 嘴
# t.color(239, 69, 19)
# t.pu()
# t.seth(90)
# t.fd(15)
# t.seth(0)
# t.fd(-100)
# t.pd()
# t.seth(-80)
# t.circle(30, 40)
# t.circle(40, 80)
#
# # 身体
# t.color("red", (255, 99, 71))
# t.pu()
# t.seth(90)
# t.fd(-20)
# t.seth(0)
# t.fd(-78)
# t.pd()
# t.begin_fill()
# t.seth(-130)
# t.circle(100, 10)
# t.circle(300, 30)
# t.seth(0)
# t.fd(230)
# t.seth(90)
# t.circle(300, 30)
# t.circle(100, 3)
# t.color((255, 155, 192), (255, 100, 100))
# t.seth(-135)
# t.circle(-80, 63)
# t.circle(-150, 24)
# t.end_fill()
#
# # 手
# t.color((255, 155, 192))
# t.pu()
# t.seth(90)
# t.fd(-40)
# t.seth(0)
# t.fd(-27)
# t.pd()
# t.seth(-160)
# t.circle(300, 15)
# t.pu()
# t.seth(90)
# t.fd(15)
# t.seth(0)
# t.fd(0)
# t.pd()
# t.seth(-10)
# t.circle(-20, 90)
#
# t.pu()
# t.seth(90)
# t.fd(30)
# t.seth(0)
# t.fd(237)
# t.pd()
# t.seth(-20)
# t.circle(-300, 15)
# t.pu()
# t.seth(90)
# t.fd(20)
# t.seth(0)
# t.fd(0)
# t.pd()
# t.seth(-170)
# t.circle(20, 90)
#
# # 脚
# t.pensize(10)
# t.color((240, 128, 128))
# t.pu()
# t.seth(90)
# t.fd(-75)
# t.seth(0)
# t.fd(-180)
# t.pd()
# t.seth(-90)
# t.fd(40)
# t.seth(-180)
# t.color("black")
# t.pensize(15)
# t.fd(20)
#
# t.pensize(10)
# t.color((240, 128, 128))
# t.pu()
# t.seth(90)
# t.fd(40)
# t.seth(0)
# t.fd(90)
# t.pd()
# t.seth(-90)
# t.fd(40)
# t.seth(-180)
# t.color("black")
# t.pensize(15)
# t.fd(20)
#
# # 尾巴
# t.pensize(4)
# t.color((255, 155, 192))
# t.pu()
# t.seth(90)
# t.fd(70)
# t.seth(0)
# t.fd(95)
# t.pd()
# t.seth(0)
# t.circle(70, 20)
# t.circle(10, 330)
# t.circle(70, 30)

# 接口测试
# import requests
# from pprint import pprint
# res = requests.get("http://apis.juhe.cn/rubbish/category?key=fe737de31d642b4e9f66e13a989c0985")
#
# print(res.status_code)
# pprint(res.json(),width=30)


# import urllib.request
#
# url = "http://apis.juhe.cn/rubbish/category?key=fe737de31d642b4e9f66e13a989c0985"
# response = urllib.request.urlopen(url)
# the_page = response.read()
# print(the_page.decode("utf-8"))


# import MySQLdb
# import xlrd
#
# conn = MySQLdb.connect(
#     host='localhost',#IP地址
#     # port='3306',#端口号，如果是3306可以缺省端口号
#     user='root',#用户名
#     passwd='Tao123!',#密码
#     db='day59',#库名
#     charset='utf8'#指定编码格式
# )

# c = conn.cursor()#创建游，通过游标对象发送SQL语句

# 读取Excel文件
# import pandas as pd;
#
# def excel():
#
#     file_path = 'C:/Users/Administrator/Documents/student.xlsx'
#     sheetName = 'student'
#     file = pd.read_excel(file_path, sheet_name=sheetName)
#     dat = []  # 创建空list
#     for a in range(file.columns):  # 循环读取表格内容（每次读取一行数据）
#         data = []
#         data[0] = file.columns[0]
#         data[1] = file.columns[1]
#         dat.append(data)  # 把每次循环读取的数据插入到list
#     return dat
# a = excel()  # 返回整个函数的值
# print(a)

# def test(a):   #a变量传入
#     for b in a:  #循环读取a变量list
#         print(b)
# test(a)


# 读取数据，系统自动分析数据
# c.execute('select * from userinfo')#执行SQL语句，读取表中的所有数据
# rows = c.fetchall()#读取数据库的全部数据，但是不分行，以大元组显示
# print(rows)

# 插入数据
# for x in range(1000):
#     c.execute(f"INSERT INTO userinfo(name,pwd) VALUES('daisy{x+1}','tt56{x+1}') ")

# conn.commit()#对数据库的更改之后都得加commit方法

# for i in range(c.rowcount):#游标属性告诉你多少条记录
# row = c.fetchone()#返回执行SQL语句中数据中的第一行，执行一次返回一条信息
# row = c.fetchmany(3)#分组读取
# print(row)
# if row[1] == 'alex':
#     print('检查点=>>alex找到，测试通过')
#     break


# print("亲爱的xxx：\n","\t请点击链接激活用户：激活用户")


# name = "张三"
# gameName = input("请输入游戏名称:")
# cname = input("请输入游戏角色：")
# zhuangbei = input("请输入游戏装备：")
# buy = input("请输入购买装备：")
# coins = input("请输入付款金额：")
#
# print(
#     """
#     游戏：{}
#     角色：{}
#     拥有装备：{}
#     购买装备：{}
#     付款金额：{}
#     """.format(gameName,cname,zhuangbei,buy,coins)
# )
#
# print(name+"拥有了{}、{}装备，花了{}钱".format(zhuangbei,buy,coins))


# import random
# ran = random.randint(1,10)
# num = int(input("请输入你心中所想的数字："))
#
# if ran>num:
#     print("小了")

# n = 1
#
# while n<=100:
#     if n%3==0 and n%5==0:
#         print(n)
#     n+=1

# i=1
# sum_1=0
#
# while i<=20:
#     sum_1+=i
#     i+=1
#
# print(sum_1)


# ceng = 1
# while ceng<=5:
#     # print("*"*ceng)
#     count=1
#     while count<=ceng:
#         print("*",end="")
#         count+=1
#     ceng+=1
#     print()

# ceng = 1
# while ceng <= 9:
#     count = 1
#     while count <= ceng:
#         print("{}*{}={}".format(count,ceng,(count*ceng)),end=" ")
#         count += 1
#     ceng += 1
#     print()


# 一条包含字母 A-Z 的消息通过以下映射进行了编码 ：
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# 要解码已编码的消息，所有数字必须基于上述映射的方法，反向映射回字母（可能有多种方法）。例如，"11106" 可以映射为：
# "AAJF" ，将消息分组为 (1 1 10 6)
# "KJF" ，将消息分组为 (11 10 6)
# 注意，消息不能分组为  (1 11 06) ，因为 "06" 不能映射为 "F" ，这是由于 "6" 和 "06" 在映射中并不等价。
# 给你一个只含数字的 非空 字符串 s ，请计算并返回 解码 方法的 总数 。
# 题目数据保证答案肯定是一个 32 位 的整数。

# 示例 1：
# 输入：s = "12"
# 输出：2
# 解释：它可以解码为 "AB"（1 2）或者 "L"（12）。

# 示例 2：
# 输入：s = "226"
# 输出：3
# 解释：它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。

# 示例 3：
# 输入：s = "0"
# 输出：0
# 解释：没有字符映射到以 0 开头的数字。
# 含有 0 的有效映射是 'J' -> "10" 和 'T'-> "20" 。
# 由于没有字符，因此没有有效的方法对此进行解码，因为所有数字都需要映射。

# 示例 4：
# 输入：s = "06"
# 输出：0
# 解释："06" 不能映射到 "F" ，因为字符串含有前导 0（"6" 和 "06" 在映射中并不等价）。


# class Solution:
#     def numDecodings(self, s: str) -> int:
#         n = len(s)
#         f = [1] + [0] * n
#         for i in range(1, n + 1):
#             if s[i - 1] != '0':
#                 f[i] += f[i - 1]
#             if i > 1 and s[i - 2] != '0' and int(s[i-2:i]) <= 26:
#                 f[i] += f[i - 2]
#         return f[n]
#
#
# num = input("输入：")
# code = Solution().numDecodings(num)
# print(code)


# t = int(input("请输入温度："))
# if t > 30:
#     print("太热了！")
# else:
#     print("还行~")


# p = True
# q = False
# i = not (p and not q)
# print(i)


# sum = 0
# i = 1
# while i <= 50:
#     # print(i)
#     if i%2 == 0:
#         sum += i
#     i+=1
#
# print(sum)


# list列表添加往末尾添加  元组使用小括号-->s1 = (1,2,3,......)
# brands = ['hp','huawei','dell','mac']
#
# l = len(brands)
# i = 0
# while i<1:
#     if 'hp' in brands[i] or 'mac' in brands[i]:
#         del brands[i]
#         l-=1
#
#     i+=1
#
# print(brands)


# #集合
# #无序不重复特点：去重
# list1 = [3,5,3,4,5,6,7,8,9,0,1]
# #声明集合：set
# s1 = set() #创建空集合，只能使用set（）
#
# s2 = {1,3,7}  #字典：{key:value,key:value,....} 集合{元素1,元素2,.......}
#
# #应用：如果讲一个列表快速去重 set（）
# s3 = set(list1)
# print(s3)  # {0, 1, 3, 4, 5, 6, 7, 8, 9}
#
#
# #增删改查：
# #1.增加 s1 = set()
# #add() 添加一个元素
# s1.add('hello')
# s1.add('qqqq')
# s1.add('lucy')
# print(s1)
#
# #update() 可以添加多个元素
# t1 = ('林志玲','言承旭')
# s1.update(t1)
# print(s1)#{'言承旭', 'lucy', 'qqqq', '林志玲', 'hello'}
#
# s1.add(t1)
# print(s1) #{'言承旭', ('林志玲', '言承旭'), 'lucy', 'qqqq', '林志玲', 'hello'}
#
# #2.删除
# # remove如果元素存在则删除，不存在则报错
# s1.remove('言承旭')
# print(s1)#{('林志玲', '言承旭'), 'qqqq', 'lucy', '林志玲', 'hello'}
# # s1.remove('道明寺')
# # print(s1)#KeyError: '道明寺'
#
# # pop随机删除（一般删除第一个元素）
# s1.pop()
# print(s1)#{'hello', '林志玲', ('林志玲', '言承旭'), 'qqqq'}
# s1.pop()
# print(s1)#{'lucy', ('林志玲', '言承旭'), 'hello'}
#
# # s1.clear()#清空
#
# #dicard() 类似remove（） 在移除不存在的元素时不会报错
# s1.discard('道明寺')
# print(s1)


#
# def func(number):
#     a = 100
#
#     def inner_func():
#         nonlocal a
#         nonlocal number
#         number += 1
#         for i in range(number):
#             a += 1
#
#
#         print('修改后的a：',a)
#     return inner_func
#
# # 调用
# x = func(5)
# x()
#
# # 函数作为参数
# a = 50
# func(a)
# f1 = func(a) # a是一个实参
# f1()
#
# # 地址引用
# a = 10  # 声明整型变量
# b = a

# def test():  # 声明函数
#     print('-----test------')
#
# t = test
# # test()
# # t()
# # print(t,test)
#
# def func(f):
#     print(f)
#     f()
#     print('----------->func')
#
#
# #调用
# func(test)


# sum = 0
#
# for i in range(1,11,1):
#     sum += i
#     print(i)
# print(sum)

# list = []
# sum = 0
# for i in range(1,101):
#
#     if i % 5 == 0:
#         # print(i)
#         sum += i
#         list.append(sum)
#         # print(str(sum))
#
#
# print(list)

# print(sum)

'''
1.产生10个1~20的随机数，去除里面的重复项
2.键盘输入一个元素，将此元素从不重复的集合中删除
'''
import random
# #方法一：都不是10个随机数
# list1 = []
# for i in range(10):
#     ran = random.randint(1,20)
#     list1.append(ran)
# set1 = set(list1)
#
#
# print(list1)

# 方法二：
# set1 = set()
# for i in range(10):
#     ran = random.randint(1,20)
#     set1.add(ran)
# print(set1)
#
#
# num = int(input('请输入一个数字：'))
# set1.discard(num)
# print('删除之后的结果',set1)


# 创建一个list1的结果空列表，然后循环直到result的长度超过10退出循环，循环里面随机生成一个1-10之间的数，先查看生成的num随机数是否在result列表里，不在就添加进去
# import random
# list1 = []
#
# while len(list1) < 10:
#     num =random.randint(1,10)
#     if num not in list1:
#         list1.append(num)
# print(list1)


# 打印九九乘法表
# i = 1
# while i <= 9:
#     j = 1
#     while j <= i:
#         print('{}*{}={} '.format(j,i,(j*i)),end='')
#         j += 1
#     i += 1
#     print()

# while i <= 9:
#     j = 1
#     while j <= i:
#         print(i,"*",j,'=',i*j ,end='')
#         j += 1
#     i += 1
#     print()

# 其他：符号操作
# in 表示某个元素有没有在这个里面
# print(6 in set1)
#
# set2 = {2,34,5,67}
# set3 = {2,3,4,5,6}
#
# print(set2 == set3)#判断两个集合中的内容是否相等

# 测试：print（set2 != set3)??


# 不支持 （+ *） - & |
# set4 = set2+set3
# print(set4)

# set4=set3-set2 #差集  difference()
# print(set4)
# set5 = set3.difference(set2)
# print(set5)
#
# # &交集 intersection（）
# set6 = set3 & set2
# print(set6)

# | 并集 union() 联合

# '''
# 已知两个列表
# l1 = [5,1,2,9,3,6]
# l2 = [7,2,3,5,9]
# 找出两个列表的不同元素
# 找出两个列表的相同元素
# '''
# l1 = [5,1,2,9,3,6]
# l2 = [7,2,3,5,9]
#
# s1 = set(l1)
# s2 = set(l2)
#
# #对称差集
#
# result = (s1|s2)-(s1&s2)
# print(result)
#
# result = s1^s2 #两个列表中不一样的元素 亦或
#
# s3=s1.symmetric_difference(s2)
# s4 = s1.intersection(s2)
#
# print(s3,s4)

# 可变 和 不可变

# 不可变：对象所指向的内存中的值是不可以改变
# 不可变的类型：int  str float 元组tuple
# num = 10
#
# s1 = 'abc'
# print(id(s1))
# s1 = 'abcd'
# print(id(s1))
#
# t1 = (3,5,6)
# print(id(t1))
# t1 = (3,5)
# print(id(t1))

# 可变的：对象所指向的内存中的值是可以改变
# 可变类型：字典dict  列表list 集合
# list1 = [1,2,3,4,5]
# print(list1,id(list1))
# list1.pop()
# print(list1,id(list1))

# dict1 = {1:'aa',2:'bb'}
# print(dict1,id(dict1))
# dict1.pop(1)
# print(dict1,id(dict1))

# '''
# 集合是可变的
# '''
# set1 = {1, 2, 3, 4, 5}
# print(set1,id(set1))
# set1.pop()
# print(set1,id(set1))


# 类型转换
# str() int() list()-[]  dict()-{键值对}   set()-{元素}   tuple()-()
# str ---> int,list,set,tuple

# s='8'
# i=int(s)
#
# s='abc'
# l = list(s)
# print(l)
#
# s=set(s)
# print(s)
#
# t = tuple(s)
# print(t)

# 反向转换
# str <--- int,list,set,tuple,dict,float
# i = 8
# s = str(i)
# l = str(['a','b','c'])
# print(l,type(l))

# list ---> set(),tuple(),可以转成字典，列表必须符合[(key,value),(key,value),(....)]

# set ---> list,set ---> list,dict ---> list只是将key放在列表中
# tuple1 = (1, 2, 3, 4)
# print(list(tuple1))
# set1 = {1, 2, 3, 4}
# print(list(set1))
#
# dict1 = {1: 'a', 2: 'b'}
# print(list(dict1))#只是将key放在list中


# 函数
# 将重复的代码，封装到函数，只要直接找函数。可以增强代码的模块化和提高代码的重复利用率


# 定义函数
# 格式：
# def 函数名（[参数]）：
#     函数体（重复代码）
# 注意：1.必须使用关键字def 2.函数体注意缩进 3.函数名() 绑定

# 定义函数：完成随机数的产生
# 自动格式化：Ctrl+Alt+L

import random

# def generate_random():
#     for i in range(10):
#         ran = random.randint(1, 20)
#         print(ran)


# print(generate_random)  # 打印函数名

# 调用:函数名（） 找到函数并执行函数体的内容
# generate_random()

# 函数：带参数的
import time
from functools import reduce

'''
定义
def 函数名（参数，参数，....）:
    函数体
调用：
    pass
'''

# 求随机数的函数，产生的个数未知
# def generate_random(number,a,b):  #形参：形式上参数
#     for i in range(number):
#         ran = random.randint(a,b)
#         print(ran)
#
# print(generate_random)

# 调用
# generate_random(10,1,100)  #实参：实际上的参数 具体的值


# 求加法的函数

# def add(a, b):
#     result = a + b
#     print('和：', result)
#
#
# add(2,3)
# add(1,1)

'''
定义一个登陆函数，参数是username，password
函数体：
判断参数传过来的username，password是否正确，如果正确则登陆成功，否则打印登陆失败
'''

# 定义
# def login(username, password):
#     # 相当于数据库注册的用户名和密码
#     uname = 'admin123'
#     pwd = '112233'
#
# #   while True:
#     for i in range(3):
#         if username == uname and password == pwd:
#             print('登陆成功！')
#             break
#         else:
#             print('登陆失败！')
#             username = input('输入用户名：')
#             password = input('输入密码：')
#     else:
#         print('账户锁定')
#
#
# # 调用：
# username = input('输入用户名：')
# password = input('输入密码：')
#
# login(username, password)

'''
找出列表的最大值
自己封装一个求最大值的函数
'''

# def max(iterable):
#     max = iterable[0]
#     for i in iterable:
#         if i > max:
#             max = i
#     print('最大值是：',max)

# 调用：测试是否能找出最大值
# list1 = [1,4,2,4,5,6,9,0]
# max(list1)
#
# tuple1 = (2,35,2,5,6,3)
# max(tuple1)

# sort  min  reverse
#
# print(type(tuple1))#查看是什么类型
# #判断是不是什么类型：isinstance(变量，类型关键字)
# isinstance(2,int) #返回值是False True
# isinstance(tuple1,tuple)

# 复用

# def enumerate(value):
#     list1 = []
#     index = 0
#     for i in value:
#         t1 = (index,i)
#         list1.append(t1)
#
#         index += 1
#     print(list1)

# s = 'abc'
# s1 = s
# s = 'abcd'
# print(s1)

# 可变参数必须放在后面：name,*args
# 定义方式
# def add(*args):
#     # print(args)# 空元组
#     sum = 0
#     if len(args)>0:
#         for i in args:
#             sum += i
#         print('元素和为',sum)
#     else:
#         print('没有元素可计算',sum)
# add()   里面的参数也可以加*
#
# add(1,2,3)


'''
xxx计算出来的累加和是xxx
'''
# def add(name,*args):#预先准备一个元组
#     sum = 0
#     if len(args)>0:
#         for i in args:
#             sum += i
#         print('%s元素和为%s'%(name,sum))
#     else:
#         print('没有元素可计算',sum)
# #调用
# add('霏霏',1,2,3,4)


# 可变参数+关键字参数
# 关键字参数：key=value

# def add(a,b=10,c=8):  #关键字参数 此时的b就是默认值
#     result = a+b
#     print(result)
# #调用
# add(1, 9)  #a=1,b=9 此时的9或覆盖b原来的默认值
# add(2, c=6)#如果想将6赋值给c,则需要结合关键字的key使用

# 使用函数的时候：
# def aa(**kwargs):装包
#     print(kwargs)
# 如果在开发的时候，已知一个字典
# dict1 =  {'001':'python','002':'java','003':'c++','004':'es6'}   拆包
# aa(**dict1)

# 函数：计算每位同学年龄
# students={'001':('蔡徐坤',20),'002':('王源',19),'003':('王俊凯',18),'004':('朱一龙',27)}
#
#
# def print_boy(name,**persons):  # persons=students
#     print('{}喜欢的小鲜肉是：'.format(name))
#     if isinstance(persons,dict):
#         values = persons.values()
#         for name,age in values:
#             print('{}的年龄是：{}'.format(name,age))
#
# #调用
# print_boy('弟弟',**students)


# def func(**kwargs): #key word argumernt，预先准备一个字典
#     print(kwargs)
#
# #调用
# # func(a=1,b=2,c=3)#关键字参数
#
# dict1 = {'001':'python','002':'java','003':'c++','004':'es6'}
# func(**dict1) #**只能用在字典前，将字典进行拆包，将字典拆包成关键字参数的形式001=Python
'''
步骤：
1.将字典进行拆包
   func（。。。。。）
2.func里面的参数都是关键字参数
3.将关键字参数再进行一次装包动作
4.装包成功：kwargs
  就是装包成功的字典
'''

# def bb(a,b,*c,**d):
#     print(a,b,c,d)
#
# bb(1,2) #1 2 () {}
#
# bb(1,2,3,4)# 1 2 (3,4) {}
#
# bb(1,2,x=100,y=200) # 1 2 （） {'x':100,'y':200}


# def func1(name,*args):
#     if len(args) > 0:
#         for i in args:
#             print('{}学习了{}'.format(name,i))
#     else:
#         print('没有学习任何编程语言！')
#
# courses = ['html','mysql','python']
#
# #调用函数
# func1('坤坤',*courses) #拆包

'''
无参函数：
def func():
     pass
func()


有参数函数：
1.普通参数
def func(name,age):
     pass
func('aa',8)  形参与实参的个数要一致


2.可变参数
A.def func(*args):
     pass
func() 函数调用时，实参的个数可以没有，也可以多个  *不能是关键字参数


B.def func(**kwargs):
     pass
func(a=1,b=2) 函数调用时，实参的个数可以没有，也可以多个  **必须是关键字参数


C.def func(*args,**kwargs):
     pass
list1 = [1,3]
dict1 = {'1':'a','2':'b'}
func(*list1,**dict1) 拆包

D.混用
def func(name,*args,**kwargs):
     pass
func('tom')  必须赋值

3.默认值+关键字
def func(name,age=18):
     pass
func('tom') tom 18

func('tom',age=20)
'''

# 返回值：将函数中运算的结果通过 return 关键字“扔”出来
# def add(a,b):
#     result = a + b
#     print(result) #仅仅限于打印在终端上，辅助查看，但是外部是无法使用的
#     return 'aaa'
#
# x = add(2,8)
# print(x)

'''
return返回值
1.return后面可以是一个参数   接收的时候x=add(1,2)

2.return后面也可以是多个参数，如果是多个参数则底层会将多个参数先放在一个元组中，将元组作为整体返回 x=add(1,2)   x----(1,2,3)
3.接收的时候也可以是多个：return 'hello','world' x,y=('hello','world')  -------x='hello' y='world'
'''

'''
加入购物车
判断用户是否登录，如果登录，成功加入购物车，否则提示请登录之后添加

成功True  不成功 False

def add_shoppingcart(goodsName):
    pass
    
def login(username,password):
    pass
    
调用
'''

# islogin = False #用于判断用户是否登录的变量 默认是没有登录的
#
# def add_shoppingcart(goodsName):
#     if islogin and goodsName:
#         #登录的
#         print('成功将{}加入到购物车中！'.format(goodsName))
#     else:
#         #没有登录
#         print('用户未登录或者没有添加任何商品！')
#
#
# def login(username, password):
#     if username=='lijiaqi' and password=='123456':
#         #登录成功
#         print('登录成功')
#         return True
#     else:
#         print('用户名或者密码有误')
#         return False
#
#
# #调用函数：添加商品到购物车中
# username = input('输入你的用户名：')
# password = input('输入你的密码：')
#
# islogin = login(username,password)
#
# add_shoppingcart('完美日记红丝绒')


# islogin = False #用于判断用户是否登录的变量 默认是没有登录的
#
# def add_shoppingcart(goodsName):
#     global islogin
#
#     if islogin:
#         if goodsName:
#           # 登录的
#           print('成功将{}加入到购物车中！'.format(goodsName))
#         else:
#           print('没有选中任何商品！')
#     else:
#         #没有登录
#         answer = input('用户没有登录！是否登录用户（yes/no）')
#         if answer == 'yes':
#             username = input('输入你的用户名：')
#             password = input('输入你的密码：')
#
#             #调用login
#             islogin = login(username,password) #在一个函数中可以调用另一个函数
#             # print('islogin',islogin)
#             print('成功将{}加入到购物车中！'.format(goodsName))
#         else:
#             print('不能添加任何商品！')
#
#
#
# def login(username, password):
#     if username=='lijiaqi' and password=='123456':
#         #登录成功
#         # print('登录成功')
#         return True
#     else:
#         # print('用户名或者密码有误')
#         return False
#
#
# #调用函数：添加商品到购物车中
# username = input('输入你的用户名：')
# password = input('输入你的密码：')
#
# islogin = login(username,password)
#
# add_shoppingcart('完美日记红丝绒')


'''
用户登录
输入用户名
输入密码
输入验证码 --->封装成一个函数
'''

# 定义生成验证码的函数
# def generate_checkcode(n):
#     s = '0987654321qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
#     code = ''
#     for i in range(n):
#         ran = random.randint(0,len(s)-1)
#         code += s[ran]
#     return code
#
# #定义登录函数
# def login():
#     username = input('输入用户名:')
#     password = input('输入密码:')
#
#     # 得到一个验证码
#     code = generate_checkcode(5) # 函数之间的调用
#     print('验证码是：',code)
#     code1 = input('输入验证码:')
#     # 验证
#     if code.lower()==code1.lower():
#         #验证码输入正确
#         if username=='lijiaqi' and password=='123456':
#             print('用户登录成功！')
#         else:
#             print('用户名或者密码有误！')
#     else:
#         print('验证码输入有误！')
#
# # 调用函数

# login()


# global 变量的范围
# 局部变量 全局变量
# 全局变量如果是不可变在函数中进行修改需要添加global关键字，如果全局变量是可变的，在函数中修改时就不需要添加global
# 声明在函数外层是全局的，所有函数都可以访问


# name = '费费'
#
#
# def func():
#     s = 'abcd'
#     s += 'X'  # 局部变量 函数内部声明的变量，局部变量仅限于在函数内部使用
#
#     print(s, name)
#
#
# def fun1():
#     global name # 不修改全局变量，只是获取打印，但是如果发生修改全局变量，则需要在函数内部声明： global+变量名
#     print(name)  #报错：函数内部变量可以随便修改赋值，但是全局变量不能随便在函数体中进行修改
#     name += '12345'
#     print(name)
#
# # print（s）报错
#
# def func2():
#     name = '月月' # 局部变量与全局变量同名
#     name +='弹吉他的小美女'
#     print('func2修改后的name是：',name)
#
# # func2()
# fun1()
# func()

# name = '月月'
#
# list1 = [1, 2, 4, 6]
#
#
# def func():
#     name = '蕊蕊'
#     print(name)
#
#
# def func1():
#     global name
#     print(name)
#     name += '真好看！'
#
#     # 修改列表
#     list1.append(8)
#     print(list1)
#
#
# func1()


# 内部函数
'''
特点：
1.可以访问外部函数的变量
2.内部函数可以修改外部函数的可变类型的变量比如：list1
3.内部函数修改全局的不可变的变量时，需要在内部函数声明global+变量名
  内部函数修改外部函数的不可变变量时，需要再内部函数声明nonlocal+变量名
4.locals（）查看本地变量有哪些，以字典的形式输出
  globals（）查看全局变量有哪些，以字典的形式输出
'''
# def func():
#     # 声明变量
#     n = 100  # 局部变量
#
#     list1 = [8, 2, 6, 4]  # 局部变量
#
#     # 声明内部函数
#     def inner_func():
#         nonlocal n
#         # 对list1里面的元素进行加5操作
#         for index, i in enumerate(list1):
#             # 0 3
#             list1[index] = i + n
#
#         list1.sort()
#         # 修改n变量
#         n += 101
#
#     inner_func()
#
#     print(list1,n)
#
# # 调用func
# func()


# a = 100 # 全局变量
# print(globals())
#
# def func():
#     b = 99
#     def inner_func():
#         global a
#         nonlocal b
#         c = 88
#         # 尝试修改
#         c += 12
#         b += 1
#         a += 0
#         # 尝试打印
#         print(a,b,c)
#     inner_func()
#     # 使用locals（）内置函数进行查看，可看到在当前函数中声明的内容有哪些
#     # locals（）是一个字典，key：value
#     print(locals())
#
#
# # 调用
# func()


# 闭包
# 在函数中提出的概念
'''
条件：
1.外部函数中定义了内部函数
2.外部函数是有返回值
3.返回值是：内部函数名
4.内部函数引用了外部函数的变量

格式：
def 外部函数（）：
    ....
    def 内部函数（）：
       ....
    return 内部函数
    
'''

# def func():
#     a = 100
#
#
#     def inner_func():
#         b = 99
#         print(a,b)
#
#     return inner_func
#
# # func()
#
# # print(a)
# # inner_func()
#
# x = func()
#
# print(x)
#
# x()


# 闭包

# def func(a,b):
#     c = 10
#
#     def inner_func():
#         s = a+b+c
#         print('相加之后的结果是：',s)
#
#     return inner_func
#
#
# i_func = func(4,6)  # i_func就是inner_func  i_func = inner_func
#
# #调用返出来的内部函数
# i_func()


# 闭包的应用
# 闭包
'''
1.保存返回闭包时的状态（外层函数变量）
闭包缺点：
1.作用域没有那么直观
2.因为变量不会被垃圾回收所以有一定的内存占用问题

闭包作用：
1.可以使用同级的作用域
2.读取其他元素的内部变量
3.延长作用域


闭包总结：
1.闭包看似优化了变量，原来需要类对象完成的工作，闭包也可完成
2.由于闭包引用了外部函数的局部变量，则外部函数的局部变量没有及时释放，消耗内存
3.闭包的好处，使代码变得简洁，便于阅读代码
4.闭包是理解装饰器的基础
'''

# def func(a,b):
#     c = 10
#
#     def inner_func():
#         s = a+b+c
#         print('相加之后的结果是：',s)
#
#     return inner_func
#
#
# i_func = func(4,6)  # i_func就是inner_func  i_func = inner_func
# i_func1 = func(2,9)
# #调用返出来的内部函数
# i_func()
# i_func1()


# def func():
#     a = 100
#
#     def inner_func1():
#         b = 90
#
#         s = a + b
#         print(s)
#
#     def inner_func2():
#         inner_func1()
#         print('--------->inner_func2',a)
#         return 'hello'
#
#     return inner_func2
#
#
# #调用func
# f = func()
#
# print(f)
#
# f()
# ff = f()
#
# print(ff)


# 计数器

# def generate_count():
#     container = [0]
#
#     def add_one():
#         container[0] = container[0] + 1
#         print('当前是第{}次访问'.format(container[0]))
#
#     return add_one
#
#
# # 内部函数就是一个计数器
# counter = generate_count()
#
# counter()  # 第一次的访问
# counter()  # 第二次的访问
# counter()  # 第三次的访问


# 装饰器
''''
 加入购物车，付款，修改收货地址......
 判断用户的登录状态
 
 
特点：
1.函数A是作为参数出现的（函数B就接收函数A作为参数）
2.要有闭包的特点

'''

# 定义一个装饰器
# def decorate(func):
#     a = 100
#     print('wrapper外层打印测试')
#
#     def wrapper():
#         func()
#         print('------->硬装')
#         # func()
#         print('-------->软装',a)
#
#     print('wrapper加载完成....')
#     return wrapper
#
# # 使用装饰器
# @decorate
# def house():
#     print("我是毛坯房。。。。")

'''
1.house被装饰函数
2.将被装饰函数作为参数传给装饰器decorate
3.执行decorate函数
4.将返回值又赋值给house

'''

# 调用函数house
# house()

import random

# 登录校验
# def decorate(func):
#     def wrapper(*args,**kwargs): # 元组（） {'clazz':'1904'}
#         print('正在校验中....')
#         time.sleep(2)
#         print('校验完毕！')
#         # 调用原函数 args----->()
#         func(*args,**kwargs) # f1 f2 f3
#
#     return wrapper
#
#
#
# @decorate
# def f1(n):
#     print('-----f1-------',n)
# f1(5) # 此时的f1是wrapper,
#
# @decorate
# def f2(name,age):
#     print('------f2-------',name,age)
# f2('lili',20)
#
# @decorate
# def f3(students,clazz = '1905'):
#     print('{}班级的学生如下：'.format(clazz))
#     for stu in students:
#         print(stu)
# students = ['22s','ddff','ffdd']
# f3(students,clazz='1904')
#
#
# @decorate
# def f4():
#     print('-------f4----------')
#
# f4()


# 装饰器
# def zhuang1(func):
#     print('----->1 start')
#
#     def wrapper(*args,**kwargs):
#         func()
#         print('刷漆')
#     print('------>1 end')
#
#
#     return wrapper
#
#
# def zhuang2(func):
#     print('----->2 start')
#
#     def wrapper(*args,**kwargs):
#         func()
#         print('吊顶')
#     print('------>2 end')
#
#
#     return wrapper
#
#
# @zhuang2
# @zhuang1
# def house():
#     print('我是毛坯房....')
#
# house()


# 装饰器带参数
'''
带参数的装饰器是三层的
最外层的函数负责接收装饰器参数
里面的内容还是原装饰器内容

'''

# def outer(a):  # 第一层：负责接收装饰器的参数
#     def decorate(func): # 第二层：负责接收函数的
#         def wrapper(*args, **kwargs):  # 第三层：负责接收函数的参数
#             func(*args)
#             print('---->铺地砖{}块..'.format(a))
#
#         return wrapper  # 返出：第三层函数名
#
#     return decorate  #返出来：第二层
#
#
# @outer(a=10)
# def house(time):
#     print('我是{}日期拿到了房钥匙，是毛坯房....'.format(time))
#
# @outer(100)
# def street():
#     print('新修的街道名字是：黑泉路')
#
#
#
# house('2020-1-22')
# street()


# 开发：登录验证


# islogin = False  # 默认是没有登录
#
#
# # 定义一个登录函数
# def login():
#     username = input('输入用户名：')
#     password = input('输入密码：')
#     if username == 'admin' and password == '123456':
#         return True
#     else:
#         return False
#
#
# # 定义一个装饰器，进行登录验证
#
# def login_required(func):
#     def wrapper(*args, **kwargs):
#         global islogin
#         print('------付款-------')
#         # 验证用户有没有登录
#
#         if islogin:
#             func(*args, **kwargs)
#         else:
#             # 跳转到登录页面
#             print('用户没有登录，不能付款！')
#             islogin = login()
#             print('result:', islogin)
#
#     return wrapper
#
#
# @login_required
# def pay(money):
#     print('正在付款，付款金额是{}元'.format(money))
#     print('付款中...')
#     time.sleep(2)
#     print('付款完成！')
#
# #调用
# pay(100000)
#
#
# pay(8000)

'''
函数：
作用域：LEGB
L：local 本地的
E：encloseing 嵌套
G：global 全局
B：built-in 内置的

嵌套函数：

闭包：
1.内层函数
2.内层函数引用外层函数的变量
3.返回内层函数


装饰器：
1.内层函数
2.内层函数引用外层函数的变量
3.返回内层函数
4.函数作为外层函数参数

使用装饰器：
@装饰器名
'''

# 匿名函数:简化函数定义
# 格式：lambda 参数1，参数2..:运算

# def func():
#     print('aaa')
#
# def add(a,b):
#     s = a + b
#     return s


# s = lambda a, b: a + b
# print(s) # s 就是函数function
#
# result = s(1,2)
# print(result)
#
# s1 = lambda x,y:x*y
#
# result=s1(3,5)
# print(result)

# 匿名函数作为参数

# def func(x,y,func):
#     print(x,y)
#     print(func)
#     func(x,y)
#     s = func(x,y)
#     print(s)
#
# # 调用func
# func(1,2,lambda a,b:a+b)


# 匿名函数与内置函数的结合使用：
# max  sorted  zip....

# list1 = [3,5,3,7,8,9,1]
# m = max(list1)
#
# print('列表的最大值：',m)
#
# list2 =[{'a':10,'b':20},{'a':6,'b':54},{'a':3,'b':27},{'a':78,'b':35}]
#
# m = max(list2,key=lambda x:x['b'])
# print('列表的最大值：',m)


# map 对列表里面的元素进行某些操作

# list1 = [3,4,5,6,7,8,9,2,1]
#
# result = map(lambda x : x + 2, list1)
# print(list(result))
#
# func = lambda x : x if x % 2 == 0 else x + 1
#
# result = func(5)
# print(result)

# 对列表中的奇数进行加1操作
# result = map(lambda x : x if x % 2 == 0 else x + 1,list1)
# print(list(result))

# for index,i in enumerate(list1):
#     if i%2!=0:
#         list1[index]=i+1
#
#
# print(list1)


# reduce（）：对列表（可迭代的）的元素进行加减乘除运算的函数

# tuple1 = (2,3,4,5,6)
#
# result = reduce(lambda x,y:x+y,tuple1)
# print(result)
#
# tuple2 = (2,)
#
# result = reduce(lambda x,y:x+y,tuple2,10)
# print(result)


# filter
# list1 = [12,45,2,6,7,88,6]
# result = filter(lambda x:x<10 ,list1)
# print(list(result))
#
#
# list2 = []
# def func(list1):
#     for i in list1:
#         if i < 10:
#             list2.append(i)
#     print(list2)
#
# func(list1)


# students = [
#     {'name':'tom','age':20},
#     {'name':'lucy','age':22},
#     {'name':'lily','age':19},
#     {'name':'mark','age':23},
#     {'name':'jack','age':17},
#     {'name':'steven','age':18},
# ]

# 找出所以年龄大于20的学生

# result = filter(lambda x:x['age']>20,students)
# print(list(result))


# 按照年龄从小到大排序

# students = sorted(students,key=lambda x:x['age'])
# print(students)


'''
max()
min()
sorted()


map()
reduce()
filter()

'''

# 递归函数：函数自己调用自己
'''
普通函数：def func():pass
匿名函数：lambda 参数：返回结果
递归函数：普通函数的一种表现形式

特点：
1.递归函数必须要设定终点
2.通常都会有一个入口
'''

# def sum(n):# 1~n
#     if n == 0:
#         return 0
#     else:
#        return n + sum(n-1)
#
# result = sum(100)
# print(result)
#


# def sum1(n):
#     '''
#     求和函数
#     :param n: 从1~n累加和
#     :return:求和的结果
#     '''
#     if n == 100:
#         return 100
#     else:
#        return n + sum1(n+1)
#
# result = sum1(0)
# print(result)


#
# s = 0
# for i in range(11):
#     s += i
# print(s)
#
#
# def f1(n):
#     if n>0:
#         print('---->',n)
#         f1(n-1)
#     else:
#         print('---->',n)
#
# f1(10)


'''
总结函数：
普通函数：
  def 函数名([参数,...]):
      函数体
      
      
  1.如何定义函数
  2.调用函数
  
  
  参数：
  1.无参数：
  def func():
     pass
     
   func()
   
  2.有参数：
    一般参数：
    
    def func(a,b):
      pass
      
    func(1,2)
    
    可变参数：
    
    def func(*args,**kwargs): args单个元素   kwargs关键字参数
      pass
      
    func()
    
    func(1)
    
    func(a=10)
    
    默认值：
    def func(a=10,b=10)
       pass
       
    func()
    
    func(100)
    
    关键字参数：
    
    func(b=99)
    
  返回值：return
  
  没有返回值 
  
  def func()
       print('......')
       
    x = func() ------>x=None
    
    有返回值：
      def func()
       return ’a‘,'b'
       
    x = func() ------>x=(’a‘,'b')
    
  嵌套函数 ----> 闭包 ----> 装饰器
    
    def func():
       def wrapper():
           ....
           
        return wrapper
        
    变量的作用域：LEGB
    global nolocal
    globals() locals()
    
    LEGB
    L：local 本地的
    E：encloseing 嵌套
    G：global 全局
    B：built-in 内置的
    
    装饰器：
    
    单层装饰器
    
    def decorate(func):
        def wrapper(*args,**kwargs):
         ....
         
        return warpper
        
    @decorate
    def house():
        pass
      
    @decorate
    def f1(a,b):
        pass
        
    多层装饰器：
    
    @zhuang1
    @zhuang2
    def fi(a,b):
        pass
          
'''

# 文件操作：
'''
文件上传：
保存log

系统函数
open(file,mode,buffering,encodeing)

读：
open(path/filename,'rt')---->返回值：steam（管道）

container = stream.read() ------>读取管道中内容

注意：如果传递的文件有误，则会报错
如果是图片则不能使用默认的读取方式，mode = 'rb'

总结：
read（）读取所有内容
readline（）每次读取一行内容
readlines（）读取所有的行保存到列表中
readable（）判断是否可读

mode:（r--read读 w--write写）------纯文本文件
     【rb---read binary（二进制） wb--write binary】-----纯文本、图片、音乐、视频
     
文件上传：

文件下载：

'''

# stream = open(r'D:\aa.txt')

# container = stream.read()
# print(container)

# result = stream.readable()  #判断是否可以读取 true false
# print(result)

# while True:
#     line = stream.readline()
#     print(line)
#     if not line:
#         break


# lines = stream.readlines() # 保存到列表中
# print(lines)
# for i in lines:
#     print(i)
#

# 写文件
'''
stream = open(r'D:\aa.txt','w')
mode是'w'表示就是写操作  每次都会将原来的内容清空

方法：
   write（内容） 每次都会将原来的内容清空，然后写当前的内容
   writelines(Iterable) 没有换行的效果
   stream.writelines(['高进\n','赌圣\n','小刀\n']) ------>自己加
   
如果 mode=‘a’----> append追加 每次都不会将原来的内容清空

'''
stream = open(r'D:\aa.txt', 'w')

# stream.writable() #判断文件是否可写

# s='''
# 你好！
#     欢迎来到开心刮刮乐，来啊来啊~
#                 工作人员：哦哦
# '''
# result = stream.write('hello')
# # print(result)
#
# stream.write('龙五')
#
# stream.writelines(['高进\n','赌圣\n','小刀\n'])
#
# stream.close() #释放资源


# 文件复制
'''
原文件：D:\壁纸\tim.jpg
目标文件：D:\tim.jpg

D:\learn\test1
D:\learn\test2

with 结合open使用，可以帮助我们自动释放资源
'''

# stream = open(r'D:\壁纸\tim.jpg','rb')
# with open(r'D:\壁纸\tim.jpg','rb') as rstream:
#     container = rstream.read() # 读取文件内容
#
#
# with open(r'D:\tim.jpg','wb') as wstream:
#     wstream.write(container)
#
# print('文件复制完成！')

# stream.close()

# 模块：os.py
# import os

# tim.jpg保存到当前文件夹所在的目录
# with open(r'D:\壁纸\tim.jpg','rb') as rstream:
#     container = rstream.read() # 读取文件内容
#     file = stream.name
#     filename = file[file.rfind('\\')+1:] # 截取文件名
#
# path = os.path.dirname(__file__)
# result = os.path.join(path,filename)
# # print(result)
#
# with open(result,'wb') as wstream:
#     wstream.write(container)


# os 模块

import os

# os.path里的函数


# absolute 绝对的 D:\壁纸\tim.jpg
# 相对路径：../../xxx/xxx
# 获取路径：directory 目录 文件夹
# 当前文件所在的文件夹路径

# path = os.path.dirname(__file__)

# 通过相对路径得到绝对路径
# s = os.path.abspath('aa.txt')

# 获取当前文件的绝对路径
# path = os.path.abspath(__file__)

# 获取当前文件夹的路径
# path = os.getcwd()

# r = os.path.isabs('D:\壁纸\tim.jpg')

# print(path)


# 得到文件名
# filename = path[path.rfind('\\')+1:]
# r = r'D:\壁纸\tim.jpg'
#
# result = os.path.split(r)
#
# print(result)
# print(result[1])

# 分割文件与扩展名
# result = os.path.splitext(r)
# print(result)

# 获取文件大小，单位是字节
# size = os.path.getsize(r)
# print(size)
#
# result = os.path.join(os.getcwd(),'file','a','al.jpg')

'''
os.path:常用函数
dirname() 获取指定文件目录
join() 拼接获取新的路径
split() 分割（文件目录，文件名）
splittext() 分割（文件目录\文件名，文件的扩展名）
getsize() 获取文件大小

isabs() 判断是否是绝对路径
isfile() 判断是否是文件
isdir() 判断是否是文件夹

'''

# os中的函数：

# dir = os.getcwd()
# print(dir)

# 返回指定目录下的所有的文件和文件夹，保存到列表中
# all = os.listdir(r'D:\壁纸')
# print(all)

# 创建文件夹
# if not os.path.exists(r'D:\壁纸\testimg'):
#     f = os.mkdir(r'D:\壁纸\testimg')
#     print(f)

# 删除文件夹,只能移除空文件夹
# f = os.rmdir(r'D:\壁纸\testimg')
# print(f)


# f = os.removedirs(r'D:\壁纸\testimg')
# print(f)


# 删除文件
# os.remove(r'D:\壁纸\testimg\aa.txt')

# 删除p4文件夹

# path = r'D:\壁纸\testimg\p4'
#
# filelist = os.listdir(path)
#
# for file in filelist:
#     path1 = os.path.join(path,file)
#     os.remove(path1)
# else:
#     os.rmdir(path)
#
# print('删除成功！')

# 切换目录
# os.chdir()


'''
os模块方法：
os.getcwd() 获取当前目录
os.listdir() 浏览文件夹
os.mkdir() 创建文件夹
os.rmdir() 删除空的文件夹
os.remove() 删除文件
os.chdir() 切换目录
'''

# 文件复制
# src_path = r'D:\壁纸\testimg\p4'
# target_path = r'D:\壁纸\testimg\p3'


# # 封装成函数
# def copy(src, target):
#     if os.path.isdir(src) and os.path.isdir(target):  # 判断是否为文件夹
#         filelist = os.listdir(src)  # 列出要复制的文件夹中所有文件列表
#
#         for file in filelist:  # 遍历文件列表
#
#             path = os.path.join(src, file)  # 拼接完整路径
#             with open(path, 'rb') as rstream:  # 建立一个通道缓存
#                 container = rstream.read()  # 读取文件内容，把文件内容放进去
#
#                 path1 = os.path.join(target, file)  # 拼接目标文件夹中文件的完整路径
#                 with open(path1, 'wb') as wstream:  # 建立一个通道
#                     wstream.write(container)  # 写入需要复制的文件内容
#         else:
#             print('复制完毕')
#
#
# # 调用函数
# copy(src_path, target_path)


# 文件夹包文件夹复制
# src_path = r'D:\壁纸\testimg\p4'
# target_path = r'D:\壁纸\testimg\p2'
#
# # 封装成递归函数
# def copy(src_path,target_path):
#     filelist = os.listdir(src_path) # 获取文件夹内容
#     for file in filelist:  # 遍历文件列表
#         path = os.path.join(src_path, file)  # 拼接完整路径
#         if os.path.isdir(path): # 判断是否是文件夹
#            target_path1 = os.path.join(target_path,file)
#            os.mkdir(target_path1)
#            copy(path,target_path1) # 递归调用
#         else: # 不是文件夹直接进行复制
#             with open(path, 'rb') as rstream:  # 建立一个通道缓存
#                 container = rstream.read()  # 读取文件内容，把文件内容放进去
#                 path1 = os.path.join(target_path, file)  # 拼接目标文件夹中文件的完整路径
#                 with open(path1, 'wb') as wstream:  # 建立一个通道
#                     wstream.write(container)  # 写入需要复制的文件内容
#     else:
#         print('复制完成！')
#
# copy(src_path,target_path)


# 图书管理系统   D:\壁纸\testimg\p2\p1
# 持久化保存：文件
# 非持久化：list 元组 字典----->内存
# 用户注册

# def register():
#     username = input('输入用户名：')
#     password = input('输入密码：')
#     repassword = input('再次输入密码：')
#
#     if password == repassword:
#         # 保存信息
#         with open(r'D:\壁纸\testimg\p2\p1\users.txt','a') as wstream:
#             wstream.write('{} {}\n'.format(username,password))
#
#         print('用户注册成功！')
#
#     else:
#         print('密码不一致！')
#
#
# # 用户登录
# def login():
#     username = input('输入用户名：')
#     password = input('输入密码：')
#
#     if username and password:
#         with open(r'D:\壁纸\testimg\p2\p1\users.txt','r') as rstream:
#             while True:
#                 user = rstream.readline() # feifei 123456\n
#
#                 if not user:
#                     print('用户名或者密码输入有误！')
#                     break
#
#                 input_user = '{} {}\n'.format(username,password)
#                 # 如果用户输入的根文件中的内容一致则认为用户登录成功
#                 if user == input_user:
#                     print('用户登录成功！')
#                     break
#
#
# def show_books():
#     print('图书馆里面的书名：')
#     with open(r'D:\壁纸\testimg\p2\p1\books.txt','r',encoding='utf-8') as rstream:
#         books = rstream.readlines()
#         for book in books:
#             print(book,end='') # 因为读取的内容中有\n 所以取消print中自带的末尾换行

# 调用函数
# register()
# login()
# show_books()


# 语法错误与异常

# 语法错误：
# while True
#     print('----')

# number = 100
# def func():
#     number += 1


# 异常：程序运行时报出来的，xxxError
# def chu(a,b):
#     return a/b
#
#
# x = chu(1,0) # ZeroDivisionError: division by zero
# print('------------->',x)


# 异常处理：
'''
try:
    可能出现异常的代码
except：
    如果有异常执行的代码
[finally：
    无论是否存在异常都会被执行的代码]

   

    
情况1：
try:
   有可能产生多种异常
except 异常的类型1：
   print（。。。。。）
except 异常的类型2：
   print（。。。。。）
except 异常的类型3：
   print（。。。。。）
except Exception：
   pass
如果是多个except，异常类型的顺序需要注意，Exception需要放在最下面


情况2：获取Exception错误原因
try:
   有可能产生多种异常
except 异常的类型1：
   print（。。。。。）
except Exception as err：
   print(err)------>err的内容就是错误原因
   
情况3：
try:
    可能出现异常的代码
except：
    如果有异常执行的代码
[finally：
    无论是否存在异常都会被执行的代码]
else:
   如果try中没有异常则进入的代码
   
注意：如果使用else则在try代码中不能出现return

情况4：
# 文件操作  stream.close()
# 数据库操作  close()
try:
    pass
except：
    pass
finally：
    pass---->释放资源
    


'''
# def func():
#     try:
#         n1 = int(input('输入第一个数字：'))
#         n2 = int(input('输入第二个数字：'))
#
#         per = input('输入运算符号（+ - * /）：')
#
#         if per == '+':
#             result = n1+n2
#         elif per == '-':
#             result = n1-n2
#
#         elif per == '*':
#             result = n1*n2
#
#         elif per == '/':
#             result = n1/n2
#         else:
#             print('符号输入有误！')
#
#
#         print('结果是：',result)
#
#
#         # 操作列表
#         list1 = []
#         list1.pop()
#
#         # 文件操作
#         # with open(r'D:\壁纸\testimg\p2\p1\books.txt','w') as wstream:
#         #     wstream.write('本次的运算结果是：{}'.format(result))
#         with open(r'D:\壁纸\testimg\p2\p1\books.txt', 'r') as rstream: # FileNotFoundError
#             print(rstream.read())
#
#     except ZeroDivisionError:
#         print('除数不能为零！')
#     except ValueError:
#         print('必须输入数字！！！')
#     except Exception as err:
#         print('出错啦！！',err)
#
# func()
# print('--------->')


# else不能出现return
# def func():
#     try:
#         n1 = int(input('输入数字：'))
#         print(n1)
#         return 1
#     except ValueError:
#         print('必须是数字....')
#         return 2
#     else:
#         print('数字输入完毕！') #没有异常才会执行的代码快
#
# func()


# 文件释放资源
# def func():
#     stream=None
#     try:
#         stream = open(r'D:\壁纸\testimg\p2\p1\books.txt',encoding='utf_8')
#         contanier = stream.read()
#         print(contanier)
#         return 1
#     except Exception as err:
#         print(err)
#         return 2
#     finally:
#         print('------->')
#         if stream:
#             stream.close()
#         return 3
# x = func()
# print(x)


# 抛出异常 raise

# 注册用户名必须6位

# def register():
#     username = input('输入用户名：')
#     if len(username)<6:
#         raise Exception('用户名长度必须6位以上')
#     else:
#         print('输入用户名是：',username)
#
# try:
#     register()
# except Exception as err:
#     print(err)
#     print('注册失败！')
# else:
#     print('注册成功！')


# 列表推导式 字典推导式 集合推导式
# 旧的列表 ---> 新的列表

# 1.列表推导式： 格式：[表达式 for 变量 in 旧列表] 或者 [表达式 for 变量 in 旧列表 if 条件]


# 过滤掉长度小于等于3的人名，得到的列表首字母大写 有条件
# names = ['tom', 'lily', 'abc', 'jack', 'steven', 'bob', 'ha']
#
# result = [name.capitalize() for name in names if len(name) > 3]
#
# print(result)

'''
def func(names):
    newlist = []
    for name in names:
        if len(name)>3:
           name = name.title()
           newlist.append(name)
        return newlist
'''

# 将1到100之间能被3整除，组成一个新的列表

# newlist = [i for i in range(1,101) if i % 3 == 0 and i % 5 == 0]
# print(newlist)

# 0~5的偶数 0~10的奇数
# [(偶数,奇数),(),(),()]  [(0,1),(0,3),(0,5),(0,7),(0,9),(2,1),(2,3)]

# newlist = [(x, y) for x in range(5) if x % 2 == 0 for y in range(10) if y % 2 != 0]
# print(newlist)
'''
def func():
    newlist = []
    for i in range(5):
        if i%2==0:
            for j in range(10):
                if j %2!=0:
                    newlist.append((i,j))
    print(newlist)

func()
'''

#list1 = [[1,2,3],[4,5,6],[7,8,9],[1,3,5]] ---> [3,6,9,5] 没有条件
# list1 = [[1,2,3],[4,5,6],[7,8,9],[1,3,5]]
# newlist = [i[-1] for i in list1]


# dict1 = {'name':'tom','salary':5000}
# dict2 = {'name':'lucy','salary':8000}
# dict3 = {'name':'jack','salary':4500}
# dict4 = {'name':'lily','salary':3000}
# # 如果薪资大于5000加200，低于5000加500
#
#
# list1 = [dict1,dict2,dict3,dict4]
#
# newlist = [person['salary']+200 if person['salary']>5000 else person['salary']+500 for person in list1 ]
# print(newlist)


#集合推导式 {}类似列表推导式，在列表推导式的基础上添加了一个去除重复项
# list1 = [1,2,1,3,5,2,1,3,4,5,9,0]
#
# set1 = {x-1 for x in list1 if x > 5}
# print(set1)

# 字典推导式
# dict1 = {'a':'A','b':'B','c':'C','d':'C'}
#
# newdict = {value:key for key,value in dict1.items()}
#
# print(newdict)


'''
通过列表生成式（列表推导式），我们可以直接创建一个列表
但是，受内存限制，列表容量肯定是有限的
而且，创建一个包含100万个元素的列表，不仅占用很大的储存空间，如果我们仅仅需要访问前面的几个元素，那后面绝大多数元素占用的空间都白白浪费了
所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？
这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator

得到生成器方式：
1.通过列表推导式得到生成器


'''

# [x for x in range(100000000000)]

#[0,3,6,9,12,15,18,21,.....27]

# newlist = [x*3 for x in range(10)]
# print(type(newlist))


# 得到生成器
# g = (x*3 for x in range(10))
# print(type(g)) #generator

# 方式1：通过__next__()方式得到元素
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())

#方式2：next（生成器对象） builtins系统内置函数
#每调用一次next则会产生一个元素
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g)) # StopIteration 生成器本来就可以产生10个，得到了10个，再调用就会抛出异常

# g = (x*3 for x in range(10))
#
# while True:
#     try:
#         e = next(g)
#         print(e)
#     except:
#         print('没有更多元素')
#         break

# 定义生成器的方式二：借助函数完成
#只要函数中出现了yield关键字，说明函数变成生成器了
# 菲波那切数列

'''
步骤：
1.定义一个函数，函数中使用yield关键字
2.调用函数，接收调用的结果
3.得到的结果就是生成器
4.借助next(),__next__()得到元素

'''

# def func():
#     n=0
#     while True:
#         n+=1
#         # print(n)
#         yield n  # return n + 暂停
# g = func()
# print(g)

# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# list = [2,5,4,9,8]
# list1 = list[1:5]
# list2 = []
# for i in list1:
#     if i%2==0:
#         list2.append(i)
# print(list2)

# def fib(length):
#     a,b = 0,1
#     n = 0
#
#     while n<length:
#         # print(b)
#         yield b
#         a,b=b,a+b
#         n+=1
#
#     return '没有更多元素了！' # return就是在得到StopIteration后的提示信息
#
# g = fib(8)
#
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))


'''
生成器方法：
__next__():获取下一个元素
send(Value):向每次生成器调用中传值，注意第一次需要传None,send(None)
'''
# def gen():
#     i=0
#     while i<5:
#         temp = yield i # return 0 + 暂停
#         print('temp:',temp)
#
#         for x in range(temp):
#             print('----->',x)
#         print('************')
#         i += 1
#     return '没有更多的数据'
#
# g = gen()

# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# g.__next__()
# n = g.send(None)
# n1 = g.send(2)
# n2 = g.send(5)
#
# print(n,n1,n2)



# 进程 > 线程 > 协程（交替完成）

# def task1(n):
#     for i in range(n):
#         print('正在搬第{}块砖！'.format(i))
#         yield
#
# def task2(n):
#     for i in range(n):
#         print('正在听第{}首歌！'.format(i))
#         yield
#
# g1 = task1(5)
# g2 = task2(5)
#
# while True:
#     try:
#         g1.__next__()
#         g2.__next__()
#     except:
#         break
'''
生成器:generator
定义生成器方式：
1.通过列表推导式方式
  g = （x+1 for x in range (6)）
  
2.函数+yield
  def fun():
      .....
      yiled
      
    g = fun()
产生元素：
1.next(generator) ---->每次调用都会产生一个新的元素，如果元素产生完毕，再次调用的话会产生异常
2.生成器自己的方法：
   g.__next__()
   g.send(value)
   
应用：协程
'''

# 可迭代的对象：1.generator生成器 2.列表、元组、集合、字典、字符串
# 如何判断一个对象是否可迭代

# from collections.abc import Iterable
# list1=[1,23,45,6,3]
# f = isinstance(list1,Iterable)
# print(f)
#
# f = isinstance("abc",Iterable)
# print(f)
#
# f = isinstance(100,Iterable)
# print(f)
#
# g = (x+1 for x in range(10))
# f = isinstance(g,Iterable)
# print(f)


'''
迭代是访问集合元素的一种方式。迭代器是一个可以记住遍历的位置的对象。
特点：
迭代器对象从集合的第一个元素开始访向直到所有的元素被访问完结束。
迭代器只能往前不会后退。
可以被next()函数调用并不断返回下一个值的对象称为迭代器:Iterator。

可迭代的 是不是肯定就是 迭代器?
生成器是可迭代的，也是迭代器
list是可迭代的，但不是迭代器


list--->iter(list)---->迭代器next()


生成器与迭代器：
生成器是迭代器的一种

'''

# list1 = [1,23,4,6]
# # print(next(list1))  # TypeError: 'list' object is not an iterator
#
# list1 = iter(list1)  # 通过iter()函数将可迭代的变成一个迭代器
#
# print(next(list1))
# print(next(list1))


'''
面向对象：
程序      现实中
对象 ----> 具体的事物

现实中的事物---->转成电脑程序
时间万物皆对象

好处：

面向对象：
类
对象
属性
方法

对象：
小雨的手机
小微的手机
小牧的手机
小四的手机
...

对象的集合 -----> 共同特征：品牌  颜色  大小  价格  内存    动作：打电话 发短信 上网  游戏

类别： 手机类：共同特征：品牌  颜色  大小  价格  内存    动作：打电话 发短信 上网  游戏
      学生类：特征：姓名  年龄  性别  身高  血型  婚否(属性)   动作：刷抖音  敲代码  看书 ...(方法)
      
多个对象 ---> 提取对象的共同特征和动作 ---> 封装到一个类中


'''
# 所以类名要求首字母大写，多个单词使用驼峰式命名
# ValueError
# object
'''
class 类名【（父类）】：
     属性：特征
     方法：动作

'''
# class Phone:
#     # 属性
#     brand = 'huawei'
#     # 方法
#
# print(Phone)

# 使用类创建对象
# yp = Phone()
# print(yp)
# print(yp.brand)
# yp.brand = 'iphone'
# print(yp.brand)
#
#
# feifei = Phone()
# print(feifei)
# print(feifei.brand)
# feifei.brand='iphone xxs'
# print(feifei.brand)
#
#
# xiaowei = Phone()
# print(xiaowei.brand)


# 定义类和属性
# 定义类
# class Student:
    # 类属性
    # name = 'xiaowei'
    # age = 2

# 使用类创建对象
# xiaowei = Student()


#对象属性
# xiaowei.age = 18
#
# print(xiaowei.age)# 先找自己空间中的属性，找不到再去类中找
# print(xiaowei.name)
#
# yupeng = Student()
# yupeng.name = 'xiaopeng'
# yupeng.age = 1
# print(yupeng.name)
#
#
# Student.name='feifei'
#
#
# ruirui = Student()
# print(ruirui.name)


# 类中方法：动作
# 种类： 普通方法 类方法 静态方法 魔术方法
'''
普通方法格式：
def 方法名（self【，参数，参数】）：
   pass

'''
#
# class Phone:
#     brand = 'xiaomi'
#     price = 4999
#     type = 'mate 80'
#
#     #Phone类里面的方法：call
#     def call(self):
#         print('self----------->',self)
#         print('正在打电话......')
#
#
# phone1 = Phone()
# print(phone1)
# # print(phone1.brand)
# phone1.call()
#
#
# print('*'*30)
# phone2 = Phone()
# print(phone2)

# print(int(186/10))


#今日北京天气：阴，气温：高温 4℃~低温 -4℃,感冒多发期，适当减少外出频率，适量补充水分，适当增减衣物。
#请结合任务五，在右侧环境内读取当天北京的最高温度、最低温度、感冒预警信息，并使用格式化字符输出。
# import requests
# data = requests.get('http://wthrcdn.etouch.cn/weather_mini?city=北京')
# weather = data.json()
# print(weather)
# print(weather['data']['forecast'][1]['fengli'])
# city = weather["data"]['city']
# tianqi = weather['data']['forecast'][0]['type']
# gaowen = weather['data']['forecast'][0]['high']
# diwen = weather['data']['forecast'][0]['low']
# ganmao = weather['data']['ganmao']
# print('今日{}天气：{}，气温：{}~{}，{}'.format(city,tianqi,gaowen,diwen,ganmao))


# i = 2
# while (i < 100):
#     j = 2
#     while (j <= (i / j)):
#         if not (i % j): break
#         j = j + 1
#     if (j > i / j):
#         print(i, " 是素数")
#     i = i + 1
#
# print("Good bye!")


dic1 = {'1':'星期一','2':'星期二','3':'星期三','4':'星期四','5':'星期五','6':'星期六','7':'星期日'}
s = int(input("请输入1-7的数字："))
for i in dic1:
    if s == dic1[i] and s > 0:
        print(i)
    else:
        print('输入错误！')
        break