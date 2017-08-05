### plt画图练习 ###
import matplotlib.pyplot as plt
import numpy as np

# plt.plot([1, 2, 3, 4])  # (0, 1) (1, 2) (2, 3) (3, 4)
# # plt.xlabel / ylabel:为坐标轴添加注释
# # plt.title:添加标题
# plt.title('a picture')
# plt.xlabel('x label')
# plt.ylabel('some numbers')
# plt.grid(True)  # 添加栅格
# plt.legend('upper')  # 添加图例
# plt.show()


# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'b-', linewidth=10)  # plot()可以接受两个list，分别作为x和y的取值
# # plot()第三个参数控制线的颜色和样式 linewidth控制线的宽度
# plt.axis([0, 10, 0, 20])
# # plt.axis()分别控制xy轴的显示范围
# plt.show()

# n = np.arange(0., 5., 0.2)
# # 在一幅图中画多条线
# plt.plot(n, n, 'r--', n, (n**2 + 1), 'rs', n, n**3, 'g^')
# plt.show()

# lines = plt.plot([1, 3, 7, 11])
# plt.setp(lines, linewidth=2.5, color='orange')
# plt.show()

# 一次显示多幅图像
# n = np.arange(0, 10, 0.1)
# plt.figure(1)  # 设置显示窗口
# plt.subplot(211)  # 设置小图像位置 plt.subplot(行数，列数，图像编号)
# plt.plot(n, n**2, 'k')
#
# plt.subplot(212)
# plt.plot(n, np.sin(n), 'ro')
# plt.show()



