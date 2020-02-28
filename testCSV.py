"""

2020年2月28日08:59:47
与张淼测试点云数据极限压缩(仅保留Z值)后的大小

"""

csv_path = r'C:\Users\18320\Desktop\1ABCH00.csv'
z_path = r'C:\Users\18320\Desktop\gggg1ABCH00.csv'

with open(csv_path, 'r') as f:
    for str_line in f:
        points_line = list(map(float, str_line.split(',')))
        z_line = []
        for i in range(0, len(points_line), 4):
            z_line.extend(points_line[i:i + 3])
        with open(z_path, 'a', encoding='utf-8') as fz:
            for x in z_line:
                print(x, file=fz, end=',')
            print('', file=fz, end='\n')
