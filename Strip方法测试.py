"""
Python中有三个去除头尾字符、空白符的函数，它们依次为:

strip： 用来去除头尾字符、空白符(包括\n、\r、\t、' '，即：换行、回车、制表符、空格)

lstrip：用来去除开头字符、空白符(包括\n、\r、\t、' '，即：换行、回车、制表符、空格)

rstrip：用来去除结尾字符、空白符(包括\n、\r、\t、' '，即：换行、回车、制表符、空格)

从字面可以看出r=right，l=left，strip、rstrip、lstrip是开发中常用的字符串格式化的方法。

注意：这些函数都只会删除头和尾的字符，中间的不会删除。
"""

name = '         python              '
print(name.strip(), '#')
name = '         python              '
print(name.lstrip(), '#')
name = '         python              '
print(name.rstrip(), '#')

name = '    1     python      1        '
print(name.strip(), '#')


print('#########################################')


# 当strip函数中存在参数时，把参数视为一个一个字符，删除开头和结尾的字符
name = '00000000011100000000111000200000python000002000011100000111100000000000000000'
print(name.strip('01'))


