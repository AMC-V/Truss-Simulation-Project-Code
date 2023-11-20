import numpy as np
import vpython as vp
import sys

a = 1 / vp.sqrt(2)

# Joint A 
Sum_of_forces_A_x = np.array( [a, 0, 1, 1, 0, 0] )
Sum_of_forces_A_y = np.array( [a, 0, 0, 0, 1, 0] )

# Joint B
Sum_of_forces_B_x = np.array( [-a, a, 0, 0, 0, 0] )
Sum_of_forces_B_y = np.array( [-a, -a, 0, 0, 0, 0] )

# Joint C
Sum_of_forces_C_x = np.array( [0, -a, -1, 0, 0, 0] )
Sum_of_forces_C_y = np.array( [0, a, 0, 0, 0, 1] )

# K coefficient matrix
k = np.array( [Sum_of_forces_A_x, Sum_of_forces_A_y, # 6 rows
             Sum_of_forces_B_x, Sum_of_forces_B_y,
             Sum_of_forces_C_x, Sum_of_forces_C_y, ] )

print(k)
print("\n")

# Unknown reaction force
f_AB = 0
f_AE = 0
f_BC = 0
D_x = 0
D_y = 0
R = 0
fr = np.array( [[f_AB], [f_AE], [f_BC], [D_x], [D_y], [R]] ) # single row

# Know forces
fa = np.array( [[0], [0], [0], [1], [0], [0]] ) # single row

# Solution
fr = (np.linalg.inv(k)).dot(fa)

print(fr) 
sys.exit(0)