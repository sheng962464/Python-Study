import numpy as np

# 输入系数矩阵A
A = np.array([[2, 4, -11], [3, -5, -3], [1, 2, -6], [2, 1, -7]])

# 对A进行svd分解
U, Sigma, VT = np.linalg.svd(A)
print(f'矩阵VT为：\n{VT}')

x_1 = VT[2, 0] / VT[2, 2]
x_2 = VT[2, 1] / VT[2, 2]
print(f'x1 = {x_1}, x2 = {x_2}')

# 求解,V的列向量即是A^TA的特征向量
# VT最后一行的行向量即为最小特征值对应的特征向量
# 由于x[3,0]=1,所以需要对结果进行处理
# k = 1 / VT[2, 2]
# x_1 = VT[2, 0] * k
# x_2 = VT[2, 1] * k
# print(x_1, x_2)
#
# 误差
X = np.array([[x_1], [x_2], [1]])
R = np.dot(np.transpose(np.dot(A, X)), (np.dot(A, X)))
print(f'误差为：{R[0,0]}')

"""
https://blog.csdn.net/qq_45427038/article/details/100655624?utm_medium=distribute.pc_relevant_right.none-task-blog-OPENSEARCH-11&depth_1-utm_source=distribute.pc_relevant_right.none-task-blog-OPENSEARCH-11
https://blog.csdn.net/zhongkejingwang/article/details/43053513?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-1&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-1
"""