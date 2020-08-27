from POINT3D import POINT3D
from POINT2D import POINT2D
from LINE3D import LINE3D
from LINE2D import LINE2D


def point_3d_to_point_2d(x_point_3d):
    """
    将3D点转化为2D点，即投影到Z平面上
    @param x_point_3d:
    @return:
    """
    assert isinstance(x_point_3d, POINT3D)
    return POINT2D(x_point_3d.x, x_point_3d.y)


def point_2d_to_point_3d(x_point_2d):
    """
    将2D点转化为3D点，将Z置为0
    @param x_point_2d:
    @return:
    """
    assert isinstance(x_point_2d, POINT2D)
    return POINT3D(x_point_2d.x, x_point_2d.y, 0)


def line_3d_to_line_2d(x_line_3d):
    """
    将3D的直线转化为2D直线，即投影到Z平面上
    @param x_line_3d:
    @return:
    """
    assert isinstance(x_line_3d, LINE3D)
    origin_line_2d = point_3d_to_point_2d(x_line_3d.origin)
    direction_line_2d = point_3d_to_point_2d(x_line_3d.direction)
    return LINE3D(origin_line_2d, direction_line_2d)


def line_2d_to_3d(x_line_2d):
    """
    将2D的直线转化为3D直线，即将Z置为0
    @param x_line_2d:
    @return:
    """
    assert isinstance(x_line_2d, LINE2D)
    origin_line_3d = point_2d_to_point_3d(x_line_2d.origin)
    direction_line_3d = point_2d_to_point_3d(x_line_2d.direction)
    return LINE3D(origin_line_3d, direction_line_3d)
