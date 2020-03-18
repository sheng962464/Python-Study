import numpy as np
import numpy.matlib


def Rodrigues(x_vector):
    """
    罗德里格斯变换:绕任意轴旋转某个角度
    x = [nx,ny,nz] = n*[x,y,z]
    [x,y,z]为单位向量，表示旋转轴
    n表示旋转角度
    计算旋转矩阵

    :return: 变换矩阵
    """
    assert isinstance(x_vector, point)
    theta = x_vector.norm()
    s = math.sin(theta)
    c = math.cos(theta)
    c1 = 1.0 - c
    if theta == 0:
        itheta = 0
    else:
        itheta = 1 / theta
    x_vector = x_vector * itheta
    # ax = Point3D.toArray(xVector)

    rrt = x_vector * x_vector
    r_x = Matrix3D([[0, -x_vector.z, x_vector.y],
                    [x_vector.z, 0, -x_vector.x],
                    [-x_vector.y, x_vector.x, 0]])
    ae = Matrix3D.eye()
    r = ae * c + r_x * s + rrt * c1
    return r


def euler_angle_to_matrix(x_euler_angle):
    """
    欧拉角转换为旋转矩阵
    """
    assert len(x_euler_angle) == 3
    euler_angle = np.array(x_euler_angle)
    ax, ay, az = map(np.deg2rad, euler_angle)

    mx = np.array([[1, 0, 0], [0, np.cos(ax), -np.sin(ax)], [0, np.sin(ax), np.cos(ax)]])
    my = np.array([[np.cos(ay), 0, np.sin(ay)], [0, 1, 0], [-np.sin(ay), 0, np.cos(ay)]])
    mz = np.array([[np.cos(az), -np.sin(az), 0], [np.sin(az), np.cos(az), 0], [0, 0, 1]])

    return np.dot(mz, np.dot(my, mx))


def is_rotate_matrix(x_matrix):
    """
    旋转矩阵为正交矩阵，正交矩阵与正交矩阵的逆的乘积为单位矩阵，行列式的值为1
    """
    matrix = np.array(x_matrix)
    pass


def matrix_to_euler_angle(x_matrix):
    """
    旋转矩阵转换为欧拉角
    """
    # 判断是否旋转矩阵
    pass


def test_unit():
    pass


if __name__ == '__main__':
    print('################################')
    test_matrix = euler_angle_to_matrix([10.0, 10.0, 10.0])
    print('旋转矩阵：\n',test_matrix)
    temp = test_matrix.T
    print('旋转矩阵的转置：\n',temp)
    print('旋转矩阵与转置的乘法：\n',np.dot(test_matrix, temp))
    print('乘法的行列式：',np.linalg.det(np.dot(test_matrix, temp)))
