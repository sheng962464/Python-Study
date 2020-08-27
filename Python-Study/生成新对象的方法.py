import sys
import copy
import types


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# 普通调用init函数
point1 = Point(1, 2)
# point1的深拷贝
point6 = copy.deepcopy(point1)

# 下面全是花里胡哨的写法(了解一下就行)
# 字符串为Point(1,2),利用eval执行了这个字符串表达式，并返回表达式的值
point2 = eval("{}({}, {})".format("Point", 1, 2))
# global()函数返回当前位置的全部全局变量,以字典的形式返回
# global()["Point"]相当于调用Point类
point3 = globals()["Point"](1, 2)
# locals()同理
point4 = locals()["Point"](1, 2)
# 根据函数名"Point"，获得函数对象
point5 = getattr(sys.modules[__name__], "Point")(1, 2)
# 获得point1对象的类型point
point7 = point1.__class__(1, 2)
# type(name,base,dict)
# name: 类的名称
# base: 基类的元组
# dict: 字典，类内定义的命名空间变量
# 类似于创建了一个新的类？？？？我母鸡呀
point8 = type('Point', (Point,), {})(1, 2)
point9 = types.new_class('Point', (Point,), {})(1, 2)
