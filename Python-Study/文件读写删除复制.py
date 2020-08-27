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


##################################################################
'''
https://www.pythontab.com/html/2018/pythonjichu_0131/1237.html
r	以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
w	以写方式打开，
a	以追加模式打开 (从 EOF 开始, 必要时创建新文件)
r+	以读写模式打开
w+	以读写模式打开 (参见 w )
a+	以读写模式打开 (参见 a )
rb	以二进制读模式打开
wb	以二进制写模式打开 (参见 w )
ab	以二进制追加模式打开 (参见 a )
rb+	以二进制读写模式打开 (参见 r+ )
wb+	以二进制读写模式打开 (参见 w+ )
ab+	以二进制读写模式打开 (参见 a+ )



os.getcwd()	                            得到当前工作目录，即当前Python脚本工作的目录路径
os.listdir()	                        返回指定目录下的所有文件和目录名
os.remove()	                            函数用来删除一个文件
os.removedirs(r"c/python")	            删除多个目录
os.path.isfile()	                    检验给出的路径是否是一个文件
os.path.isdir()	                        检验给出的路径是否是一个目录
os.path.isabs()	                        判断是否是绝对路径
os.path.exists()	                    检验给出的路径是否真地存
os.path.split()	                        返回一个路径的目录名和文件名
os.path.splitext()	                    分离扩展名
os.path.dirname()	                    获取路径名
os.path.basename()	                    获取文件名
os.system()	                            运行shell命令
os.getenv() 与os.putenv()	            读取和设置环境变量
os.linesep 	                            给出当前平台使用的行终止符，Windows使用'rn'，Linux使用'n'而Mac使用'r'
os.name	                                指示你正在使用的平台，对于Windows，它是'nt'，而对于Linux/Unix用户，它是'posix'
os.rename(old, new)	                    重命名
os.makedirs(r"c：/python/test")	        创建多级目录
os.mkdir("test")	                    创建单个目录
os.stat(file)	                        获取文件属性
os.chmod(file)	                        修改文件权限与时间戳
os.exit()	                            终止当前进程
os.path.getsize(filename)	            获取文件大小
os.mkdir("file")	                    创建目录
shutil.copyfile("oldfile","newfile")	复制文件, oldfile和newfile都只能是文件
shutil.copy("oldfile","newfile")	    oldfile只能是文件夹，newfile可以是文件，也可以是目标目录
shutil.copytree("olddir","newdir")	    复制文件夹, olddir和newdir都只能是目录，且newdir必须不存在
os.rename("oldname","newname")	        重命名文件（目录）,文件或目录都是使用这条命令
shutil.move("oldpos","newpos")	        移动文件（目录）
os.remove("file")	                    删除文件
os.rmdir("dir")	                        删除目录, 只能删除空目录
shutil.rmtree("dir")	                空目录、有内容的目录都可以删
os.chdir("path")	                    转换目录, 换路径
os.mknod("test.txt")	                创建空文件
'''