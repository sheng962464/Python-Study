import numpy as np


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
        return Point2D(self.__x + other.__x, self.__y + other.__y)

    def __sub__(self, other):
        return Point2D(self.__x - other.__x, self.__y - other.__y)

    def __mul__(self, other):
        return Point2D(self.__x * other, self.__y * other)

    def __truediv__(self, other):
        if other:
            return Point2D(self.__x / other, self.__y / other)
        else:
            return Point2D.nan()

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

    @staticmethod
    def nan():
        return Point2D(float('nan'), float('nan'))


if __name__ == '__main__':
    print(Point2D.nan())
