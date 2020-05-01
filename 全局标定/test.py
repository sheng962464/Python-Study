from BaseClass import Point2D

"""
v1 = Point3D(-7.929647695882494e-16, 43.307464599609375, -4.210000038146973)
v2 = Point3D(-0.012109375558793545, 43.28156661987305, -4.210000038146973)
v3 = Point3D(-7.929647695882494e-16, 41.29999923706055, -4.210000038146973)

nx = (v1.y - v3.y) * (v2.z - v3.z) - (v1.z - v3.z) * (v2.y - v3.y)
ny = (v1.z - v3.z) * (v2.x - v3.x) - (v2.z - v3.z) * (v1.x - v3.x)
nz = (v1.x - v3.x) * (v2.y - v3.y) - (v2.x - v3.x) * (v1.y - v3.y)

print(f'法向量为： {nx:.3f} {ny:.3f} {nz:.3f}')

print(f'顶点1为： {v1.x:.3f} {v1.y:.3f} {v1.z:.3f}')
print(f'顶点1为： {v2.x:.3f} {v2.y:.3f} {v2.z:.3f}')
print(f'顶点1为： {v3.x:.3f} {v3.y:.3f} {v3.z:.3f}')
"""

testPoint = Point2D(1, 1)
pointList = [Point2D(0, 2), Point2D(2, 2), Point2D(2, 0), Point2D(0, 0)]
bRet = False
j = len(pointList) - 1
for i in range(len(pointList)):
    if pointList[i].y < testPoint.y < pointList[j].y or pointList[j].y < testPoint.y < pointList[i].y:
        if testPoint.x > (testPoint.y - pointList[i].y) * (pointList[j].x - pointList[i].x) / (
                pointList[j].y - pointList[i].y) + pointList[i].x:
            bRet = not bRet
    j = i
print(bRet)
