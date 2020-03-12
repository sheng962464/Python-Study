listA = [1, 2, 3, 4]
listB = [2, 3, 4]

# 差集
ret = list(set(listA) ^ set(listB))

print('两者差集结果1：', ret)

ret = list(set(listA).difference(set(listB)))
print('两者差集结果2：', ret)

# 并集
ret = list(set(listA).union(set(listB)))
print('两者并集结果：', ret)

# 交集
ret = list(set(listA).intersection(set(listB)))
print('两者交集结果：', ret)
