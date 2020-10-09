import os
import time


def unlock(x_target_path):
    index = 0
    for root, dirs, files in os.walk(x_target_path):
        # root 表示当前正在访问的文件夹路径
        # dirs 表示该文件夹下的子目录名list
        # files 表示该文件夹下的文件list
        # 遍历文件
        for f in files:
            # 增加对于后缀的判断
            """
            txt
            sln
            gif
            ico
            jpg
            cs
            csproj
            """
            if f.endswith('.txt') \
                    or f.endswith('.sln') \
                    or f.endswith('.gif') \
                    or f.endswith('.ico') \
                    or f.endswith('.jpg')\
                    or f.endswith('.cs')\
                    or f.endswith('.csproj'):
                index = index + 1
                file_path = os.path.join(root, f)
                # 2020年10月9日15:14:46 修改这一行是为了解决当前python改名字加密的问题
                # new_file_name = os.path.splitext(file_path)[0]+'.tx'
                new_file_name = file_path + '.tx'
                new_file_path = os.path.join(root, new_file_name)
                print(f'{index:0>5d} 文件:{file_path} ==> {new_file_name}')

                # 在文件名上加引号可以解决空格引起的路径错误问题
                os.popen(f'copy "{file_path}" "{new_file_path}"')

                while True:
                    # 需在这里判断一下文件是否复制结束，结束了再开始重命名
                    if os.path.exists(new_file_path):
                        os.remove(file_path)
                        # os.rename(new_file_path, file_path)
                        break
                    else:
                        time.sleep(1)


def change_postfix(x_target_path):
    pass


def get_all_postfix(x_target_path):
    # 获取所有的后缀
    postfix = []
    for root, dirs, files in os.walk(x_target_path):

        for f in files:
            str_info = f.split('.')
            if len(str_info) > 1:
                postfix.append(str_info[-1])
    # 去重
    postfix = list(set(postfix))
    print(postfix)


if __name__ == '__main__':
    target_path = "D:\\unlock"
    # get_all_postfix(target_path)
    unlock(target_path)


