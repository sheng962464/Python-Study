import numpy as np

"""
numpy.dot() 
对于两个一维的数组，计算的是这两个数组对应下标元素的乘积和(数学上称之为内积)；
对于二维数组，计算的是两个数组的矩阵乘积；
"""
print(np.dot(np.array([2, 3]), np.array([3, 4])))

a = np.array([[1, 2], [3, 4]])
b = np.array([[11, 12], [13, 14]])
# 矩阵乘法
print(np.dot(a, b))

ax, ay, az = np.array([1, 2, 3])
print(ax, ay, az)
