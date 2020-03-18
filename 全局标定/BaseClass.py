import numpy as np
import numpy.matlib


class point:
    def __init__(self, xx=0.0, xy=0.0, xz=0.0):
        self.x = xx
        self.y = xy
        self.z = xz

    def __add__(self, other):
        assert isinstance(other, point)
        return point(self.x + other.x, self.y + other.y, self.z + other.y)

    def __sub__(self, other):
        assert isinstance(other, point)
        return point(self.x - other.x, self.y - other.y, self.z - other.y)

    def __str__(self):
        return f'({self.x},{self.y},{self.z})'

    def save(self, x_file_path):
        with open(x_file_path, 'w') as x_file:
            print(f'{self.x},{self.y},{self.z}', file=x_file)


class line:
    """
    直线的参数方程：
    x = m1 + v1 * t
    y = m2 + v2 * t
    z = m3 + v3 * t
    其中(m1,m2,m3)为直线上的点，(v1,v2,v3)为直线的方向向量
    """

    def __init__(self, xorigin=point(0, 0, 0), xdirection=point(0, 0, 1)):
        self.origin = xorigin
        self.direction = xdirection

    def __str__(self):
        return f'origin:{self.origin},direction:{self.direction}'

    def save(self):
        pass


class plane:
    """
    面的点法式方程：
    vp1 * (x-n1) + vp2 * (y-n2) + vp3 * (z-n3) = 0
    """

    def __init__(self, xorigin=point(0, 0, 0), xvector=point(0, 0, 1)):
        self.origin = xorigin
        self.vector = xvector

    def __str__(self):
        return f'origin:{self.origin},vector:{self.vector}'

    def save(self):
        pass


class sensor:
    """
    点数，点间隔，安装角度，安装位置
    """

    def __init__(self, x_point_num=1500, x_point_interval=0.001, x_fix_angle=(0, 0, 0), x_location=(0, 0, 0)):
        self.pointNum = x_point_num
        self.pointInterval = x_point_interval
        self.fixAngle = x_fix_angle
        self.location = x_location
        self.laser_vector = [0, 0, -1]

        self.trigPoint = (i * self.pointInterval for i in range(-x_point_num // 2, x_point_num // 2 + 1))

    def sensor_init(self):
        self.laser_vector = np.dot()

    def save(self):
        pass


class model:
    def __init__(self):
        pass

    def save(self):
        pass


def test_unit():
    import os
    save_folder = r"D:\全局标定测试"

    # # region 测试point类
    # m_point = point()
    # print('测试print函数：', m_point)
    # print('测试点加法：', m_point + point(1, 1, 1))
    # print('测试点减法：', m_point - point(1, 1, 1))
    # save_point_path = os.path.join(save_folder, 'point.txt')
    # m_point.save(save_point_path)
    # print(f'测试点保存：{save_point_path}')
    # # endregion 测试point类

    # # region 测试line类
    # m_line = line()
    # print('测试print函数：', m_line)
    # # endregion 测试line类

    # # region 测试plane类
    # m_plane = plane()
    # print('测试print函数：', m_plane)
    # # endregion 测试plane类


if __name__ == '__main__':
    test_unit()
