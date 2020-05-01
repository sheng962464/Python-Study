from BaseClass import *
import numpy as np
import time

epsilon1 = 1e-1
epsilon2 = 1e-2
epsilon3 = 1e-3
epsilon5 = 1e-5
epsilon8 = 1e-8

def cross_multiply(x_point1, x_point2):
    """
    | i j k |
　　|a1 b1 c1|
　　|a2 b2 c2|
　　=(b1c2 - b2c1, c1a2 - a1c2, a1b2 - a2b1)
    在三维几何中，
    向量a和向量b的叉乘结果是一个向量，更为熟知的叫法是法向量，该向量垂直于a和b向量构成的平面
    """
    assert isinstance(x_point1, Point3D) and isinstance(x_point2, Point3D)
    a1, b1, c1 = x_point1.to_array()
    a2, b2, c2 = x_point2.to_array()
    return Point3D(b1 * c2 - b2 * c1, c1 * a2 - a1 * c2, a1 * b2 - a2 * b1).to_norm()


def cross_multiply_2D(x_point1, x_point2):
    """
    | i j k |
　　|a1 b1 c1|
　　|a2 b2 c2|
　　=(b1c2 - b2c1, c1a2 - a1c2, a1b2 - a2b1)
    在三维几何中，
    向量a和向量b的叉乘结果是一个向量，更为熟知的叫法是法向量，该向量垂直于a和b向量构成的平面
    """
    assert isinstance(x_point1, Point2D) and isinstance(x_point2, Point2D)
    x1, y1 = x_point1.to_array()
    x2, y2 = x_point2.to_array()
    return x1 * y2 - x2 * y1


def dot_multiply(x_point1, x_point2):
    """
    (a1,b1,c1) * (a2,b2,c2) = a1a2 + b1b2 + c1c2
    点乘的几何意义是可以用来表征或计算两个向量之间的夹角,以及在b向量在a向量方向上的投影
    dot(x,y) = |x| * |y| * cos
    """
    assert isinstance(x_point1, Point3D) and isinstance(x_point2, Point3D)
    return np.dot(x_point1.to_array(), x_point2.to_array())


def intersection_of_line_and_plane(xline, xplane):
    """
    计算直线与面的交点
    t = ((n1–m1)*vp1 + (n2–m2)*vp2 + (n3–m3)*vp3) / (vp1*v1+ vp2*v2+ vp3*v3)
    (可以优化为向量的叉乘)
    """
    assert isinstance(xline, Line3D) and isinstance(xplane, Plane)
    if dot_multiply(xline.direction, xplane.vector):
        temp = dot_multiply((xplane.origin - xline.origin), xplane.vector) / dot_multiply(xline.direction,
                                                                                          xplane.vector)
        return xline.get_point_from_t(temp)
    else:
        return None


def create_plane_from_3point(xpoint1, xpoint2, xpoint3):
    """
    通过三个点构造面
    计算平面的法向量,用点法式构造平面
    (函数可以优化为向量的叉乘)
    """
    assert isinstance(xpoint1, Point3D) and isinstance(xpoint2, Point3D) and isinstance(xpoint3, Point3D)
    xvector1 = xpoint1 - xpoint2
    xvector2 = xpoint1 - xpoint3
    return Plane(xpoint1, cross_multiply(xvector1, xvector2))


def point_rotate(x_point, x_matrix, x_center=Point3D(0, 0, 0)):
    """
    既是点的旋转，又是向量的旋转
    """
    assert isinstance(x_point, Point3D) and isinstance(x_matrix, np.ndarray) and isinstance(x_center, Point3D)
    new_point_array = np.dot(x_matrix, (x_point - x_center).to_array()) + x_center.to_array()
    return Point3D(*new_point_array)


def line_rotate(x_line, x_matrix, x_center=Point3D(0, 0, 0)):
    """
    直线起始点绕旋转中心旋转，直线方向向量绕原点旋转
    """
    assert isinstance(x_line, Line3D) and isinstance(x_matrix, np.ndarray) and isinstance(x_center, Point3D)
    new_line_origin = point_rotate(x_line.origin, x_matrix, x_center)
    new_line_direction = point_rotate(x_line.direction, x_matrix)
    return Line3D(new_line_origin, new_line_direction)


def plane_rotate(x_plane, x_matrix, x_center=Point3D(0, 0, 0)):
    """
    面起始点绕旋转中心旋转，直线方向向量绕原点旋转
    """
    assert isinstance(x_plane, Plane) and isinstance(x_matrix, np.ndarray) and isinstance(x_center, Point3D)
    new_plane_origin = point_rotate(x_plane.origin, x_matrix, x_center)
    new_plane_vector = point_rotate(x_plane.vector, x_matrix)
    return Plane(new_plane_origin, new_plane_vector)


def triangle_rotate(x_triangle, x_matrix, x_center=Point3D(0, 0, 0)):
    """
    三角形三个顶点绕旋转中心旋转
    """
    assert isinstance(x_triangle, Triangle3D) and isinstance(x_matrix, np.ndarray) and isinstance(x_center, Point3D)
    new_vertex1 = point_rotate(x_triangle.vertex1, x_matrix, x_center)
    new_vertex2 = point_rotate(x_triangle.vertex2, x_matrix, x_center)
    new_vertex3 = point_rotate(x_triangle.vertex3, x_matrix, x_center)
    return Triangle3D(new_vertex1, new_vertex2, new_vertex3)


def triangle_slice_rotate(x_triangle_slice, x_matrix, x_center=Point3D(0, 0, 0)):
    """
    三角形三个顶点绕旋转中心旋转,法向量绕原点旋转
    """
    assert isinstance(x_triangle_slice, TriangleSlice) and isinstance(x_matrix, np.ndarray) and isinstance(x_center,
                                                                                                           Point3D)
    new_vertex = triangle_rotate(x_triangle_slice.vertex, x_matrix, x_center)
    new_facet = point_rotate(x_triangle_slice.facet, x_matrix)
    return TriangleSlice(new_facet, new_vertex)


def model_rotate(x_model, x_matrix, x_center=Point3D(0, 0, 0)):
    """
    每个三角面片绕旋转中心旋转
    """
    assert isinstance(x_model, STLModel) and isinstance(x_matrix, np.ndarray) and isinstance(x_center, Point3D)
    triangle_list = []
    for x_triangle_slice in x_model:
        triangle_list.append(triangle_slice_rotate(x_triangle_slice, x_matrix, x_center))
    return STLModel(triangle_list)


def is_point_in_triangle_3D(x_point, x_triangle):
    pass


def is_point_in_triangle_2D(x_point, x_triangle_2D):
    """
    判断平面上的点是否在三角形内
    算法原理使用向量的叉乘。假设三角形的三个点按照顺时针顺序为A,B,C
    对于某一点P,求出三个向量PA，PB，PC
    t1 = PA * PB
    t2 = PB * PC
    t3 = PC * PA
    如果t1,t2,t3同号，则P在三角形内部，否则在外部
    如果t1*t2*t3 = 0，则表示该点在三角形的边界
    """
    assert isinstance(x_point, Point2D) and isinstance(x_triangle_2D, Triangle2D)

    tx, ty = x_point.x,x_point.y
    t_box = x_triangle_2D.get_box_2d()
    if not (t_box.x_min <= tx <= t_box.x_max and t_box.y_min <= ty <= t_box.y_max):
        return False

    PA = x_triangle_2D.vertex1 - x_point
    PB = x_triangle_2D.vertex2 - x_point
    PC = x_triangle_2D.vertex3 - x_point
    t1 = cross_multiply_2D(PA, PB)
    t2 = cross_multiply_2D(PB, PC)
    t3 = cross_multiply_2D(PC, PA)
    if t1 > 0 and t2 > 0 and t3 > 0 or t1 < 0 and t2 < 0 and t3 < 0:
        return True
    else:
        return False


def get_rotate_matrix_from_two_vector(x_vector_old, x_vector_new):
    """
    已知旋转前后的两个向量，计算该旋转矩阵
    使用罗德里格斯变换，通过余弦公式计算旋转角度，通过向量叉乘计算旋转轴
    返回的矩阵为由老向量至新向量的矩阵
    """
    assert isinstance(x_vector_old, Point3D) and isinstance(x_vector_new, Point3D)
    x_theta = np.arccos(dot_multiply(x_vector_old, x_vector_new) / (x_vector_old.norm() * x_vector_new.norm()))
    if x_theta <= epsilon5:
        return np.eye(3)
    x_axis = cross_multiply(x_vector_old, x_vector_new)
    return BaseTransfer.Rodrigues((x_axis * x_theta).to_array())


def intersection_of_line_and_model(x_line, x_model):
    """
    先把直线的方向向量转到(0,0,-1),计算该旋转矩阵，为axis_to_z_matrix
    axis_to_z_matrix * model = temp_model
    判断直线与三角面片的交点(Z向投影)
    计算axis_to_z_matrix的逆矩阵，z_to_axis_matrix

    """
    assert isinstance(x_line, Line3D) and isinstance(x_model, STLModel)

    # matrix_line_to_z = get_rotate_matrix_from_two_vector(x_line.direction, Point3D(0, 0, -1))
    # temp_model = model_rotate(x_model, matrix_line_to_z)

    i = 0
    for x_triangle_slice in x_model:
        i = i + 1
        temp = intersection_of_line_and_triangle_slice(x_line, x_triangle_slice)
        if temp:
            triangle_slice_model = STLModel([x_triangle_slice])
            return temp


def intersection_of_line_and_triangle_slice(x_line, x_triangle_slice):
    """
    直线的方向为(0,0,-1),与三角面片计算交点
    """
    assert isinstance(x_line, Line3D) and isinstance(x_triangle_slice, TriangleSlice)
    if is_point_in_triangle_2D(x_line.origin.to_point_2d(), x_triangle_slice.vertex.to_triangle_2d()):
        x_plane = create_plane_from_3point(x_triangle_slice.vertex.vertex1,
                                           x_triangle_slice.vertex.vertex2,
                                           x_triangle_slice.vertex.vertex3)
        intersection_point = intersection_of_line_and_plane(x_line, x_plane)
        if intersection_point:
            return intersection_point
    else:
        return None


def test_unit():
    # # region 测试point_rotate()
    # old_point = Point3D(0, 1, 1)
    # m_matrix = BaseTransfer.euler_angle_to_matrix((-90, 0, 0))
    # new_point = point_rotate(old_point, m_matrix,Point3D(0,1,0))
    # print(new_point)
    # # endregion

    # # region 测试line_rotate()
    # old_line = Line3D(xorigin=Point3D(0,0,1),xdirection=Point3D(0,0,1))
    # m_matrix = BaseTransfer.euler_angle_to_matrix((-90, 0, 0))
    # new_line = line_rotate(old_line,m_matrix,Point3D(0,0,1))
    # print(new_line)
    # # endregion

    # # region 测试plane_rotate()
    # old_plane = Plane(Point3D(0,1,0),Point3D(0,0,1))
    # m_matrix = BaseTransfer.euler_angle_to_matrix((-90, 0, 0))
    # new_plane = plane_rotate(old_plane,m_matrix,Point3D(0,0,0))
    # print(new_plane)
    # # endregion

    # # region 叉乘测试
    # m_point1 = Point3D(1, 22, 0)
    # m_point2 = Point3D(3, 1, 0)
    # print(cross_multiply(m_point1, m_point2))
    # print(dot_multiply(m_point1, m_point2))
    # # endregion

    # # region 测试get_rotate_matrix_from_two_vector
    # m_vector1 = Point3D(0, 0, 1)
    # m_vector2 = Point3D(0, 0, 1)
    # print(get_rotate_matrix_from_two_vector(m_vector1, m_vector2))
    # # endregion

    # # region 测试is_point_in_triangle_2D()
    # start_time = time.time()
    # m_point = Point3D(0.1, 0, 2)
    # m_triangle = Triangle3D(Point3D(0, 0, 0), Point3D(1, 0, 0), Point3D(0, 1, 1))
    # m_point_2D = m_point.to_point_2d()
    # m_triangle_2D = m_triangle.to_triangle_2d()
    # print(m_point_2D)
    # print(m_triangle_2D)
    # print(is_point_in_triangle_2D(m_point_2D, m_triangle_2D))
    # end_time = time.time()
    # print(f'总共耗时：{end_time - start_time}s')
    # # endregion

    # region 测试intersection_of_line_and_model
    m_model = STLModel.read_stl(r'D:\全局标定测试\单层NEY模型-Binary格式.stl')
    print(f'stl读取结束,共{len(m_model)}个三角面片')
    list_intersection = []
    for j in range(-400, 400):
        '''
        从(-2, range(-100,100), 20)点发出光线
        '''
        for i in range(-800, 800):
            start_time = time.time()
            m_line = Line3D(xorigin=Point3D(j * 0.1, i * 0.1, 20), xdirection=Point3D(0, 0, -1))
            print(f'射线的起点：{m_line.origin}', end=',')
            temp = intersection_of_line_and_model(m_line, m_model)
            if temp:
                list_intersection.append(temp)
                end_time = time.time()
                print(f'耗时 {end_time - start_time} s')
            else:
                print(f'无交点', end=',')
                end_time = time.time()
                print(f'耗时 {end_time - start_time} s')

        m_path = r'D:\全局标定测试\result.txt'
        with open(m_path, 'w') as f:
            for x in list_intersection:
                print(f'{x.x},{x.y},{x.z}\n', file=f)
    # endregion

    # # region 测试intersection_of_line_and_triangle_slice
    # m_line = Line3D(xorigin=Point3D(0.000,99.000,20.000), xdirection=Point3D(0, 0, -1))
    # m_triangle_slice = TriangleSlice(x_facet=(0.000,0.000,0.024),
    #                                   x_vertex=Triangle3D(Point3D(-0.000,43.307,-4.210),
    #                                                     Point3D(-0.012,43.282,-4.210),
    #                                                     Point3D(-0.000,41.300,-4.210)))
    # print(intersection_of_line_and_triangle_slice(m_line,m_triangle_slice))
    # # endregion

    # # region 测试model_rotate
    # m_model = STLModel.read_stl(r'D:\全局标定测试\单层NEY模型.stl')
    # m_matrix = BaseTransfer.euler_angle_to_matrix([0, 0, 90])
    # n_model = model_rotate(m_model, m_matrix)
    # n_model.save(r'D:\全局标定测试\单层NEY模型-111.stl')
    # # endregion
    pass


if __name__ == '__main__':
    test_unit()
