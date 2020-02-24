# python3 列表合并的3种方法

# 1. 直接使用‘+’合并
a1List = [1, 2, 3]
b1List = ['www', 'pythontab.com']
cList = a1List + b1List
dList = b1List + a1List
print(cList)
print(dList)

# 2. 使用extend方法
aList = [1, 2, 3]
bList = ['www', 'pythontab.com']
aList.extend(bList)
print(aList)

# 3. 使用切片
aList = [1, 2, 3]
bList = ['www', 'pythontab.com']
aList[len(aList):len(aList)] = bList
print(aList)

'''
第一种方方法思路比较清晰，就是运算符的重载；

第二种方法比较简洁，但会覆盖原始list；

第三种方法功能比较强大，可以将一个列表插入另一个列表的任意位置
'''
