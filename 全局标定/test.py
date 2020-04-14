from BaseClass import point

v1 = point(2.872126e+01, -7.796996e+01, -3.244035e+00)
v2 = point(2.847628e+01, -7.800980e+01, -3.250578e+00)
v3 = point(2.849395e+01, -7.810213e+01, -3.397496e+00)

nx = (v1.y - v3.y) * (v2.z - v3.z) - (v1.z - v3.z) * (v2.y - v3.y)
ny = (v1.z - v3.z) * (v2.x - v3.x) - (v2.z - v3.z) * (v1.x - v3.x)
nz = (v1.x - v3.x) * (v2.y - v3.y) - (v2.x - v3.x) * (v1.y - v3.y)

print(f'{nx:.6e} {ny:.6e} {nz:.6e}')
