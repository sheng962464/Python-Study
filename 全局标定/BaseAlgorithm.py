from BaseClass import *
import numpy as np


# 计算直线与面的交点
def intersection_of_line_and_plane(xline, xplane):
    """
    t = ((n1–m1)*vp1 + (n2–m2)*vp2 + (n3–m3)*vp3) / (vp1*v1+ vp2*v2+ vp3*v3)
    """
    assert isinstance(xline, line) and isinstance(xplane, plane)

    m1 = xline.origin.x
    m2 = xline.origin.y
    m3 = xline.origin.z
    v1 = xline.direction.x
    v2 = xline.direction.y
    v3 = xline.direction.z

    n1 = xplane.origin.x
    n2 = xplane.origin.y
    n3 = xplane.origin.z
    vp1 = xplane.vector.x
    vp2 = xplane.vector.y
    vp3 = xplane.vector.z

    xtemp = ((n1 - m1) * vp1 + (n2 - m2) * vp2 + (n3 - m3) * vp3) / (vp1 * v1 + vp2 * v2 + vp3 * v3)

    return point(m1 + v1 * xtemp, m2 + v2 * xtemp, m3 + v3 * xtemp)


# 通过三个点构造面
def create_plane_from_3point(xpoint1, xpoint2, xpoint3):
    """
    计算平面的法向量,用点法式构造平面
    """
    assert isinstance(xpoint1, point) and isinstance(xpoint2, point) and isinstance(xpoint3, point)
    xvector1 = xpoint1 - xpoint2
    xvector2 = xpoint1 - xpoint3
    x1 = xvector1.x
    y1 = xvector1.y
    z1 = xvector1.z

    x2 = xvector2.x
    y2 = xvector2.y
    z2 = xvector2.z

    a = y1 * z2 - y2 * z1
    b = z1 * x2 - z2 * x1
    c = x1 * y2 - x2 * y1

    return plane(xpoint1, point(a, b, c))


def point_rotate(x_point, x_matrix, x_center=point(0, 0, 0)):
    """
    既是点的旋转，又是向量的旋转
    """
    assert isinstance(x_point, point) and isinstance(x_matrix, np.ndarray) and isinstance(x_center,point)
    new_point_array = np.dot(x_matrix, (x_point - x_center).to_array()) + x_center.to_array()
    return point(*new_point_array)


def line_rotate(x_line, x_matrix, x_center=point(0, 0, 0)):
    """
    直线起始点绕旋转中心旋转，直线方向向量绕原点旋转
    """
    assert isinstance(x_line, line) and isinstance(x_matrix, np.ndarray) and isinstance(x_center, point)
    new_line_origin = point_rotate(x_line.origin, x_matrix, x_center)
    new_line_direction = point_rotate(x_line.direction, x_matrix)
    return line(new_line_origin, new_line_direction)


def plane_rotate(x_plane, x_matrix, x_center=None):
    """
    面起始点绕旋转中心旋转，直线方向向量绕原点旋转
    """
    assert isinstance(x_plane, plane) and isinstance(x_center, point)
    new_plane_origin = point_rotate(x_plane.origin, x_matrix, x_center)
    new_plane_vector = point_rotate(x_plane.vector, x_matrix)
    return plane(new_plane_origin,new_plane_vector)


def test_unit():
    # # region 测试point_rotate()
    # old_point = point(0, 1, 1)
    # m_matrix = BaseTransfer.euler_angle_to_matrix((-90, 0, 0))
    # new_point = point_rotate(old_point, m_matrix,point(0,1,0))
    # print(new_point)
    # # endregion

    # # region 测试line_rotate()
    # old_line = line(xorigin=point(0,0,1),xdirection=point(0,0,1))
    # m_matrix = BaseTransfer.euler_angle_to_matrix((-90, 0, 0))
    # new_line = line_rotate(old_line,m_matrix,point(0,0,1))
    # print(new_line)
    # # endregion

    # region 测试plane_rotate()
    old_plane = plane(point(0,1,0),point(0,0,1))
    m_matrix = BaseTransfer.euler_angle_to_matrix((-90, 0, 0))
    new_plane = plane_rotate(old_plane,m_matrix,point(0,0,0))
    print(new_plane)
    # endregion
    pass


if __name__ == '__main__':
    test_unit()
