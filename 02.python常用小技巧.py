"""
01. 原地交换两个数字
02. 链状比较操作符
03. 使用三元操作符来实现条件赋值
04. 多行字符串
05. 存储列表元素到新的变量
06. 打印引入模块的绝对路径
07. 交互环境下的"_"操作符
08. 字典/集合推导
09. 调试脚本
10. 开启文件分享
11. 检查python中的对象
12. 简化if语句
13. 运行时检测python版本
14. 组合多个字符串
15. 翻转字符串、列表的方式
16. 用枚举在循环中找到索引
17. 定义枚举量
18. 从方法中返回多个值
19. 使用*运算符解包函数参数
20. 用字典来存储表达式
21. 计算任何数的阶乘
22. 找到列表中出现次数最多的数
23. 重置递归限制
24. 检查一个对象的内存使用
25. 使用slots减少内存开支
26. 用lambda来模仿输出方法
27. 从两个相关序列构建一个字典
28. 搜索字符串的多个前后缀
29. 不使用循环构造一个列表
30. 实现switch-case语句
"""

# 1.原地交换两个数字
x, y = 10, 20
print(x, y)
y, x = x, y
print(x, y)

# 2. 链状比较操作符
n = 10
print(1 < n < 20)
print(1 > n <= 9)

# 3. 使用三元操作符来实现条件赋值
# [表达式为真的返回值] if [表达式] else [表达式为假的返回值]
y = 20
x = 9 if (y == 20) else 8
print(x)


# 找abc中最小的数
def small(a, b, c):
    return a if a < b and a < c else (b if b < a and b < c else c)


print(small(1, 0, 1))
print(small(1, 2, 2))
print(small(2, 2, 3))
print(small(5, 4, 3))

# 列表推导
x = [m ** 2 if m > 10 else m ** 4 for m in range(50)]
print(x)

# 4. 多行字符串
multistr = "select * from multi_row \
where row_id < 5"
print(multistr)

multistr = """select * from multi_row
where row_id < 5"""
print(multistr)  # 能显示真正的多行

multistr = ("select * from multi_row"
            "where row_id < 5"
            "order by age")
print(multistr)

# 5. 存储列表元素到新的变量
testList = [1, 2, 3]
x, y, z = testList  # 变量个数应该和列表长度严格一致
print(x, y, z)

# 6. 打印引入模块的绝对路径
import threading
import socket

print(threading)
print(socket)

# 7. 交互环境下的“_”操作符
"""
在python控制台，不论我们测试一个表达式还是调用一个方法，结果都会分配给一个临时变量“_”
"""

# 8. 字典/集合推导
testDic = {i: i * i for i in range(10)}
testSet = {i * 2 for i in range(10)}
print(testDic)
print(testSet)

# 9. 调试脚本
import pdb

# 先注释掉，不然每次都要在这里停止
# pdb.set_trace()

# 10. 开启文件分享
pass


# 11. 检查python中的对象
class A:
    def __init__(self):
        self.age = 10


a = A()
print(dir(a))

# 12. 简化if语句
# use following way to verify multi values
m = 2
if m in [1, 2, 3, 4]:
    pass
# 不要用下面的方法
if m == 1 or m == 2 or m == 3 or m == 4:
    pass

# 13. 运行时检测python版本
import sys

if not hasattr(sys, "hexversion") or sys.version_info != (2, 7):
    print("sorry, you are not running on python 2.7")
    print("current python version:", sys.version)

# 14. 组合多个字符串
test = ["I", "Like", "Python"]
print(test)
print(" ".join(test))  # 前面的' '表示字符串中间的分隔符

# 15. 翻转字符串、列表
pass

# 16. 用枚举在循环中找到索引
test = [10, 20, 30]
for i, value in enumerate(test):
    print(i, ':', value)


# 17. 定义枚举量
class shapes:
    circle, square, triangle, quadrangle = range(4)


print(shapes.circle)
print(shapes.square)
print(shapes.triangle)
print(shapes.quadrangle)


# 18. 从方法中返回多个值
def x():
    return 1, 2, 3, 4


a, b, c, d = x()
print(a, b, c, d)


# 19. 使用*运算符解包函数参数
def test(x, y, z):
    print(x, y, z)


testDic = {'x': 1, 'y': 2, 'z': 3}
testList = [10, 20, 30]
test(*testDic)  # 对于字典，*表示键，**表示值
test(**testDic)
test(*testList)

# 20. 用字典来存储表达式
stdcalc = {
    "sum": lambda x, y: x + y,
    "subtract": test
}

# 字典的键定义为函数名，而值为lambda表达式，也可以是函数的名字(不加括号)
print(stdcalc["sum"](9, 3))
stdcalc["subtract"](9, 3, 3)

# 21. 计算任何数的阶乘
# 这里functools没有完全理解
import functools

result = (lambda k: functools.reduce(int.__mul__, range(1, k + 1), 1))(3)
print(result)

# 22. 找到列表中出现次数最多的数
test = [5, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4, 4]
print(set(test))
print(max(set(test)))  # 找到最大的数
print(max(set(test), key=test.count))  # 找到出现次数最多的数
print(test.count(4))  # test.count(obj)统计某个元素在列表中的次数

# 23. 重置递归限制
# python限制递归次数到1000，可以用下面的方法重置
import sys

x = 1200
print(sys.getrecursionlimit())
sys.setrecursionlimit(x)
print(sys.getrecursionlimit())

# 24. 检查一个对象的内存使用
import sys

x = 1
print(sys.getsizeof(x))

# 25. 使用slots减少内存开支

import sys


# 原始类
class FileSystem(object):
    def __init__(self, files, folders, devices):
        self.files = files
        self.folder = folders
        self.devices = devices


print(sys.getsizeof(FileSystem))


# 减少内存后
class FileSystem(object):
    __slots__ = ['files', 'folders', 'devices']

    def __init__(self, files, folders, devices):
        self.files = files
        self.folder = folders
        self.devices = devices


print(sys.getsizeof(FileSystem))

# 26. 用lambda方法来模仿输出
# map()方法，将列表中的吗
import sys

lprint = lambda *args: sys.stdout.write(" ".join(map(str, args)))
lprint("python", "tips", 1000, 1001)
print()

# 27. 从两个相关序列构建一个字典
t1 = (1, 2, 3)
t2 = (10, 20, 30)
print(dict(zip(t1, t2)))
print(list(zip(t1, t2)))

# 28. 搜索字符串的多个前后缀
print("http://localhost:8888/notebooks/Untitled6.ipynb".startswith(("http://", "https://")))
print("http://localhost:8888/notebooks/Untitled6.ipynb".endswith((".ipynb", ".py")))

# 29. 不使用循环构造一个列表
import itertools
import numpy as np

test = [[-1, -2], [30, 40], [25, 35]]
print(list(itertools.chain.from_iterable(test)))


# 30. 实现switch-case语句
def xswitch(x):
    return xswitch._system_dict.get(x, None)


xswitch._system_dict = {"files": 10, "folders": 5, "devices": 2}
print(xswitch("default"))
print(xswitch("devices"))
