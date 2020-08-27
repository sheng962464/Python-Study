"""
1. __new__方法的第一个参数是这个类，而其余的参数会在调用成功后全部传递给__init__方法初始化
2. 如果__new__方法返回None，则__init__方法不会被执行
3. __init__是当实例对象创建完成后被调用的，然后设置对象属性的一些初始值。
   __new__是在实例创建之前被调用的，因为它的任务就是创建实例然后返回该实例，是个静态方法。

"""


class A:
    """
    相当于要做三件事：
        1. 调用__new__方法来创建对象，然后找一个变量来接受__new__的返回值，这个返回值表示创建出来的对象的引用
        2. __init__(self)函数执行，其中self为刚刚创建出来的对象引用
        3. 返回对象的引用
    """

    def __init__(self):
        print('这是init方法:')
        print('__init__收到的对象为：', self)
        print()

    def __new__(cls, *args, **kwargs):
        print('这是new方法:')
        print('cls的地址为：', id(cls))
        ret = super().__new__(cls)
        print('__new__实例化的对象为', ret)
        print()
        return ret


if __name__ == '__main__':
    print('Class A的地址为：', id(A))
    print()
    a = A()

