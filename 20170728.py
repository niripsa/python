### 使用python进行数学运算 ###
# 加法
# print(1 + 1)

# 减法
# print(2 - 1)

# 乘法
# print(2 * 4)

# 除法
# print(5 / 2)

# 求余
# print(5 % 2)

# 地板除
# print(5 // 2)

# 乘方
# print(2 ** 3)


### 格式控制符 ###
# print("%f" % (5/3))  # 1.666667
# print("%.2f" % (5/3))  # 1.67
# print("%f" % (415 * 20.2))  # 8383.000000
# print("%0.f" % (415 * 20.2))  # 8383

# 格式控制会进行四舍五入
# print("$%.3f" % 30.00123)  # $30.001
# print("$%.3f" % 30.00173)  # $30.002

# 在python中使用浮点数运算会导致整个算式改用浮点数，去掉所有浮点数会导致将所有数看做int，除非结果是浮点数


### python保留词 ###
# and, as, assert, break, class, continue, def, del, elif, else, except, exec
# False, finally, for, from, global, if, import, in, is, lambda, not, None
# or, pass, print, raise, return, try, True, while, with, yield


### python内置类型 tuple list dict set ###
## 元组 tuple ---- 不可更改的数据序列 ##

# 元组是值的序列，其中每个值都可以被访问，但不可更改；元组被小括号()包围
# a = ('first', 'second', 'third')
# print(a)
# print(a[0])
# print(a[2])
# b = (a, "b\'s second element")
# print(b)
# print(b[0][1])
# 注：若要创建一个只有一个元素的元组，需要在末尾加一个逗号，否则会被认为是字符串

## 列表 list ---- 可以更改的数据序列 ##

# 列表类似元组，包含从0开始引用元素的序列，其中元素可以被更改；被中括号[]包围；类似php数组
# 列表已有的元素，可以直接修改
# breakfast = ['coffee', 'tea', 'toast', 'egg']
# print(breakfast)
# breakfast[0] = 'pie'
# print(breakfast)
#
# # 向列表末尾添加单个元素，使用内置的append方法
# breakfast.append('milk')
# print(breakfast)
# # 向列表末尾添加多个元素，使用内置的extend方法，该方法传入一个list或tuple，将其中每个元素追加到原列表末尾
# breakfast.extend(['apple', 'banana', 'pear'])
# print(breakfast)
# # 列表的长度可以由内置的len方法确定，长度是从1开始的
# print(breakfast.__len__())

