"""
1. 如果子类(Puple)继承父类(Person)不做初始化，那么会自动继承父类(Person)属性name。
        即pass
2. 如果子类(Puple_Init)继承父类(Person)做了初始化，且不调用super初始化父类构造函数，那么子类(Puple_Init)不会自动继承父类的属性(name)。
        即无super().__init__()
3. 如果子类(Puple_super)继承父类(Person)做了初始化，且调用了super初始化了父类的构造函数，那么子类(Puple_Super)也会继承父类的(name)属性。
        即有super().__init__()

"""


class Person:
    def __init__(self, name='Person'):
        self.name = name


class Puple(Person):
    pass


class Puple_Init(Person):
    # pycharm这里会给出提示__init__没有继承父类的初始化
    def __init__(self, age):
        # 根据pycharm提示添加的语句，用于继承父类的初始化
        # super().__init__()
        self.age = age


class Puple_Super(Person):
    def __init__(self, name, age):
        self.age = age
        super().__init__(name)


pp = Puple()
pp_i = Puple_Init(10)
pp_s = Puple_Super('Puple_Super', 12)

print(pp.name)
# print(pp_i.name)              # 该注释去掉之后会报错，因为在Puple_Init类中并没有继承父类的属性,所以pp_i并没有name属性
print(pp_s.name)
