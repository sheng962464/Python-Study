import numpy as np


def test_np_dot():
    """
    numpy.dot()
    对于两个一维的数组，计算的是这两个数组对应下标元素的乘积和(数学上称之为内积)；
    对于二维数组，计算的是两个数组的矩阵乘积；
    """
    print(np.dot(np.array([2, 3]), np.array([3, 4])))

    a = np.array([[1, 2], [3, 4]])
    b = np.array([[11, 12], [13, 14]])
    # 矩阵乘法
    print(np.dot(a, b))

    data = np.arange(10).reshape(2, 5)
    print(data.T)


def test_np_eig():
    # np中的eig分解为A=P*B*PT 而不是A=QT*B*Q
    # 即 C = vecs * np.diag(vals) * vecs.T # 这里简写*为矩阵乘法
    # eig分解出的vecs的列向量是特征向量。
    A = np.random.randint(-10, 10, (4, 4))
    C = np.dot(A.T, A)
    print(C)
    vals, vecs = np.linalg.eig(C)
    print(vals)
    print("每一列代表一个特征向量：")
    print(vecs)
    # C * vecs[:,0] = vals[0] * vecs[:,0]
    print(f"其中一个特征向量：{vecs[:, 0]}")
    print(f"验证C=P*B*PT：{np.allclose(C, np.dot(vecs, np.dot(np.diag(vals), vecs.transpose())))}")


def test_np_svd():
    A = np.array([[-9., 3., -7.],
                  [4., -8., -1.],
                  [-1., 6., -9.],
                  [-4., -10., 2.]])
    print(A)
    u, s, vh = np.linalg.svd(A)
    print(f"u.shape:{u.shape}  s.shape:{s.shape}  vh.shape:{vh.shape}")
    print("把S化为奇异值矩阵")
    s_diag = np.zeros([4, 3])
    s_diag[:3, :3] = np.diag(s)
    print(s_diag)
    print(f"验证A == u*s*vh:{np.allclose(A, np.dot(u, np.dot(s_diag, vh)))}")


def test_is_rotate_matrix():
    A = np.array([[1, 0.1, -0.2],
                  [-0.1, 1, 0.3],
                  [0.2, -0.3, 1]])
    print(A.T)
    print(np.linalg.inv(A))


# 矩阵乘法
# np.matmul()

if __name__ == '__main__':
    test_is_rotate_matrix()
