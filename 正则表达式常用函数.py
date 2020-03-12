import re

'''
match和search的区别：
1. match()函数只检测RE是不是在string的开始位置匹配，
2. search()会扫描整个string查找匹配
3. match()只有在0位置匹配成功的话才有返回，如果不是开始位置匹配成功的话，match()就返回none
'''

text = 'PythonTab.com is a good Python website'
m = re.match(" is", text)
print(m)
if m:
    print(m.group())
else:
    print('not match')

result = re.match("hello", "hello,world")
if result:
    print(result.group())
else:
    print("匹配失败!")
