from POINT3D import POINT3D
from copy import deepcopy


class LINE3D:
    """
    直线的参数方程：
    x = m1 + v1 * t
    y = m2 + v2 * t
    z = m3 + v3 * t
    其中(m1,m2,m3)为直线上的点，(v1,v2,v3)为直线的方向向量
    """

    def __init__(self, xorigin=POINT3D(0, 0, 0), xdirection=POINT3D(0, 0, 1)):
        self.__origin = deepcopy(xorigin)
        self.__direction = deepcopy(xdirection)

    def __str__(self):
        return f'origin:{self.__origin},direction:{self.__direction}'

    @property
    def origin(self):
        return self.__origin

    @property
    def direction(self):
        return self.__direction

    @origin.setter
    def origin(self, x_origin):
        self.__origin = x_origin

    @direction.setter
    def direction(self, x_direction):
        self.__direction = x_direction

    def get_point_from_t(self, x_t):
        """
        根据参数值，获取直线上的点
        """
        return self.__origin + self.__direction * x_t

    def start_point(self):
        """
        直线的起始点，记为参数为0的点
        @return:
        """
        return self.get_point_from_t(0)

    def end_point(self):
        """
        直线的终止点，记为参数为100的点
        @return:
        """
        return self.get_point_from_t(100)

    def save(self, x_file_path, x_length=100000, x_step=0.001):
        with open(x_file_path, 'w') as f:
            for i in range(x_length):
                i -= x_length / 2
                m_point = self.get_point_from_t(i * x_step)
                print(f'{m_point.x},{m_point.y},{m_point.z}', file=f)


def test_unit():
    import os
    save_folder = r"D:\全局标定测试\测试单元"
    save_file = os.path.join(save_folder, "test-LINE2D.txt")

    origin_line_1 = POINT3D(0, 0, 0)
    direction_line_1 = POINT3D(1, 0, 0)
    test_line_1 = LINE3D(origin_line_1, direction_line_1)

    print(f"测试print:直线为{test_line_1}")
    origin_line_1.x = 2
    print(f"测试print:直线为{test_line_1}")
    print(f"测试start_point：起始点为{test_line_1.start_point()}")
    print(f"测试end_point：结束点为{test_line_1.end_point()}")
    test_line_1.save(save_file)
    print(f"测试save：{save_file} - success")


if __name__ == '__main__':
    test_unit()
