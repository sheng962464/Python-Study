import BaseClass
import BaseAlgorithm
import BaseTransfer


# 传感器扫描函数
def sensor_scan(x_sensor, x_plane):
    """
    使用的传感器，传感器运动的轨迹，扫描的物体
    """
    result = []
    for x_line in x_sensor.laser:
        result.append(BaseAlgorithm.intersection_of_line_and_plane(x_line, x_plane))
    return result


def test_unit():
    result = []
    m_sensor = BaseClass.sensor(x_location=(0, 0, 1))
    path = [[0, i * 0.01, 10] for i in range(-100, 100)]
    for xpath in path:
        m_sensor.sensor_absolute_move(xpath)
        result.append(sensor_scan(m_sensor, BaseClass.plane()))
    print('扫描结束')
    with open(r'D:\全局标定测试\result.txt', 'w') as f:
        for x in result:
            for y in x:
                print(f'{y.x},{y.y},{y.z}', file=f)


if __name__ == '__main__':
    import time
    start_time = time.time()
    test_unit()
    end_time = time.time()
    print(f'耗时{end_time-start_time}s')
