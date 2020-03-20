from BaseClass import *
import numpy as np


def cross_multip(x_point1, x_point2):
    """
    | i j k |
　　|a1 b1 c1|
　　|a2 b2 c2|
　　=(b1c2 - b2c1, c1a2 - a1c2, a1b2 - a2b1)
    在三维几何中，
    向量a和向量b的叉乘结果是一个向量，更为熟知的叫法是法向量，该向量垂直于a和b向量构成的平面
    """
    assert isinstance(x_point1, point) and isinstance(x_point2, point)
    a1, b1, c1 = x_point1.to_array()
    a2, b2, c2 = x_point2.to_array()
    return point(b1 * c2 - b2 * c1, c1 * a2 - a1 * c2, a1 * b2 - a2 * b1).to_norm()


def dot_multip(x_point1, x_point2):
    """
    (a1,b1,c1) * (a2,b2,c2) = a1a2 + b1b2 + c1c2
    点乘的几何意义是可以用来表征或计算两个向量之间的夹角,以及在b向量在a向量方向上的投影
    dot(x,y) = |x| * |y| * cos
    """
    assert isinstance(x_point1, point) and isinstance(x_point2, point)
    return np.dot(x_point1.to_array(), x_point2.to_array())


def intersection_of_line_and_plane(xline, xplane):
    """
    计算直线与面的交点
    t = ((n1–m1)*vp1 + (n2–m2)*vp2 + (n3–m3)*vp3) / (vp1*v1+ vp2*v2+ vp3*v3)
    (可以优化为向量的叉乘)
    """
    assert isinstance(xline, line) and isinstance(xplane, plane)
    temp = dot_multip((xplane.origin - xline.origin), xplane.vector) / dot_multip(xline.direction, xplane.vector)
    return xline.get_point_from_t(temp)


def create_plane_from_3point(xpoint1, xpoint2, xpoint3):
    """
    通过三个点构造面
    计算平面的法向量,用点法式构造平面
    (函数可以优化为向量的叉乘)
    """
    assert isinstance(xpoint1, point) and isinstance(xpoint2, point) and isinstance(xpoint3, point)
    xvector1 = xpoint1 - xpoint2
    xvector2 = xpoint1 - xpoint3
    return plane(xpoint1, cross_multip(xvector1, xvector2))


def point_rotate(x_point, x_matrix, x_center=point(0, 0, 0)):
    """
    既是点的旋转，又是向量的旋转
    """
    assert isinstance(x_point, point) and isinstance(x_matrix, np.ndarray) and isinstance(x_center, point)
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
    return plane(new_plane_origin, new_plane_vector)


def get_rotate_matrix_from_two_vector(x_vector_old, x_vector_new):
    """
    已知旋转前后的两个向量，计算该旋转矩阵
    使用罗德里格斯变换，通过余弦公式计算旋转角度，通过向量叉乘计算旋转轴
    返回的矩阵为由老向量至新向量的矩阵
    """
    assert isinstance(x_vector_old, point) and isinstance(x_vector_new, point)
    x_theta = np.arccos(dot_multip(x_vector_old, x_vector_new) / (x_vector_old.norm() * x_vector_new.norm()))
    x_axis = cross_multip(x_vector_old, x_vector_new)
    return BaseTransfer.Rodrigues((x_axis * x_theta).to_array())

def intersection_of_line_and_triangle():
    """
    先把直线的方向向量转到(0,0,-1),计算该旋转矩阵，为axis_to_z_matrix
    axis_to_z_matrix * model = temp_model
    判断直线与三角面片的交点(Z向投影)
    计算axis_to_z_matrix的逆矩阵，z_to_axis_matrix

    """
    pass
    pass


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

    # # region 测试plane_rotate()
    # old_plane = plane(point(0,1,0),point(0,0,1))
    # m_matrix = BaseTransfer.euler_angle_to_matrix((-90, 0, 0))
    # new_plane = plane_rotate(old_plane,m_matrix,point(0,0,0))
    # print(new_plane)
    # # endregion

    # # region 叉乘测试
    # m_point1 = point(1, 22, 0)
    # m_point2 = point(3, 1, 0)
    # print(cross_multip(m_point1, m_point2))
    # print(dot_multip(m_point1, m_point2))
    # # endregion

    # region 测试get_rotate_matrix_from_two_vector
    m_vector1 = point(0,1,0)
    m_vector2 = point(1,0,0)
    print(get_rotate_matrix_from_two_vector(m_vector1,m_vector2))
    # endregion
    pass


if __name__ == '__main__':
    test_unit()
