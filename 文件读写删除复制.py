import os

file_path = '1.txt'
assert os.path.exists(file_path)
# 读文件
with open(file_path, 'r')as f:
    for line in f:
        print(line)

# 写文件
with open(file_path, 'w') as f:
    print('Hello World!', file=f)

# 删除文件
if os.path.exists(file_path):
    os.remove(file_path)
    print("删除成功")
else:
    print('文件不存在')
# 复制文件
with open("a.txt") as src, open("a_copy.txt", 'w') as dest:
    dest.write(src.read())
print('复制成功啦！')
