import os


def open_file_as(x_software, x_file):
    os.popen(f'"{x_software}" "{x_file}"')


if __name__ == '__main__':
    # CloudCompare的安装路径
    CloudCompare = r"C:\Program Files\CloudCompareStereo\CloudCompare.exe"
    FilePath = r'D:\全局标定测试\result.txt'
    open_file_as(CloudCompare, FilePath)
