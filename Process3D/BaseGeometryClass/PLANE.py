from POINT3D import POINT3D
from copy import deepcopy
import numpy as np
from MathematicsTransfer import rodrigues


class Plane:
    """
    面的点法式方程：
    vp1 * (x-n1) + vp2 * (y-n2) + vp3 * (z-n3) = 0
    """

    def __init__(self, xorigin=POINT3D(0, 0, 0), xvector=POINT3D(0, 0, 1)):
        self.origin = deepcopy(xorigin)
        self.vector = deepcopy(xvector)

    def __str__(self):
        return f'origin:{self.origin},vector:{self.vector}'

    def save(self, x_file_path):
        # 生成大小为100*100的XY平面，然后旋转到当前法向量，保存
        list_of_point = []
        for xx in range(-50, 50):
            for yy in range(-50, 50):
                list_of_point.append(POINT3D(xx, yy, 0))
        old_vector = POINT3D(0, 0, 1)

        x_theta = np.arccos(np.dot(old_vector.to_array(), self.vector.to_array()) / (old_vector.norm() * self.vector.norm()))
        if x_theta < 1e-5:
            # 如果旋转角度很小，则直接保存Z平面
            with open(x_file_path, 'w') as f:
                for x_point in list_of_point:
                    print(f'{x_point.x},{x_point.y},{x_point.z}', file=f)
        else:
            # 通过旋转轴和旋转角度计算变换矩阵
            a1, b1, c1 = old_vector.to_array()
            a2, b2, c2 = self.vector.to_array()
            x_axis = POINT3D(b1 * c2 - b2 * c1, c1 * a2 - a1 * c2, a1 * b2 - a2 * b1).to_norm()
            x_matrix = rodrigues((x_axis * x_theta).to_array())
            with open(x_file_path, 'w') as f:
                for x_point in list_of_point:
                    new_point_array = np.dot(x_matrix, x_point.to_array()) + self.origin.to_array()
                    print(f'{new_point_array[0]},{new_point_array[1]},{new_point_array[2]}', file=f)


def test():
    import os
    save_folder = r"D:\全局标定测试\测试单元"
    save_file = os.path.join(save_folder, "test-Plane.txt")

    # region 测试plane类
    m_plane = Plane(xorigin=POINT3D(0, 0, 0), xvector=POINT3D(0, 1, 1))
    print('测试print函数：', m_plane)
    m_plane.save(save_file)
    # endregion 测试plane类


if __name__ == '__main__':
    test()
