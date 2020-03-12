orgList = [1, 0, 3, 7, 7, 5]

# 不保留原来的顺序
formatList = list(set(orgList))
print(formatList)

# 不保留原来的顺序
formatList = list({}.fromkeys(orgList).keys())
print(formatList)

# 按照索引再次排序
formatList = list(set(orgList))
formatList.sort(key=orgList.index)
print(formatList)
