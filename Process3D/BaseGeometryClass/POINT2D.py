import numpy as np


class POINT2D:
    def __init__(self, xx=0.0, xy=0.0):
        self.__x = xx
        self.__y = xy

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @x.setter
    def x(self, xx):
        self.__x = xx

    @y.setter
    def y(self, xy):
        self.__y = xy

    def __add__(self, other):
        assert isinstance(other, POINT2D)
        return POINT2D(self.__x + other.__x, self.__y + other.__y)

    def __sub__(self, other):
        assert isinstance(other, POINT2D)
        return POINT2D(self.__x - other.__x, self.__y - other.__y)

    def __mul__(self, other):
        assert isinstance(other, (int, float))
        return POINT2D(self.__x * other, self.__y * other)

    def __truediv__(self, other):
        assert isinstance(other, (int, float)) and other
        return POINT2D(self.__x / other, self.__y / other)

    def __str__(self):
        return f'({self.__x:.3f},{self.__y:.3f})'

    def __len__(self):
        return len(self.to_array())

    def save(self, x_file_path):
        with open(x_file_path, 'w') as x_file:
            print(f'{self.__x},{self.__y}', file=x_file)

    def to_array(self):
        """
        点转化为numpy数组
        """
        return np.array([self.__x, self.__y])

    def to_list(self):
        """
        点转化为list列表
        """
        return [self.__x, self.__y]

    def to_norm(self):
        """
        单位化，计算 (x,y) / sqrt(x*x + y*y)
        """
        point_array = self / self.norm()
        return point_array

    def norm(self):
        """
        计算 sqrt(x*x + y*y)
        """
        return float(np.linalg.norm(self.to_array()))


def test_unit():
    import os
    save_folder = r"D:\全局标定测试\测试单元"
    save_file = os.path.join(save_folder, "test-Point2D.txt")

    test_point2d_1 = POINT2D(3, 3)
    test_point2d_2 = POINT2D(1, 1)
    print(f"测试加法：{test_point2d_1} + {test_point2d_2} = {test_point2d_1 + test_point2d_2}")
    print(f"测试减法：{test_point2d_1} - {test_point2d_2} = {test_point2d_1 - test_point2d_2}")
    print(f"测试乘法：{test_point2d_1} * 2 = {test_point2d_1 * 2}")
    print(f"测试除法：{test_point2d_1} / 2 = {test_point2d_1 / 2}")
    test_point2d_1.save(save_file)
    print(f"测试save：{save_file} - success")
    array_point_1 = test_point2d_1.to_array()
    print(f"测试to_array:{array_point_1},类型{type(array_point_1)}")
    list_point_1 = test_point2d_1.to_list()
    print(f"测试to_list:{list_point_1},类型{type(list_point_1)}")
    norm_point_1 = test_point2d_1.to_norm()
    print(f"测试to_norm:{norm_point_1},类型{type(norm_point_1)}")
    norm_value = test_point2d_1.norm()
    print(f"测试norm:{norm_value},类型{type(norm_value)}")


if __name__ == '__main__':
    test_unit()
