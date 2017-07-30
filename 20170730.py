### 切片 ###
# sString = "testString"
# sSlice = sString[0:-2]
# print(sSlice)
#
# lList = ['apple', 'orange', 'grape', 'pear', 'pineapple']
# lSlice = lList[2:4]
# print(lSlice)


### 列表生成式 ###
# l = [x for x in range(10)]
# print(l)
#
# l = [x**3 for x in range(1, 7)]
# print(l)
#
# l = [x for x in range(0, 20) if x % 2 == 0]
# print(l)


### generator 生成器 ###
# 函数体中含有yield的函数是生成器，每次运行遇到yield则返回一次
# def gener(a):
#     for i in range(1, a+1):
#         if i % 2 != 0:
#             yield i
#     return 'success'
#
# for x in gener(10):
#     print(x)


def yangTriangle(n):
    if not isinstance(n, int):
        raise TypeError
    if n <= 0:
        raise ValueError
    for i in range(1, n + 1):
        if i == 1:
            yield [1, ]
        elif i == 2:
            l = [1, 1]
            yield l
        else:
            l2 = []
            if l2 != []:
               # print("in")
               l = l2
            else:
                # print("else")
                l2 = [1, 1]
            l2 = l[:]
            for x in range(1, i - 1):
                # print("before l, l2", l, l2, x)
                l2[x] = l[x-1] + l[x]
                # print("after l, l2", l, l2, x)
            l2.append(1)
            l = l2
            yield l
    return 'done'

for x in  yangTriangle(15):
    print(x)
