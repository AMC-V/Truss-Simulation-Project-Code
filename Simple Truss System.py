import vpython as vp 
import numpy as np

# region compatablaility methods from VCcode to Growscript, Don't add these to Glowscript
def arrow(**kid):
    return vp.arrow(pos = kid["pos"], axis = kid["axis"], round = True)

def vec(x,y,z):
    return vp.vec(x,y,z)

def sphere(**kid):
    return vp.sphere(pos = kid["pos"], radius = kid["radius"], make_trail = True)

def radians(number):
    return vp.radians(number)

def sin(number):
    return vp.sin(number)

def cos(number):
    return vp.cos(number)

def arange(min, max, change):
    return vp.arange(min, max, change)

def cylinder(**kid):
    return vp.cylinder(pos = kid["pos"], axis = kid["axis"], color = kid["color"])

def pi():
    return vp.pi

def ring(**kid):
    return vp.ring(pos = kid["pos"], axis = kid["axis"], radius = kid["radius"])

def rate(number):
    return vp.rate(number)

def cross(number_1, number_2):
    return vp.cross(number_1, number_2)

def mag(number):
    return vp.mag(number)

def hat(number):
    return vp.hat(number)
# endregion

# region Coordiante System 
origin = vp.vec(0, 0, 0)
axis = vp.sphere(pos = origin, radius = 5)  # Here radius is length of axis
axis.l = axis.radius  # Lenght of axis arrows
axis.s = 0.05         # Radius of axis arrows
axis.f = 'monospace'
axis.toffset = 0.05
axis.visible = False

pos_x_axis = vp.arrow(pos = origin, axis = vp.vec(axis.l,0,0), shaftwidth = axis.s, round=True,
         color = vp.vec(1, 0, 0))
pos_x_axis_label = vp.label(pos = pos_x_axis.pos + pos_x_axis.axis + vp.vec(axis.toffset, 0, 0), 
         text='+x', height = 16, border = 4, font = axis.f, line = False, opacity = 0, box = False)
         
neg_x_axis = vp.arrow(pos = origin, axis = vp.vector(-axis.l,0,0), shaftwidth = axis.s, round=True,
         color = vp.vec(1, 0, 0))
neg_x_axis_label = vp.label(pos = neg_x_axis.pos + neg_x_axis.axis + vp.vec(-axis.toffset, 0, 0), 
         text='-x', height = 16, border = 4, font = axis.f, line = False, opacity = 0, box = False)
         
pos_y_axis = vp.arrow(pos = origin, axis = vp.vector(0,axis.l,0), shaftwidth = axis.s, round=True, 
         color = vp.vec(0, 1, 0))
pos_y_axis_label = vp.label(pos = pos_y_axis.pos + pos_y_axis.axis + vp.vec(0, axis.toffset, 0), 
         text='+y', height = 16, border = 4, font = axis.f, line = False, opacity = 0, box = False)
         
neg_y_axis = vp.arrow(pos = origin, axis = vp.vector(0,-axis.l,0), shaftwidth = axis.s, round=True, 
         color = vp.vec(0, 1, 0))
neg_y_axis_label = vp.label(pos = neg_y_axis.pos + neg_y_axis.axis + vp.vec(0, -axis.toffset, 0), 
         text='-y', height = 16, border = 4,font = axis.f, line = False, opacity = 0, box = False)

pos_z_axis = vp.arrow(pos = origin, axis = vp.vector(0,0,axis.l), shaftwidth = axis.s, round=True, 
         color = vp.vec(0, 0, 1))
pos_z_axis_label = vp.label(pos = pos_z_axis.pos + pos_z_axis.axis + vp.vec(0, axis.toffset, 0), 
         text='+z', height = 16, border = 4, font = axis.f, line = False, opacity = 0, box = False)
         
neg_z_axis = vp.arrow(pos = origin, axis = vp.vector(0,0,-axis.l), shaftwidth = axis.s, round=True, 
         color = vp.vec(0, 0, 1))
neg_z_axis_label = vp.label(pos = neg_z_axis.pos + neg_z_axis.axis + vp.vec(0, -axis.toffset, 0), 
         text='-z', height = 16, border = 4,font = axis.f, line = False, opacity = 0, box = False)
# endregion

# region Object Creation
truss_mass = 1 # kg Here we assume weight is neglible 
b = 1 # m
a = 1 # m
c = vp.sqrt(a**2 + b**2)

truss_1 = vp.sphere(pos=vp.vec(0,0,0), radius=.1, color=vp.vec(1,0.8,0.56))
truss_2 = vp.sphere(pos=vp.vec(0,b,0), radius=.1, color=vp.vec(1,0.8,0.56))
truss_3 = vp.sphere(pos=vp.vec(a,b,0), radius=.1, color=vp.vec(1,0.8,0.56))

member_1to2 = vp.cylinder(pos=truss_1.pos, radius=truss_1.radius, axis=truss_2.pos,
                          texture=vp.textures.metal)
member_1to3 = vp.cylinder(pos=truss_1.pos, radius=truss_2.radius, axis=truss_3.pos,
                          texture=vp.textures.metal)
member_2to3 = vp.cylinder(pos=truss_2.pos, radius=truss_3.radius, axis=truss_3.pos-truss_2.pos,
                          texture=vp.textures.metal)
# endregion

# region Engineering supports
roller_support = vp.sphere(pos=truss_1.pos - vp.vec(2*truss_1.radius, 0, 0), radius=truss_1.radius)

pin_support = vp.pyramid(pos=truss_2.pos-vp.vec(2*truss_2.radius, 0, 0)+vp.vec(0 ,truss_2.radius/2, 0),
                size=vp.vec(.2, .2, .2))
# endregion

# region ground
ground = vp.box(pos=roller_support.pos - vp.vec(roller_support.radius + 2/2, 0, 0),
                size=vp.vec(2,5,5), texture=vp.textures.wood)
# endregion

user_input_force = input("Enter Force\n")
truss_location = input("Enter truss applied\n")

force_applied = int(user_input_force) # Will be axis, y dir only

force_applied_vector = vp.vec(0, -force_applied, 0)

force_arrow = vp.arrow(pos = origin, axis = vp.vec(0,0,0), shaftwidth = axis.s, round=True,
         color = vp.vec(1, 0, 0))

if truss_location == 'A':
    print("applied at A")
    
    force_arrow.pos = vp.vec(truss_1.pos.x, truss_1.pos.y + 1, 0)
    force_arrow.axis = vp.hat(force_applied_vector)
    
elif truss_location == 'B':
    print("applied at B")
    
    force_arrow.pos = vp.vec(truss_2.pos.x, truss_2.pos.y + 1, 0)
    force_arrow.axis = vp.hat(force_applied_vector)
    
else:
    print("applied at C")
    
    force_arrow.pos = vp.vec(truss_3.pos.x, truss_3.pos.y + 1, 0)
    force_arrow.axis = vp.hat(force_applied_vector)


# Joint A 
Sum_of_forces_A_x = np.array( [0, a/c, 0, 0, 0, 1] )
Sum_of_forces_A_y = np.array( [1, b/c, 0, 0, 0, 0] )

# Joint B
Sum_of_forces_B_x = np.array( [0, 0, 1, 1, 0, 0] )
Sum_of_forces_B_y = np.array( [-1, 0, 0, 0, 1, 0] )

# Joint C
Sum_of_forces_C_x = np.array( [0, -a/c, -1, 0, 0, 0] )
Sum_of_forces_C_y = np.array( [0, -b/c, 0, 0, 0, 0] )

# K coefficient matrix
k = np.array( [Sum_of_forces_A_x, Sum_of_forces_A_y, # 6 rows
             Sum_of_forces_B_x, Sum_of_forces_B_y,
             Sum_of_forces_C_x, Sum_of_forces_C_y] )

# Unknown reaction force
f_1 = 0
f_2 = 0
f_3 = 0
r_1_x = 0
r_1_y = 0
r_2 = 0
fr = np.array( [[f_1], [f_2], [f_3], [r_1_x], [r_1_y], [r_2]] ) # single row

# Know forces
fa = np.array( [[0], [0], [0], [0], [0], [-force_applied]] ) # single row

# Solution
fr = (np.linalg.inv(k)).dot(fa)

print(fr) 
