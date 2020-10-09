def save_point_cloud(x_file, x_list):
    with open(x_file, 'w', encoding='utf-8') as f:
        for row in x_list:
            for point in row:
                print(f"{point[0]},{point[1]},{point[2]},", end='', file=f)
                print(f"{point[0]},{point[1]},{point[2]}", end='')
            print('', file=f)
            print('')


def get_rectangle_point_cloud(sx, sy, sz, width, height):
    # 左上角为起点，输入起点与大小
    x_step = 0.01
    y_step = 0.1
    point_list = []
    x_num = int(width / x_step)
    y_num = int(height / y_step)
    for i in range(y_num):
        row_point = []
        for j in range(x_num):
            row_point.append([sx + j * x_step, sy - i * y_step, sz])
        point_list.append(row_point)
    return point_list


def gen_point_file(sx, sy, sz, width, height, file_path):
    save_point_cloud(file_path, get_rectangle_point_cloud(sx, sy, sz, width, height))


if __name__ == '__main__':
    gen_point_file(1, 13, 0, 1, 11, '1.tx')
    gen_point_file(2, 13, 0, 6, 1, '2.tx')
    gen_point_file(2, 9.5, 0, 6, 1, '3.tx')

