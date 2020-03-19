import BaseClass
import BaseAlgorithm
import BaseTransfer


# 传感器扫描函数
def sensor_scan(x_sensor, x_travel, x_object):
    """
    使用的传感器，传感器运动的轨迹，扫描的物体
    """


def test_unit():
    m_sensor = BaseClass.sensor(x_location=(0, 0, 1))
    m_sensor.sensor_init()
    path = [[0, i * 0.1, 10] for i in range(-10, 10)]
    for xpath in path:
        m_sensor.sensor_absolute_move(xpath)
        for x in m_sensor.trigPoint:
            xline = BaseClass.line(x, m_sensor.__laser_vector)


if __name__ == '__main__':
    test_unit()
