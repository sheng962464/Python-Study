import numpy as np


class POINT3D:
    def __init__(self, xx=0.0, xy=0.0, xz=0.0):
        self.__x = xx
        self.__y = xy
        self.__z = xz

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def z(self):
        return self.__z

    @x.setter
    def x(self, xx):
        self.__x = xx

    @y.setter
    def y(self, xy):
        self.__y = xy

    @z.setter
    def z(self, xz):
        self.__z = xz

    def __add__(self, other):
        assert isinstance(other, POINT3D)
        return POINT3D(self.__x + other.__x, self.__y + other.__y, self.__z + other.__z)

    def __sub__(self, other):
        assert isinstance(other, POINT3D)
        return POINT3D(self.__x - other.__x, self.__y - other.__y, self.__z - other.__z)

    def __mul__(self, other):
        assert isinstance(other, (int, float))
        return POINT3D(self.__x * other, self.__y * other, self.__z * other)

    def __truediv__(self, other):
        assert isinstance(other, (int, float)) and other
        return POINT3D(self.__x / other, self.__y / other, self.__z / other)

    def __str__(self):
        return f'({self.__x:.3f},{self.__y:.3f},{self.__z:.3f})'

    def __len__(self):
        return len(self.to_array())

    def save(self, x_file_path):
        with open(x_file_path, 'w') as x_file:
            print(f'{self.__x},{self.__y},{self.__z}', file=x_file)

    def to_array(self):
        """
        点转化为numpy数组
        """
        return np.array([self.__x, self.__y, self.__z])

    def to_list(self):
        """
        点转化为list列表
        """
        return [self.__x, self.__y, self.__z]

    def to_norm(self):
        """
        计算 (x,y,z) / sqrt(x*x + y*y + z*z)
        """
        point_array = self / self.norm()
        return point_array

    def norm(self):
        """
        计算 sqrt(x*x + y*y + z*z)
        """
        return float(np.linalg.norm(self.to_array()))


def test_unit():
    import os
    save_folder = r"D:\全局标定测试\测试单元"
    save_file = os.path.join(save_folder, "test-Point3D.txt")

    test_point3d_1 = POINT3D(3, 3, 3)
    test_point3d_2 = POINT3D(1, 1, 1)
    print(f"测试加法：{test_point3d_1} + {test_point3d_2} = {test_point3d_1 + test_point3d_2}")
    print(f"测试减法：{test_point3d_1} - {test_point3d_2} = {test_point3d_1 - test_point3d_2}")
    print(f"测试乘法：{test_point3d_1} * 2 = {test_point3d_1 * 2}")
    print(f"测试除法：{test_point3d_1} / 2 = {test_point3d_1 / 2}")
    test_point3d_1.save(save_file)
    print(f"测试save：{save_file} - success")
    array_point_1 = test_point3d_1.to_array()
    print(f"测试to_array:{array_point_1},类型{type(array_point_1)}")
    list_point_1 = test_point3d_1.to_list()
    print(f"测试to_list:{list_point_1},类型{type(list_point_1)}")
    norm_point_1 = test_point3d_1.to_norm()
    print(f"测试to_norm:{norm_point_1},类型{type(norm_point_1)}")
    norm_value = test_point3d_1.norm()
    print(f"测试norm:{norm_value},类型{type(norm_value)}")


if __name__ == '__main__':
    test_unit()

