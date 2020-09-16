class Point3D:
    def __init__(self, d_x, d_y, d_z):
        self.x = d_x
        self.y = d_y
        self.z = d_z


m_matrix = [[],
            [],
            [],
            []]


def transfer(d_matrix, d_point):
    assert isinstance(d_point, Point3D)
    p_x = d_matrix[0][0] * d_point.x + d_matrix[0][1] * d_point.y + d_matrix[0][2] * d_point.z + d_matrix[0][3]
    p_y = d_matrix[1][0] * d_point.x + d_matrix[1][1] * d_point.y + d_matrix[1][2] * d_point.z + d_matrix[1][3]
    p_z = d_matrix[2][0] * d_point.x + d_matrix[2][1] * d_point.y + d_matrix[2][2] * d_point.z + d_matrix[2][3]
    return Point3D(p_x, p_y, p_z)


def test():
    point_list = []
    with open('sphere_3.txt', 'r', encoding='utf-8') as f:
        for point_rows in f.readline():
            point_lines = []
            value_list = point_rows.split(',')
            value_count = len(value_list)
            for index in range(0, value_count, 3):
                m_point = Point3D(value_list[index], value_list[index + 1], value_list[index + 2])
                mt_point = transfer(m_matrix, m_point)
                point_lines.append(mt_point)
            point_list.append(point_list)
    return point_list


def save(d_point_list, x_file_path):
    with open(x_file_path, 'w', encoding='utf-8') as f:
        for point_line in d_point_list:
            for point in point_line:
                print(f"{point.x},{point.y},{point.z}", end=',', file=f)
            print('', end='\n', file=f)


if __name__ == '__main__':
    test()
