# 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

# list=[]
# for i in range(1,5):
#     # print(i)
#     for j in range(1,5):
#         for k in range(1,5):
#             if i!=j or k!= i or k!=j:
#                 continue
#             else:
#                 list = list.append(str(i)+str(j)+str(k))
#                 print(list)


L = []
a = [1, 2, 3, 4]

# for i in range(len(a)):

for val_1 in a:
    for val_2 in a:
        for val_3 in a:
            if (val_1 == val_2 or val_1 == val_3 or val_2 == val_3):
                continue
            else:
                L.append(str(val_1) + str(val_2) + str(val_3))

print(len(L))
print(L)