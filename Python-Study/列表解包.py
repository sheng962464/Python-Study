def unpack(a, b, c):
    print(a, b, c)


# *号用于列表解包作为参数
unpack(*[1, 2, 3])
unpack(*(2, 3, 4))

# 可以往函数中传入一个列表后进行解包
