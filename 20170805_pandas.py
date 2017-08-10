### pandas练习 ###
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Pandas 有2种数据类型
# Series：带标签的数组，类似php中key-value数组，标签可以是数字或字符串
# a = pd.Series([1, 0, 'hello', np.NaN, True])
# print(a)

# DataFrame：一种二维的表结构，每一个坐标轴都有标签，类似二维的key-value数组或者带标签的矩阵
dates = pd.date_range('20130101', periods=6)
# print(dates)
# pd.date_range(start, end, periods, freq, tz, normalize, name, closed)
# periods:产生日期个数   freq:指定计时单位，默认是D(Y-m-d)    tz:timezone，时区
# normalize:默认False，如果True则会把start和end转化为0时    name:名字
# closed:String或None，默认None，表示start和end端点是否包含 left:左闭右开 right:右闭左开 None:两边均为闭区间

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=['A', 'B', 'C', 'D'])
# index：左侧索引(每一行的索引)    columns：每一列的索引
# print(df)

# print(df.head())  # 观察前n行，默认是5行
# print(df.tail(3))  # 观察后n行，默认是5行

# 其他基本信息
# print(df.index)  # 行索引
# print(df.columns)  # 列索引
# print(df.values)  # 去掉索引的数值
# print(df.describe())  # 一些统计信息
# print(df.info())  # 一些基本信息

# print(df.T)  # 转置
# print(df.sort_index(axis=1, ascending=False))  # 按索引排序
# print(df.sort_index(axis=0, ascending=False))
#
# print(df.sort_values(by='B'))  # 按值排序

# DataFrame的选择
# DataFrame中选中一列，与Series等效
# print(df.A)  # 两种写法都可以
# print(df["A"])

# print(df[1:3])  # 1 - 3 行(索引1-2，前包后不包)
# print(df['2013-01-02':'2013-01-05'])  # 前后都是闭区间
