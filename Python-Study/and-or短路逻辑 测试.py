"""
表达式从左至右运算，若 or 的左侧逻辑值为 True ，则短路 or 后所有的表达式（不管是 and 还是 or），直接输出 or 左侧表达式 。
表达式从左至右运算，若 and 的左侧逻辑值为 False ，则短路其后所有 and 表达式，直到有 or 出现，输出 and 左侧表达式到 or 的左侧。
若 or 的左侧为 False ，或者 and 的左侧为 True 则不能使用短路逻辑。
"""


def a(x):
    print('A', end=' ')
    return x


def b(x):
    print('B', end=' ')
    return x


def c(x):
    print('C', end=' ')
    return x


def d(x):
    print('D', end=' ')
    return x


def e(x):
    print('E', end=' ')
    return x


def f(x):
    print('F', end=' ')
    return x


def g(x):
    print('G', end=' ')
    return x


def h(x):
    print('H', end=' ')
    return x


# 只要是任何为空的对象都能被当做false，如'',[],0,()等

print('example 1:')
if a(0) and b(1) and c(1) and d(0) and e(1):
    """
    a()为假 ，其后均为 and 语句，全部短路，最终只返回 a() 的表达式。
    记住，所有被短路的表达式均不会被输出。所以，此处仅仅打印 A 。
    """
    print('ok')
else:
    print()

print('example 2:')
if a(1) and b(1) and c(0) and d(1) and e(1):
    """
    python 从左至右先执行 a() ,a() 返回的逻辑值为 True，后面是 and 语句，所以不能短路其后，
    继续与 b() 进行逻辑运算，a() and b() 输出 b() 的逻辑值 True，
    接着与 c() 进行逻辑运算，b() and c() 输出 c() 的逻辑值 False，
    而其后均为 and 语句， 则全部短路，最终只打印了 A B C 。
    """
    print('ok')
else:
    print()

print('example 3:')
if a(1) or b(1) or c(0) or d(1) or e(0):
    """
    a() 的逻辑值为 True ，其后均为 or 语句，全部短路，最终只打印了 A，
    而 if 语句为 True ，所以还要打印一个 ok。
    """
    print('ok')
else:
    print()

print('example 4:')
if a(0) or b(0) or c(1) or d(0) or e(1):
    """
    python 从左至右先执行 a() ,a() 返回的逻辑值为 False，后面是 or 语句，所以不能短路其后，
    继续与 b() 进行逻辑运算，a() or b() 输出 b() 的逻辑值 False，
    接着与 c() 进行逻辑运算，b() or c() 输出 c() 的逻辑值 True，
    而其后为 or 语句， 则全部短路，最终只打印了 A B C ok。
    """
    print('ok')
else:
    print()

print('example 5:')
if a(0) and b(0) and c(1) and d(0) or e(1) and f(1) or g(0) and h(1):
    """
    从左至右，首先a() 的逻辑值为 False，
    其后到 or 语句为止有三个 and 语句： a() and b() and c() and d()，均被短路。
    只输出 a(), 得到 a() or e() 为True，
    输出 e() ,得 e() and F() 为 True ,输出 f(), 
    其后接 or 语句，则短路其后所有。最终只打印了A E F ok 。
    """
    print('ok')
else:
    print()


"""
三元操作符
return a if bool else b

类似于C，C++，Java中  bool?a:b  若bool为真则a，否则为b
"""

