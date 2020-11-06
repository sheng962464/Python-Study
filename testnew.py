import math
import numpy


def matrix_to_eular(dMatrix):
    theta_x = math.atan2(-dMatrix[6], dMatrix[10])
    theta_y = math.atan2(-dMatrix[2], math.sqrt(dMatrix[0] * dMatrix[0] + dMatrix[1] * dMatrix[1]))
    theta_z = math.atan2(-dMatrix[1], dMatrix[0])

    theta_x = numpy.rad2deg(theta_x)
    theta_y = numpy.rad2deg(theta_y)
    theta_z = numpy.rad2deg(theta_z)

    return theta_x, theta_y, theta_z


def EularToMatrix(eular):
    theta_x, theta_y, theta_z = eular

    theta_x = numpy.deg2rad(theta_x)
    theta_y = numpy.deg2rad(theta_y)
    theta_z = numpy.deg2rad(theta_z)

    c1 = numpy.cos(theta_x)
    s1 = numpy.sin(theta_x)
    c2 = numpy.cos(theta_y)
    s2 = numpy.sin(theta_y)
    c3 = numpy.cos(theta_z)
    s3 = numpy.sin(theta_z)

    matrix = [c2 * c3, -c2 * s3, -s2, 0,
              c1 * s3 - c3 * s1 * s2, c1 * c3 - s1 * s2 * s3, -c2 * s1, 0,
              s1 * s3 - c1 * c3 * s2, c3 * s1 - c1 * s2 * s3, c1 * c2, 0,
              0, 0, 0, 1]
    return toMatrix(matrix)


def toMatrix(matrix):
    return numpy.array([[matrix[0], matrix[1], matrix[2], matrix[3]],
                        [matrix[4], matrix[5], matrix[6], matrix[7]],
                        [matrix[8], matrix[9], matrix[10], matrix[11]],
                        [matrix[12], matrix[13], matrix[14], matrix[15]]])


def toList(matrix):
    return [matrix[0][0], matrix[0][1], matrix[0][2], matrix[0][3],
            matrix[1][0], matrix[1][1], matrix[1][2], matrix[1][3],
            matrix[2][0], matrix[2][1], matrix[2][2], matrix[2][3],
            matrix[3][0], matrix[3][1], matrix[3][2], matrix[3][3]]


if __name__ == '__main__':
    TP_Eular1 = [-0.1211, -0.0368, 0]
    Frame_Eular1 = [0.0466, 0.7213, 0]
    matrix1 = numpy.dot(EularToMatrix(TP_Eular1), EularToMatrix(Frame_Eular1))
    #print(matrix_to_eular(toList(matrix1)))

    # 旋转0.1
    TP_Eular2 = [-0.1211, -0.0368, 0]
    Frame_Eular2 = [0.2332, 0.7287, 0.0014]
    matrix2 = numpy.dot(EularToMatrix(TP_Eular2), EularToMatrix(Frame_Eular2))
    #print(matrix_to_eular(toList(matrix2)))


    count = 0
    eular_x = [x / 100.0 for x in range(-200, 200)]
    eular_y = [y / 100.0 for y in range(-200, 200)]
    eular_z = [z / 100.0 for z in range(-200, 200)]
    for i in eular_x:
        for j in eular_y:
            for k in eular_z:
                xxxeular = (i, j, k)
                temp = EularToMatrix(xxxeular)

                temp1 = numpy.dot(temp, matrix1)
                temp2 = numpy.dot(temp, matrix2)
                tempEular1 = matrix_to_eular(toList(temp1))
                tempEular2 = matrix_to_eular(toList(temp2))
                print(tempEular1[0] - tempEular2[0])
                if abs(tempEular1[0] - tempEular2[0]) > 0.195:
                    print(tempEular1[0] - tempEular2[0])
                    exit(0)
