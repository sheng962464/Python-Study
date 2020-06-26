import time
import numpy as np

a = list(np.random.uniform(size=1000000))
b = list(np.random.uniform(size=1000000))

start_time = time.time()
sum_a = 0
sum_a2 = 0
sum_b = 0
sum_b2 = 0
sum_ab = 0

for i in range(1000000):
    sum_a += a[i]
    sum_a2 += a[i] ** 2
    sum_b += b[i]
    sum_b2 += b[i] ** 2
    sum_ab += a[i] * b[i]
end_time = time.time()
print(sum_ab)
print(f"sum_a += i_a 耗时：{end_time - start_time}")

start_time = time.time()

sum_a = sum(a)
a2 = [x ** 2 for x in a]
sum_a2 = sum(a2)
sum_b = sum(b)
b2 = [y ** 2 for y in b]
sum_b2 = sum(b2)
sum_ab = sum(map(lambda x_a, x_b: x_a * x_b, a, b))
end_time = time.time()
print(sum_ab)
print(f"sum_a = sum(a) 耗时：{end_time - start_time}")
