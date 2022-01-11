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

#定义一个装饰器
def decorate(func):
    a = 100
    print('wrapper外层打印测试')

    def wrapper():
        func()
        print('------->硬装')
        # func()
        print('-------->软装',a)

    print('wrapper加载完成....')
    return wrapper

# 使用装饰器
@decorate
def house():
    print("我是毛坯房。。。。")

# 调用函数house
# house()










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



