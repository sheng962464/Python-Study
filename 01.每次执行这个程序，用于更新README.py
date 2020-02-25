import os

# 文件头
file_head = """# Python-Study
该库主要用python的语法学习与复习
记得在每次更新库之后，执行'01.每次执行这个程序，用于更新README.py'用于更新该文件的目录。

## 该库的目录如下(便于后期查找)：
"""
README_path = 'README.md'
Folder_Path = os.path.dirname(os.path.abspath(__file__))
print('当前目录的绝对路径为：', Folder_Path)
print()
print('当前目录下的如下：')

python_file = []

for file in os.listdir(Folder_Path):
    if file.endswith(('.py', '.md')) and file != README_path:
        python_file.append(file)
        print(file)

with open(README_path, 'w', encoding='utf-8') as ReadMe_F:
    print(file_head, file=ReadMe_F)
    for x in python_file:
        print(x, '  ', file=ReadMe_F)           # 加俩空格，md文件才能显示换行
file_num = len(python_file)
print()
print(f'以上文件均已写入README.md文件中，共{file_num}个！')
