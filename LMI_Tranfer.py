file_Path = 'D:\\replay_62053_2020-5-19.csv'
save_path = 'D:\\1111.csv'
all_num = 0
with open(file_Path, 'r') as f:
    with open(save_path, 'w') as fs:
        con = f.readlines()
        # 所有的X值
        x = list(map(float, con[27].split(',')[1:]))
        # 所有的y值与Z值 每一行第一个数表示y值，其余表示Z值
        new_set = con[28:-2]
        y_num = 0
        for i in new_set:
            line_point = []
            yz_num = i.split(',')
            y_value = float(yz_num[0])
            z = yz_num[1:]
            for x_index, z_value in enumerate(z):
                if z_value and z_value != '\n':
                    cur_Point = f'{x[x_index]},{y_value},{float(z_value)}'
                    print(cur_Point, file=fs, end=',')
                    pass
                else:
                    cur_Point = f'{x[x_index]},{y_value},{999}'
                    print(cur_Point, file=fs, end=',')
            print('', file=fs, end='\n')






