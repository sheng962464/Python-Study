from progress.bar import Bar
import time

bar_test = Bar('Processing', max=20)
for i in range(20):
    i += 1
    bar_test.next()
    time.sleep(1)
bar_test.finish()

# 这个程序没调通，没看到进度条