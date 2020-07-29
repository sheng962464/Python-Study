import struct
import numpy as np
import BaseTransfer
import random
from copy import deepcopy


class Point3D:
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
        assert isinstance(other, Point3D)
        return Point3D(self.__x + other.__x, self.__y + other.__y, self.__z + other.__z)

    def __sub__(self, other):
        assert isinstance(other, Point3D)
        return Point3D(self.__x - other.__x, self.__y - other.__y, self.__z - other.__z)

    def __mul__(self, other):
        assert isinstance(other, (int, float))
        return Point3D(self.__x * other, self.__y * other, self.__z * other)

    def __truediv__(self, other):
        assert isinstance(other, (int, float)) and other
        return Point3D(self.__x / other, self.__y / other, self.__z / other)

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
        return Point2D(self.__x, self.__y)


class Point2D:
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
        assert isinstance(other, Point2D)
        return Point2D(self.__x + other.__x, self.__y + other.__y)

    def __sub__(self, other):
        assert isinstance(other, Point2D)
        return Point2D(self.__x - other.__x, self.__y - other.__y)

    def __mul__(self, other):
        assert isinstance(other, (int, float))
        return Point2D(self.__x * other, self.__y * other)

    def __truediv__(self, other):
        assert isinstance(other, (int, float)) and other
        return Point2D(self.__x / other, self.__y / other)

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
        return float(np.linalg.norm(self.to_array()))


class Line3D:
    """
    直线的参数方程：
    x = m1 + v1 * t
    y = m2 + v2 * t
    z = m3 + v3 * t
    其中(m1,m2,m3)为直线上的点，(v1,v2,v3)为直线的方向向量
    """

    def __init__(self, xorigin=Point3D(0, 0, 0), xdirection=Point3D(0, 0, 1)):
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
        return self.get_point_from_t(0)

    def end_point(self):
        return self.get_point_from_t(100)

    def save(self, x_file_path, x_length=1000, x_step=0.1):
        with open(x_file_path, 'w') as f:
            for i in range(x_length):
                i -= x_length / 2
                m_point = self.get_point_from_t(i * x_step)
                print(f'{m_point.x},{m_point.y},{m_point.z}', file=f)


class Plane:
    """
    面的点法式方程：
    vp1 * (x-n1) + vp2 * (y-n2) + vp3 * (z-n3) = 0
    """

    def __init__(self, xorigin=Point3D(0, 0, 0), xvector=Point3D(0, 0, 1)):
        self.origin = deepcopy(xorigin)
        self.vector = deepcopy(xvector)

    def __str__(self):
        return f'origin:{self.origin},vector:{self.vector}'

    def save(self, x_file_path):
        # 生成大小为100*100的XY平面，然后旋转到当前法向量，保存
        list_of_point = []
        for xx in range(-50, 50):
            for yy in range(-50, 50):
                list_of_point.append(Point3D(xx, yy, 0))
        old_vector = Point3D(0, 0, 1)
        x_theta = np.arccos(np.dot(old_vector.to_array(), self.vector.to_array()) / (old_vector.norm() * self.vector.norm()))
        if x_theta < 1e-5:
            with open(x_file_path, 'w') as f:
                for x_point in list_of_point:
                    print(f'{x_point.x},{x_point.y},{x_point.z}', file=f)
        else:
            a1, b1, c1 = old_vector.to_array()
            a2, b2, c2 = self.vector.to_array()
            x_axis = Point3D(b1 * c2 - b2 * c1, c1 * a2 - a1 * c2, a1 * b2 - a2 * b1).to_norm()
            x_matrix = BaseTransfer.Rodrigues((x_axis * x_theta).to_array())
            with open(x_file_path, 'w') as f:
                for x_point in list_of_point:
                    new_point_array = np.dot(x_matrix, x_point.to_array()) + self.origin.to_array()
                    print(f'{new_point_array[0]},{new_point_array[1]},{new_point_array[2]}', file=f)


class Sphere:
    def __init__(self, xcenter=Point3D(0, 0, 0), xr=1):
        self.center = deepcopy(xcenter)
        self.r = xr

    def __str__(self):
        return f'center:{self.center},r:{self.r}'

    def save(self, x_file_path):
        list_of_point = []
        for i in range(int(10000 * self.r)):
            xx = random.normalvariate(0, 1)
            xy = random.normalvariate(0, 1)
            xz = random.normalvariate(0, 1)
            xr = (xx * xx + xy * xy + xz * xz) ** (1 / 2)
            list_of_point.append(Point3D(xx / xr * self.r, xy / xr * self.r, xz / xr * self.r) + self.center)
        with open(x_file_path, 'w') as f:
            for x_point in list_of_point:
                print(f'{x_point.x},{x_point.y},{x_point.z}', file=f)


class Sensor:
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
        self.laser = [Line3D(xorigin=Point3D(*x), xdirection=Point3D(*self.__laser_vector)) for x in temp_trig_point]

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


class Triangle2D:
    def __init__(self, x_vertex1=Point2D(0, 0), x_vertex2=Point2D(0, 0), x_vertex3=Point2D(0, 0)):
        assert isinstance(x_vertex1, Point2D) and isinstance(x_vertex2, Point2D) and isinstance(x_vertex3, Point2D)
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

    def get_box_2d(self):
        x_min = min([self.__vertex1.x, self.__vertex2.x, self.__vertex3.x])
        x_max = max([self.__vertex1.x, self.__vertex2.x, self.__vertex3.x])
        y_min = min([self.__vertex1.y, self.__vertex2.y, self.__vertex3.y])
        y_max = max([self.__vertex1.y, self.__vertex2.y, self.__vertex3.y])
        return Box2D(x_min, x_max, y_min, y_max)

    def __str__(self):
        return f'{self.__vertex1},{self.__vertex2},{self.__vertex3}'


class Triangle3D:
    def __init__(self, x_vertex1=Point3D(0, 0, 0), x_vertex2=Point3D(0, 0, 0), x_vertex3=Point3D(0, 0, 0)):
        assert isinstance(x_vertex1, Point3D) and isinstance(x_vertex2, Point3D) and isinstance(x_vertex3, Point3D)
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
        return Triangle2D(self.__vertex1.to_point_2d(), self.__vertex2.to_point_2d(), self.__vertex3.to_point_2d())

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

    def get_box_3d(self):
        x_min = min([self.__vertex1.x, self.__vertex2.x, self.__vertex3.x])
        x_max = max([self.__vertex1.x, self.__vertex2.x, self.__vertex3.x])
        y_min = min([self.__vertex1.y, self.__vertex2.y, self.__vertex3.y])
        y_max = max([self.__vertex1.y, self.__vertex2.y, self.__vertex3.y])
        z_min = min([self.__vertex1.z, self.__vertex2.z, self.__vertex3.z])
        z_max = max([self.__vertex1.z, self.__vertex2.z, self.__vertex3.z])
        return Box3D(x_min, x_max, y_min, y_max, z_min, z_max)

    def __str__(self):
        return f'{self.__vertex1},{self.__vertex2},{self.__vertex3}'


class TriangleSlice:
    def __init__(self, x_facet=Point3D(), x_vertex=Triangle3D()):
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

    def mesh_init(self):
        # 三角面片初始化，重新计算三角面片的法向量
        v1, v2, v3 = self.__vertex.vertex1, self.__vertex.vertex2, self.__vertex.vertex3
        nx = (v1.y - v3.y) * (v2.z - v3.z) - (v1.z - v3.z) * (v2.y - v3.y)
        ny = (v1.z - v3.z) * (v2.x - v3.x) - (v2.z - v3.z) * (v1.x - v3.x)
        nz = (v1.x - v3.x) * (v2.y - v3.y) - (v2.x - v3.x) * (v1.y - v3.y)
        self.__facet = Point3D(nx, ny, nz)

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
        tri_slice = TriangleSlice()
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
        xpoint = Point3D()
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
        """
        使用ASCII格式保存三角化模型
        @param x_path: 保存路径
        @return:
        """
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
        print('STL(ASCII)文件保存结束：成功')
        return

    def model_init(self):
        # 对模型的三角面片的法向量进行初始化，防止法向量出错
        for xx in self:  # type:TriangleSlice
            xx.mesh_init()


class Box2D:
    def __init__(self, x_min, x_max, y_min, y_max):
        """
        设定 Box2D 的范围
        """
        self.__x_min = x_min
        self.__x_max = x_max
        self.__y_min = y_min
        self.__y_max = y_max

    @property
    def x_max(self):
        return self.__x_max

    @property
    def x_min(self):
        return self.__x_min

    @property
    def y_max(self):
        return self.__y_max

    @property
    def y_min(self):
        return self.__y_min

    @x_max.setter
    def x_max(self, xx):
        self.__x_max = xx

    @x_min.setter
    def x_min(self, xx):
        self.__x_min = xx

    @y_max.setter
    def y_max(self, xy):
        self.__y_max = xy

    @y_min.setter
    def y_min(self, xy):
        self.__y_min = xy

    def __str__(self):
        return f' x_min = {self.__x_min:.3f}    x_max = {self.__x_max:.3f}\n' \
               f' y_min = {self.__y_min:.3f}    y_max = {self.__y_max:.3f}'


class Box3D:
    def __init__(self, x_min, x_max, y_min, y_max, z_min, z_max):
        """
        设定 Box3D 的范围
        """
        self.__x_min = x_min
        self.__x_max = x_max
        self.__y_min = y_min
        self.__y_max = y_max
        self.__z_min = z_min
        self.__z_max = z_max

    @property
    def x_max(self):
        return self.__x_max

    @property
    def x_min(self):
        return self.__x_min

    @property
    def y_max(self):
        return self.__y_max

    @property
    def y_min(self):
        return self.__y_min

    @property
    def z_max(self):
        return self.__z_max

    @property
    def z_min(self):
        return self.__z_min

    @x_max.setter
    def x_max(self, xx):
        self.__x_max = xx

    @x_min.setter
    def x_min(self, xx):
        self.__x_min = xx

    @y_max.setter
    def y_max(self, xy):
        self.__y_max = xy

    @y_min.setter
    def y_min(self, xy):
        self.__y_min = xy

    @z_max.setter
    def z_max(self, xz):
        self.__z_max = xz

    @z_min.setter
    def z_min(self, xz):
        self.__z_min = xz

    def __str__(self):
        return f' x_min = {self.__x_min:.3f}    x_max = {self.__x_max:.3f}\n' \
               f' y_min = {self.__y_min:.3f}    y_max = {self.__y_max:.3f}\n' \
               f' z_min = {self.__z_min:.3f}    z_max = {self.__z_max:.3f}'


def test_unit():
    pass

    import os
    save_folder = r"D:\全局标定测试"

    # # region 测试point类
    # m_point = Point3D(*[0, 2, 0])
    # print('测试print函数：', m_point)
    # print('测试点加法：', m_point + Point3D(1, 1, 1))
    # print('测试点减法：', m_point - Point3D(1, 1, 1))
    # save_point_path = os.path.join(save_folder, 'Point3D.txt')
    # m_point.save(save_point_path)
    # print(f'测试点保存：{save_point_path}')
    # print('测试点归一化:', m_point.to_norm())
    # # endregion 测试point类

    # # region 测试line类
    # m_line = Line3D()
    # print('测试print函数：', m_line)
    # print(m_line.direction)
    # print(type(m_line.direction))
    # save_line_path = os.path.join(save_folder, 'Line3D.txt')
    # m_line.save(save_line_path)
    # # endregion 测试line类

    # # region 测试plane类
    # m_plane = Plane(xorigin=Point3D(0, 0, 0), xvector=Point3D(0, 0, 1))
    # print('测试print函数：', m_plane)
    # save_plane_path = os.path.join(save_folder, 'Plane3D.txt')
    # m_plane.save(save_plane_path)
    # # endregion 测试plane类

    # region 测试sphere类
    m_sphere = Sphere(xcenter=Point3D(0, 0, 0), xr=1)
    print('测试print函数：', m_sphere)
    save_sphere_path = os.path.join(save_folder, 'Sphere.txt')
    m_sphere.save(save_sphere_path)
    # endregion 测试plane类

    # # region 测试sensor类
    # m_sensor = Sensor(x_fix_angle=(0, 0, 1))
    # m_sensor.sensor_absolute_move([0, 1, 1])
    # print(m_sensor)
    # save_point_path = os.path.join(save_folder, 'Sensor.txt')
    # m_sensor.save(save_point_path)
    # # endregion

    # # region 测试STL类
    # m_stl_model = STLModel.read_stl(r'D:\OPPO中框.stl')
    # print(f'共{len(m_stl_model)}个三角面片')
    # m_stl_model.save(r'D:\全局标定测试\单层NEY模型-111.stl')
    # # endregion

    # # region 测试box_2D类
    # m_triangle_2d = Triangle2D(Point2D(0, 0), Point2D(1, 0), Point2D(0, 1))
    # m_box = m_triangle_2d.get_box_2d()
    # print(f'盒子的范围为：\n{m_box}')
    # # endregion

    # # region 测试box_3D类
    # m_triangle_3d = Triangle3D(Point3D(0, 0, 0), Point3D(1, 0, 0), Point3D(0, 1, 0))
    # m_box = m_triangle_3d.get_box_3d()
    # print(f'盒子的范围为：\n{m_box}')
    # # endregion


if __name__ == '__main__':
    test_unit()
