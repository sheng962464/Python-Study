import time


# 这是装饰器函数，参数 func 是被装饰的函数
def logger(func):
    def wrapper(*args, **kw):
        print('开始执行：{} 函数了:'.format(func.__name__))

        # 真正执行的是这行。
        func(*args, **kw)

        print('执行结束')

    return wrapper


# 这是装饰函数
def timer(func):
    def wrapper(*args, **kw):
        t1 = time.time()
        # 这是函数真正执行的地方
        func(*args, **kw)
        t2 = time.time()

        # 计算下时长
        cost_time = t2 - t1
        print("花费时间：{}秒".format(cost_time))

    return wrapper
