import numpy as np


def test():
    point_a = np.array([0, 0, 12])
    point_b = np.array([0, 12, 0])
    point_c = np.array([12, 0, 0])

    point_d = (point_a + point_b + point_c) /3

    print(point_d)


if __name__ == '__main__':
    test()
