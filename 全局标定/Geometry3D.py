from copy import deepcopy

import numpy as np


class Point2D:
    def __init__(self, mx=0.0, my=0.0):
        self.x = mx
        self.y = my

    def __add__(self, other):
        """
        点加向量表示平移
        @param other:
        @return:
        """
        if isinstance(other, Vector2D):
            return Point2D(self.x + other.i, self.y + other.j)
        else:
            return None

    def __sub__(self, other):
        """
        点减向量表示平移,点点相减表示向量
        @param other:
        @return:
        """
        if isinstance(other, Vector2D):
            return Point2D(self.x - other.i, self.y - other.j)
        elif isinstance(other, Point2D):
            return Vector2D(self.x - other.x, self.y - other.y)
        else:
            return None

    def __str__(self):
        return f'({self.x:.3f},{self.y:.3f})'

    def to_array(self):
        """
        点转化为numpy数组
        """
        return np.array([self.x, self.y])


class Vector2D:
    def __init__(self, mi=0.0, mj=0.0):
        self.i = mi
        self.j = mj

    def __add__(self, other):
        """
        向量相加
        @param other:
        @return:
        """
        if isinstance(other, Vector2D):
            return Vector2D(self.i + other.i, self.j + other.j)
        else:
            return None

    def __sub__(self, other):
        """
        向量相减
        @param other:
        @return:
        """
        if isinstance(other, Vector2D):
            return Vector2D(self.i + other.i, self.j + other.j)
        else:
            return None

    def __mul__(self, other):
        """
        向量缩放
        @param other:
        @return:
        """
        if isinstance(other, (int, float)):
            return Vector2D(self.i * other, self.j * other)
        else:
            return None

    def __truediv__(self, other):
        """
        向量缩放
        @param other:
        @return:
        """
        if isinstance(other, (int, float)) and other:
            return Vector2D(self.i * other, self.j * other)
        else:
            return None

    def __str__(self):
        return f'({self.i:.3f},{self.j:.3f})'

    def to_array(self):
        """
        转化为numpy数组
        @return:
        """
        return np.array([self.i, self.j])

    def length(self):
        """
        向量长度
        @return:
        """
        return np.sqrt(self.i ** 2 + self.j ** 2)

    def normalize(self):
        """
        向量归一化
        @return:
        """
        length = self.length()
        return self / length


class Point3D:
    def __init__(self, mx=0.0, my=0.0, mz=0.0):
        self.x = mx
        self.y = my
        self.z = mz

    def __add__(self, other):
        """
        点加向量表示平移
        @param other:
        @return:
        """
        if isinstance(other, Vector3D):
            return Point3D(self.x + other.i, self.y + other.j, self.z + other.k)
        else:
            return None

    def __sub__(self, other):
        """
        点减向量表示平移,点点相减表示向量
        @param other:
        @return:
        """
        if isinstance(other, Vector3D):
            return Point3D(self.x - other.i, self.y - other.j, self.z - other.k)
        elif isinstance(other, Point3D):
            return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)
        else:
            return None

    def __str__(self):
        return f'({self.x:.3f},{self.y:.3f},{self.z:.3f})'

    def to_array(self):
        """
        点转化为numpy数组
        """
        return np.array([self.x, self.y, self.z])


class Vector3D:
    def __init__(self, mi=0.0, mj=0.0, mk=0.0):
        self.i = mi
        self.j = mj
        self.k = mk

    def __add__(self, other):
        """
        向量相加后仍为一个向量
        @param other:
        @return:
        """
        if isinstance(other, Vector3D):
            return Vector3D(self.i + other.i, self.j + other.j, self.k + other.k)
        else:
            return None

    def __sub__(self, other):
        """
        向量相减后仍为一个向量
        @param other:
        @return:
        """
        if isinstance(other, Vector3D):
            return Vector3D(self.i - other.i, self.j - other.j, self.k - other.k)
        else:
            return None

    def __mul__(self, other):
        """
        向量缩放
        @param other:
        @return:
        """
        if isinstance(other, (int, float)):
            return Vector3D(self.i * other, self.j * other, self.k * other)
        else:
            return None

    def __truediv__(self, other):
        """
        向量缩放
        @param other:
        @return:
        """
        if isinstance(other, (int, float)) and other:
            return Vector3D(self.i * other, self.j * other, self.k * other)
        else:
            return None

    def __str__(self):
        return f'({self.i:.3f},{self.j:.3f},{self.k:.3f})'

    def to_array(self):
        """
        转换为numpy数组
        @return:
        """
        return np.array([self.i, self.j, self.k])

    def length(self):
        """
        向量长度
        @return:
        """
        return np.sqrt(self.i ** 2 + self.j ** 2 + self.k ** 2)

    def normalize(self):
        """
        向量归一化
        @return:
        """
        length = self.length()
        return self / length


class Line2D:
    def __init__(self, m_begin_point=Point2D(0, 0), m_end_point=Point2D(0, 0)):
        self.begin = deepcopy(m_begin_point)
        self.end = deepcopy(m_end_point)

    def __str__(self):
        return f'begin point:{self.begin},end point:{self.end}'

    def direction(self) -> Vector2D:
        """
        直线的方向
        @return:
        """
        return (self.end - self.begin).normalize()

    def get_point_from_t(self, m_t) -> Point2D:
        """
        根据参数值，获取直线上的点
        """
        return self.begin + self.direction() * m_t


class Line3D:
    def __init__(self, m_begin_point=Point3D(0, 0, 0), m_end_point=Point3D(0, 0, 1)):
        self.begin = deepcopy(m_begin_point)
        self.end = deepcopy(m_end_point)

    def __str__(self):
        return f'begin point:{self.begin},end point:{self.end}'

    def direction(self) -> Vector3D:
        """
        直线的方向
        @return:
        """
        return (self.end - self.begin).normalize()

    def get_point_from_t(self, m_t) -> Point3D:
        """
        根据参数值，获取直线上的点
        """
        return self.begin + self.direction() * m_t


class Plane:
    def __init__(self, m_origin=Point3D(0, 0, 0), m_vector=Vector3D(0, 0, 1)):
        self.origin = deepcopy(m_origin)
        self.vector = deepcopy(m_vector.normalize())

    def __str__(self):
        return f'origin:{self.origin},vector:{self.vector}'


class Sphere:
    def __init__(self, m_center=Point3D(0, 0, 0), m_radius=1):
        self.center = deepcopy(m_center)
        self.radius = m_radius

    def __str__(self):
        return f'center:{self.center},radius:{self.radius}'
