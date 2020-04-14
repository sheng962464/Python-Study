import struct
import numpy as np
import BaseTransfer
from copy import deepcopy


class point:
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
        assert isinstance(other, point)
        return point(self.__x + other.__x, self.__y + other.__y, self.__z + other.__z)

    def __sub__(self, other):
        assert isinstance(other, point)
        return point(self.__x - other.__x, self.__y - other.__y, self.__z - other.__z)

    def __mul__(self, other):
        assert isinstance(other, (int, float))
        return point(self.__x * other, self.__y * other, self.__z * other)

    def __truediv__(self, other):
        assert isinstance(other, (int, float)) and other
        return point(self.__x / other, self.__y / other, self.__z / other)

    def __str__(self):
        return f'({self.__x},{self.__y},{self.__z})'

    def __len__(self):
        return len(self.to_array())

    def save(self, x_file_path):
        with open(x_file_path, 'w') as x_file:
            print(f'{self.__x},{self.__y},{self.__z}', file=x_file)

    def to_array(self):
        return np.array([self.__x, self.__y, self.__z])

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

    def to_point_2d(self):
        """
        Z向投影，返回平面的2D点
        """
        return point_2D(self.__x, self.__y)


class point_2D:
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
        assert isinstance(other, point_2D)
        return point_2D(self.__x + other.__x, self.__y + other.__y)

    def __sub__(self, other):
        assert isinstance(other, point_2D)
        return point_2D(self.__x - other.__x, self.__y - other.__y)

    def __mul__(self, other):
        assert isinstance(other, (int, float))
        return point_2D(self.__x * other, self.__y * other)

    def __truediv__(self, other):
        assert isinstance(other, (int, float)) and other
        return point_2D(self.__x / other, self.__y / other)

    def __str__(self):
        return f'({self.__x},{self.__y})'

    def __len__(self):
        return len(self.to_array())

    def save(self, x_file_path):
        with open(x_file_path, 'w') as x_file:
            print(f'{self.__x},{self.__y}', file=x_file)

    def to_array(self):
        return np.array([self.__x, self.__y])

    def to_norm(self):
        """
        计算 (x,y) / sqrt(x*x + y*y)
        """
        point_array = self / self.norm()
        return point_array

    def norm(self):
        """
        计算 sqrt(x*x + y*y)
        """
        return np.linalg.norm(self.to_array())


class line:
    """
    直线的参数方程：
    x = m1 + v1 * t
    y = m2 + v2 * t
    z = m3 + v3 * t
    其中(m1,m2,m3)为直线上的点，(v1,v2,v3)为直线的方向向量
    """

    def __init__(self, xorigin=point(0, 0, 0), xdirection=point(0, 0, 1)):
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

    def save(self):
        pass


class plane:
    """
    面的点法式方程：
    vp1 * (x-n1) + vp2 * (y-n2) + vp3 * (z-n3) = 0
    """

    def __init__(self, xorigin=point(0, 0, 0), xvector=point(0, 0, 1)):
        self.origin = deepcopy(xorigin)
        self.vector = deepcopy(xvector)

    def __str__(self):
        return f'origin:{self.origin},vector:{self.vector}'

    def save(self):
        pass


class sensor:
    """
    传感器的本质为射线的集合
    点数，点间隔，安装角度，安装位置
    """

    def __init__(self, x_point_num=1500, x_point_interval=0.001, x_fix_angle=(0, 0, 0), x_location=(0, 0, 0)):
        self.__pointNum = x_point_num
        self.__pointInterval = x_point_interval
        self.__fixAngle = x_fix_angle
        self.__location = np.array(x_location)
        self.__laser_vector = [0, 0, -1]

        self.laser = None
        self.sensor_calculation()

    def sensor_calculation(self):
        self.__laser_vector = np.dot(BaseTransfer.euler_angle_to_matrix(self.__fixAngle), np.array(self.__laser_vector))
        temp_trig_point = [self.__location + np.array([i * self.__pointInterval, 0, 0])
                           for i in range(-self.__pointNum // 2, self.__pointNum // 2)]
        self.laser = [line(xorigin=point(*x), xdirection=point(*self.__laser_vector)) for x in temp_trig_point]

    def sensor_absolute_move(self, x_location):
        # 绝对移动
        self.__location = x_location
        self.sensor_calculation()
        print(f'移动到{self.__location}位置')

    def sensor_relative_move(self):
        pass

    def save(self, x_path):
        with open(x_path, 'w') as f:
            for x in self.laser:
                print(x, file=f)

    def __str__(self):
        for x in self.laser:
            print(x)
        return f'传感器输出结束,共{len(self.laser)}条激光线'


class model:
    def __init__(self):
        pass

    def save(self):
        pass


class triangle_2D:
    def __init__(self, x_vertex1=point_2D(0, 0), x_vertex2=point_2D(0, 0), x_vertex3=point_2D(0, 0)):
        assert isinstance(x_vertex1, point_2D) and isinstance(x_vertex2, point_2D) and isinstance(x_vertex3, point_2D)
        self.__vertex1 = deepcopy(x_vertex1)
        self.__vertex2 = deepcopy(x_vertex2)
        self.__vertex3 = deepcopy(x_vertex3)

    @property
    def vertex1(self):
        return self.__vertex1

    @property
    def vertex2(self):
        return self.__vertex2

    @property
    def vertex3(self):
        return self.__vertex3

    @vertex1.setter
    def vertex1(self, x_vertex1):
        self.__vertex1 = deepcopy(x_vertex1)

    @vertex2.setter
    def vertex2(self, x_vertex2):
        self.__vertex2 = deepcopy(x_vertex2)

    @vertex3.setter
    def vertex3(self, x_vertex3):
        self.__vertex3 = deepcopy(x_vertex3)

    def __str__(self):
        return f'{self.__vertex1},{self.__vertex2},{self.__vertex3}'


class triangle:
    def __init__(self, x_vertex1=point(0, 0, 0), x_vertex2=point(0, 0, 0), x_vertex3=point(0, 0, 0)):
        assert isinstance(x_vertex1, point) and isinstance(x_vertex2, point) and isinstance(x_vertex3, point)
        self.__vertex1 = deepcopy(x_vertex1)
        self.__vertex2 = deepcopy(x_vertex2)
        self.__vertex3 = deepcopy(x_vertex3)

    @property
    def vertex1(self):
        return self.__vertex1

    @property
    def vertex2(self):
        return self.__vertex2

    @property
    def vertex3(self):
        return self.__vertex3

    @vertex1.setter
    def vertex1(self, x_vertex1):
        self.__vertex1 = deepcopy(x_vertex1)

    @vertex2.setter
    def vertex2(self, x_vertex2):
        self.__vertex2 = deepcopy(x_vertex2)

    @vertex3.setter
    def vertex3(self, x_vertex3):
        self.__vertex3 = deepcopy(x_vertex3)

    def to_triangle_2d(self):
        return triangle_2D(self.__vertex1.to_point_2d(), self.__vertex2.to_point_2d(), self.__vertex3.to_point_2d())

    def centroid(self):
        """
        计算三角形的质心，三个点的平均值
        """
        return (self.__vertex1 + self.__vertex2 + self.__vertex3) / 3

    def area(self):
        # 向量AB
        vector_ab = self.__vertex2 - self.__vertex1
        # 向量AC
        vector_ac = self.__vertex3 - self.__vertex1
        # 向量AB叉乘向量AC
        # | i  j  k |
        # |x1 y1 z1 |
        # |x2 y2 z2 |
        # (y1*z2-y2*z1, x2*z1-x1*z2, x1*y2-x2*y1)
        cross_abc = np.cross(np.array(vector_ab.to_array()), np.array(vector_ac.to_array()))
        triangle_area = np.sqrt(
            cross_abc[0] * cross_abc[0] + cross_abc[1] * cross_abc[1] + cross_abc[2] * cross_abc[2]) / 2
        return triangle_area

    def is_in_triangle(self, x_point):
        # 判断点是否在三角形内部
        # 通过面积的方式来判断，当点xPoint内部时，四个三角形的面积加起来是相等的
        triangle_1 = triangle(x_point, self.__vertex2, self.__vertex3)
        triangle_2 = triangle(self.__vertex1, x_point, self.__vertex3)
        triangle_3 = triangle(self.__vertex1, self.__vertex2, x_point)
        area1 = self.area()
        area2 = triangle_1.area()
        area3 = triangle_2.area()
        area4 = triangle_3.area()
        area_all = area2 + area3 + area4
        if abs(area_all - area1) < area1 / 100:
            return True
        return False

    def __str__(self):
        return f'{self.__vertex1},{self.__vertex2},{self.__vertex3}'


class triangle_slice:
    def __init__(self, x_facet=point(), x_vertex=triangle()):
        """
        三角面片初始化函数
        :param x_facet: 法向量
        :param x_vertex: 顶点(3个)
        """
        self.__facet = deepcopy(x_facet)
        self.__vertex = deepcopy(x_vertex)

    @property
    def facet(self):
        return self.__facet

    @property
    def vertex(self):
        return self.__vertex

    @facet.setter
    def facet(self, x_facet):
        self.__facet = deepcopy(x_facet)

    @vertex.setter
    def vertex(self, x_vertex):
        self.__vertex = deepcopy(x_vertex)

    def __str__(self):
        return f'facet: {self.__facet}, vertex: {self.__vertex}'


class STLModel:
    """
    STL模型类
    可以增加一个STL法向量修复的函数，因为模型的法向量可能会出错
    """
    def __init__(self, x_tri_list):
        """
        STL模型初始化
        :param x_tri_list: 三角面列表
        """
        self.__tri_list = deepcopy(x_tri_list)  # type: list

    @property
    def tri_list(self):
        return self.__tri_list

    @tri_list.setter
    def tri_list(self, x_tri_list):
        self.__tri_list = deepcopy(x_tri_list)

    @classmethod
    def read_stl(cls, x_path):
        """
        从二进制文件中解析STL模型

        :param x_path: 文件路径
        :return: STL模型
        """
        list_tri_slice = cls.load_binary(x_path)
        return STLModel(list_tri_slice)

    ###################
    # region STL读取函数
    @classmethod
    def load_binary(cls, str_path):
        """
        读取STL二进制文件

        :param str_path:
        :return:
        """
        list_triangle_slice = []
        with open(str_path, 'rb') as f:
            f.read(80)  # 流出80字节，文件名
            temp = f.read(4)  # 流出4字节，文件中结构体的数量
            count = struct.unpack('I', temp)[0]
            for i in range(count):
                list_triangle_slice.append(cls.triangle_slice_read(f))
        return list_triangle_slice

    @classmethod
    def triangle_slice_read(cls, f):
        """
        从字节流中读取三角片

        :param f:
        :return:
        """
        tri_slice = triangle_slice()
        tri_slice.facet = cls.point_read(f)
        tri_slice.vertex.vertex1 = cls.point_read(f)
        tri_slice.vertex.vertex2 = cls.point_read(f)
        tri_slice.vertex.vertex3 = cls.point_read(f)
        f.read(2)
        return tri_slice

    @classmethod
    def point_read(cls, f):
        """
        从字节流中读取点(32位无符号整数，每次读取4个字节)

        :param f:
        :return:
        """
        xpoint = point()
        xpoint.x = struct.unpack('f', f.read(4))[0]
        xpoint.y = struct.unpack('f', f.read(4))[0]
        xpoint.z = struct.unpack('f', f.read(4))[0]
        return xpoint

    # endregion
    ###################

    def __len__(self):
        return len(self.__tri_list)

    def __getitem__(self, x_item):
        return self.__tri_list[x_item]

    def __str__(self):
        print('三角面片开始显示')
        for i, x in enumerate(self.__tri_list):
            print(i, ':', x)
        return '三角面片显示结束'

    def save(self, x_path):
        with open(x_path, 'w') as f:
            print('solid Mesh', file=f)
            for x in self.__tri_list:
                print(f'facet normal {x.facet.x:.6e} {x.facet.y:.6e} {x.facet.z:.6e}', file=f)
                print(f'outer loop', file=f)
                print(f'vertex {x.vertex.vertex1.x:.6e} {x.vertex.vertex1.y:.6e} {x.vertex.vertex1.z:.6e}', file=f)
                print(f'vertex {x.vertex.vertex2.x:.6e} {x.vertex.vertex2.y:.6e} {x.vertex.vertex2.z:.6e}', file=f)
                print(f'vertex {x.vertex.vertex3.x:.6e} {x.vertex.vertex3.y:.6e} {x.vertex.vertex3.z:.6e}', file=f)
                print(f'endloop', file=f)
                print(f'endfacet', file=f)
            print('endsolid Mesh', file=f)
        print('STL文件保存结束：成功')
        return


def test_unit():
    pass

    import os
    save_folder = r"D:\全局标定测试"

    # # region 测试point类
    # m_point = point(*[0, 2, 0])
    # print('测试print函数：', m_point)
    # print('测试点加法：', m_point + point(1, 1, 1))
    # print('测试点减法：', m_point - point(1, 1, 1))
    # save_point_path = os.path.join(save_folder, 'point.txt')
    # m_point.save(save_point_path)
    # print(f'测试点保存：{save_point_path}')
    # print('测试点归一化:', m_point.to_norm())
    # # endregion 测试point类

    # # region 测试line类
    # m_line = line()
    # print('测试print函数：', m_line)
    # print(m_line.direction)
    # print(type(m_line.direction))
    # # endregion 测试line类

    # # region 测试plane类
    # m_plane = plane()
    # print('测试print函数：', m_plane)
    # # endregion 测试plane类

    # region 测试sensor类
    m_sensor = sensor(x_fix_angle=(0, 0, 1))
    m_sensor.sensor_absolute_move([0, 1, 1])
    print(m_sensor)
    save_point_path = os.path.join(save_folder, 'sensor.txt')
    m_sensor.save(save_point_path)
    # endregion

    # # region 测试STL类
    # m_stl_model = STLModel.read_stl(r'D:\全局标定测试\单层NEY模型.stl')
    # m_stl_model.save(r'D:\全局标定测试\单层NEY模型-111.stl')
    # # endregion


if __name__ == '__main__':
    test_unit()
