import numpy as np
from Class3D.Vector3D import *


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
