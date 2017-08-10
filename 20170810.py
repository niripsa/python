import jieba
import numpy as np
from collections import Counter


def get_cos_similar(file1, file2):
    # 读取文件并分词
    with open(file1, 'rb') as f1:
        data1 = jieba.cut(f1.read())
    with open(file2, 'rb') as f2:
        data2 = jieba.cut(f2.read())

    # 进行统计
    data1 = dict(Counter(data1))
    data2 = dict(Counter(data2))

    # 注：setdefault()函数不可用kwargs，否则会报错
    for k1 in data1:
        data2.setdefault(k1, 0)
    for k2 in data2:
        data1.setdefault(k2, 0)

    # 转化成np数组并计算
    # print(dict(sorted(data1.items())).values())
    # print(dict(sorted(data2.items())).values())
    data1 = np.array(list(dict(sorted(data1.items())).values()))
    data2 = np.array(list(dict(sorted(data2.items())).values()))
    result = np.dot(data1, data2) / (np.sqrt(np.dot(data1, data1)) * np.sqrt(np.dot(data2, data2)))
    return result

print("两篇文章的相似度是: %f" % get_cos_similar('./file1.txt', './file2.txt'))
