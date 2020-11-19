from progressbar import *
import time
from tqdm import tqdm
import sys

total = 1000


def dosomework():
    time.sleep(0.01)


# 使用progressbar包
progress = ProgressBar()
for i in progress(range(1000)):
    dosomework()

# 使用tqdm包
for i in tqdm(range(20)):
    time.sleep(0.5)

# sys.stdout.write()方法跟print()方法的区别是 前者打印不换行，后者换行。
# sys.stdout.flush()方法是立即刷新输出的内容
print("正在下载......")
for i in range(11):
    if i != 10:
        sys.stdout.write("==")
    else:
        sys.stdout.write("== " + str(i * 10) + "%/100%")
    sys.stdout.flush()
    time.sleep(0.2)
print("\n" + "下载完成")
