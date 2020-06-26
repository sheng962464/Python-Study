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
            if f.endswith('.png') or f.endswith('.jpg') or f.endswith('.h') or f.endswith('.cs') or f.endswith('.txt'):
                index = index + 1
                file_path = os.path.join(root, f)
                new_file_name = os.path.splitext(file_path)[0]+'.tx'
                new_file_path = os.path.join(root, new_file_name)

                print(f'{index:0>5d} 文件:{file_path} ==> {new_file_name}')

                # 在文件名上加引号可以解决空格引起的路径错误问题
                os.popen(f'copy "{file_path}" "{new_file_path}"')
                # 需在这里判断一下文件是否复制结束，结束了再开始重命名
                while True:
                    if os.path.exists(new_file_path):
                        os.remove(file_path)
                        os.rename(new_file_path, file_path)
                        break
                    else:
                        time.sleep(1)


if __name__ == '__main__':
    target_path = "D:\\unlock"
    unlock(target_path)
