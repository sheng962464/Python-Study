from Class3D.Point3D import *
from Class3D.LogHelper import *


class Vector3D:
    def __init__(self, mi=0.0, mj=0.0, mk=0.0):
        self.__i = mi
        self.__j = mj
        self.__k = mk

    @property
    def i(self):
        return self.__i

    @property
    def j(self):
        return self.__j

    @property
    def k(self):
        return self.__k

    @i.setter
    def i(self, mi):
        self.__i = mi

    @j.setter
    def j(self, mj):
        self.__j = mj

    @k.setter
    def k(self, mk):
        self.__k = mk

    def __str__(self):
        return f'({self.__i},{self.__j},{self.__k})'

    @logger
    def __add__(self, other):
        """
        向量相加后仍为一个向量
        @param other:
        @return:
        """
        if isinstance(other, Vector3D):
            return Vector3D(self.__i + other.__i, self.__j + other.__j, self.__k + other.__k)
        elif isinstance(other, Point3D):
            return Point3D(self.__i + other.x, self.__j + other.y, self.__k + other.z)
        else:
            pass


if __name__ == '__main__':
    vec1 = Vector3D(1, 2, 3)
    vec2 = Vector3D(2, 3, 4)
    print(vec1 + vec2)
