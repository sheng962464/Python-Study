class Person(object):  # 定义一个人类，继承objec
    def __init__(self):
        print("我要好好学习")

    def study(self):
        print("我要学好语言")


class man(Person):  # 定义一个男人，继承人类
    def __init__(self):
        print("我是男人我要好好学习")

    def study(self):
        print("我要学好数学")


class woman(Person):  # 定义一个女人，继承人类
    def __init__(self):
        print("我是女人我要好好学习")

    def study(self):
        print("我要学好英语")


class son(man, woman):  # 定义一个儿子，继承男人和女人
    def __init__(self):
        print("我是儿子我要好好学习")

    def study(self):
        print("我要学好化学和物理")
        # woman.study(self)
        # man.study(self)

        super().study()

    # def study1(self):
    #     print("我要学好英语")


"""
在son的类中的study函数中增加了 woman.study(self) 这句好相当于直接调用woman类中的study函数 同理也可以直接调用man类中的study函数；
这样就不用创建新函数了；这种等于直接调用。
我们还可以使用另外一种方式来调用man和woman中的study函数即：super().study();
前面两种我们已经注释掉了我们只研究最后一种；
即出现了上面的代码；但是其实并不会调用woman.study()
"""

son1 = son()
son1.study()
# son1.study1()


# super()不是指父类（对于man类来说Person应该是父类）而只指以实例化对象为起点的mro序列中的下一个
# 详细解释可以看这篇博客
# https://www.cnblogs.com/yan-peng/p/9961384.html
