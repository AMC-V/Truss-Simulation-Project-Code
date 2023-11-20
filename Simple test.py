# region Imports
import vpython as vp
import numpy as np
import sys 
# endregion

# region method overloads for convenions
def arrow(**kid):
    return vp.arrow(pos = kid["pos"], axis = kid["axis"], round = True)

def vec(x,y,z):
    return vp.vec(x,y,z)

def sphere(**kid):
    return vp.sphere(pos = kid["pos"], radius = 0.1, make_trail = False, color = 1/255 * vec(255,150,0))

def radians(number):
    return vp.radians(number)

def sin(number):
    return vp.sin(number)

def cos(number):
    return vp.cos(number)

def arange(min, max, change):
    return vp.arange(min, max, change)

def cylinder(**kid):
    return vp.cylinder(pos = kid["pos"], axis = kid["axis"], radius = 0.1) #, color = kid["color"])

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

def sqrt(number):
    return vp.sqrt(number)
# endregion

# region Gobal Coordiante System 
origin = vec(0, 0, 0)
axis = vp.sphere(pos = origin, radius = 5)  # Here radius is length of axis
axis.l = axis.radius  # Lenght of axis arrows
axis.s = 0.05         # Radius of axis arrows
axis.f = 'monospace'
axis.toffset = 0.05
axis.visible = False
op = 0.5

pos_x_axis = arrow(pos = origin, axis = vec(axis.l, 0, 0))
pos_x_axis.shaftwidth = axis.s
pos_x_axis.color = vec(1, 0, 0)
pos_x_axis.opacity = op

pos_x_axis_label = vp.label(pos = pos_x_axis.pos + pos_x_axis.axis + vec(axis.toffset, 0, 0), 
         text='+x', height = 16, border = 4, font = axis.f, line = False, opacity = 0, box = False)
         
neg_x_axis = arrow(pos = origin, axis = vec(-axis.l, 0, 0))
neg_x_axis.shaftwidth = axis.s
neg_x_axis.color = vec(1, 0, 0)
neg_x_axis.opacity = op

neg_x_axis_label = vp.label(pos = neg_x_axis.pos + neg_x_axis.axis + vec(-axis.toffset, 0, 0), 
         text='-x', height = 16, border = 4, font = axis.f, line = False, opacity = 0, box = False)
         
pos_y_axis = arrow(pos = origin, axis = vec(0, axis.l, 0))
pos_y_axis.shaftwidth = axis.s 
pos_y_axis.color = vec(0, 1, 0)
pos_y_axis.opacity = op

pos_y_axis_label = vp.label(pos = pos_y_axis.pos + pos_y_axis.axis + vec(0, axis.toffset, 0), 
         text='+y', height = 16, border = 4, font = axis.f, line = False, opacity = 0, box = False)
         
neg_y_axis = arrow(pos = origin, axis = vec(0, -axis.l, 0))
neg_y_axis.shaftwidth = axis.s
neg_y_axis.color = vec(0, 1, 0)
neg_y_axis.opacity = op

neg_y_axis_label = vp.label(pos = neg_y_axis.pos + neg_y_axis.axis + vec(0, -axis.toffset, 0), 
         text='-y', height = 16, border = 4,font = axis.f, line = False, opacity = 0, box = False)

pos_z_axis = arrow(pos = origin, axis = vec(0,0,axis.l))
pos_z_axis.shaftwidth = axis.s
pos_z_axis.color = vec(0, 0, 1)
pos_z_axis.opacity = op

pos_z_axis_label = vp.label(pos = pos_z_axis.pos + pos_z_axis.axis + vec(0, axis.toffset, 0), 
         text='+z', height = 16, border = 4, font = axis.f, line = False, opacity = 0, box = False)
         
neg_z_axis = arrow(pos = origin, axis = vec(0,0,-axis.l))
neg_z_axis.shaftwidth = axis.s
neg_z_axis.color = vp.vec(0, 0, 1)
neg_z_axis.opacity = op

neg_z_axis_label = vp.label(pos = neg_z_axis.pos + neg_z_axis.axis + vec(0, -axis.toffset, 0), 
         text='-z', height = 16, border = 4,font = axis.f, line = False, opacity = 0, box = False)
# endregion

list_of_nodes = [] # Will contain all nodes, examples 3 nodes
list_of_elements = [] # Will contain all the elements, connections between nodes, also the number of unknowns
reaction_forces = [] # Will contain pin and roller support

number_of_nodes = int(input("Enter number of nodes\n")) # Ask for number of nodes
print("===========================================")

print("Enter a node's position as x,y")
print("--------------------------")
for x in arange(0, number_of_nodes, 1):
    w,h = input(f"Node {x + 1} position\n").split(",")
    better_w = float(w)
    better_h = float(h) 
    
    sphere(pos = vec(better_w, better_h, 0))
    vp.label(pos = vec(better_w, better_h, 0), text = f"{x + 1}", xoffset = 5, yoffset = 10, space = 1, height = 16, 
             border = 4, font = 'monospace', box = False, opacity = 0, color = 1/255 * vec(255,150,0))
    list_of_nodes.append(vec(better_w, better_h, 0))
    print("--------------------------")
print("===========================================")

# After all nodes are created this the next thing calculated
number_of_equations = 2 * number_of_nodes # Total number of equations based on number of nodes, now 3 nodes
list_of_elements = []
element_visual_list = []
list_of_unknowns = [] # based on the amount of memebers

# which nodes do you want to connect?

number_of_current_members = 0

# Method to connect the two choosen nodes and generates Force vector for the element ==========================
def element_creation(node_number_1, node_number_2):
    global number_of_current_members
    
    number_of_current_members += 1
    
    # Check to flip the inputs
    if node_number_1 > node_number_2:
        temp_number = node_number_2
        node_number_2 = node_number_1
        node_number_1 = temp_number
    
    # Get the nodes (basicaly positions) from the nodes list 
    node_temp_n = list_of_nodes[node_number_1 - 1] # The first element of the nodes list
    node_temp_p = list_of_nodes[node_number_2 - 1] # The second element of the nodes list

    # Create visual of element
    element_AB_visual = cylinder(pos = node_temp_n, axis = node_temp_p - node_temp_n)
    element_AB_visual.texture = vp.textures.metal
    
    vp.label(pos = 1/2 * (element_AB_visual.axis) + element_AB_visual.pos, 
             text = f"<b>{number_of_current_members}</b>", xoffset = 0, yoffset = 0, space = 0, height = 15, 
             border = 1, font = 'monospace', box = True, opacity = 0, linecolor = vec(0,0,0), 
             color = 1/255 * vec(255, 0, 125))
    
    element_visual_list.append(element_AB_visual)
    
    list_of_unknowns.append(number_of_current_members) # Gets number of forces aka memebers, m
    
    x = node_temp_p.x - node_temp_n.x # As a vector component x
    y = node_temp_p.y - node_temp_n.y # As a vector component y
    c = sqrt(x**2 + y**2)   # Mag of triangle

    element_AB = np.zeros( (number_of_equations, 1) ) # Creates an empty matrix where num of eqs is the number of rows, 1 is colum

    # Since node n and node p were choosen then in the element np, the force applied there
    element_AB[node_number_1 * 2 - 2][0] = x/c # The x transformion for the force on the element AB from A
    element_AB[node_number_1 * 2 - 1][0] = y/c # The y transformion for the force on the element AB from A
    element_AB[node_number_2 * 2 - 2][0] = -1 * x/c # The x transformion for the force on the element AB from B
    element_AB[node_number_2 * 2 - 1][0] = -1 * y/c # The y transformion for the force on the element AB from B

    list_of_elements.append(element_AB)

print("Enter an element as node_number,node_number and when finished, enter done.")
print("--------------------------")
while True:
    try:
        q,v = input(f"Enter nodes to create element {number_of_current_members + 1} \n").split(",")
        better_q = int(q)
        better_v = int(v)        
        element_creation(better_q, better_v)
        print("--------------------------")
    except:
        break
print("===========================================")

master_matrix = np.concatenate((list_of_elements[0], list_of_elements[1]), axis = 1)
for x in arange(0, len(list_of_elements) - 2, 1):
    master_matrix = np.hstack((master_matrix, list_of_elements[x + 2]))

# Chose where the pin reaction force is
node_location = int(input("Enter node pin reaction\n"))
node_pin_reaction = list_of_nodes[node_location - 1]

pin_reactions = np.zeros( (number_of_equations, 1) ) # Creates an empty matrix where num of eqs is the number of rows, 1 is colum
pin_reactions[node_location * 2 - 2][0] = 1 # The x transformion for the force on pin
master_matrix = np.hstack((master_matrix, pin_reactions))

pin_reactions = np.zeros( (number_of_equations, 1) ) # Creates an empty matrix where num of eqs is the number of rows, 1 is colum
pin_reactions[node_location * 2 - 1][0] = 1 # The y transformion for the force on pin
master_matrix = np.hstack((master_matrix, pin_reactions))
print("===========================================")

# Chose where the roller reaction force is
node_location = int(input("Enter node roller reaction\n"))
node_roller_reaction = list_of_nodes[node_location - 1]
roller_support = vp.sphere(pos = node_roller_reaction - vec(0 , 0.1 + 0.1, 0), radius=0.1,
                           texture = vp.textures.granite)

# Since node n and node p were choosen then in the element np, the force applied there
roller_reactions = np.zeros( (number_of_equations, 1) ) # Creates an empty matrix where num of eqs is the number of rows, 1 is colum
roller_reactions[node_location * 2 - 1][0] = 1 # The x transformion for the force on pin
coeffeicent_matrix = np.hstack((master_matrix, roller_reactions))


# LOOK THIS OVER
ground = vp.box(pos=roller_support.pos - vp.vec(roller_support.pos.x, roller_support.radius + 0.05, 0), 
                size=vp.vec(roller_support.pos.x * 2, 0.1 ,2), texture=vp.textures.wood)

pin_support = vp.pyramid(pos = vec(node_pin_reaction.x, ground.pos.y + 0.05, 0), 
                         size = vec(node_pin_reaction.y - ground.pos.y , 0.5, 0.5),
                         axis = vec(0, 1, 0), texture = vp.textures.granite)
print("===========================================")
#print("Coeffiecent matrix")
#print(coeffeicent_matrix)
#print("===========================================")

number_of_forces = int(input("Enter number of applied forces\n")) # Ask for number of nodes
print("--------------------------")

known_forces = np.zeros( (number_of_equations, 1) ) 
forces_visual = []
for x in arange(0, number_of_forces, 1):
    h = input(f"For force {x + 1} enter node number.\n")
    better_h = int(h) 
    
    node_location = list_of_nodes[better_h - 1]
    
    force_applied = float(input("Enter force value\n"))
    angle = radians(float(input("Enter angle of force\n")))

    x_1 = force_applied * cos(angle)
    
    if abs(x_1) < 0.1000:
        x_1 = 0
    
    y = force_applied * sin(angle)
    
    if abs(y) < 0.1000:
        y = 0
    
    position = vec(x_1, y, 0)
    #print(position)
    
    bp = node_location + hat(position)
    
    forces_visual.append(vp.arrow(pos = bp, axis = node_location - bp,
                                  color = 1/255 * vec(112, 41, 99), opacity = 0.75))
    #vp.label(pos = bp * 1.05, text = '<i>F</i>', height = 16, border = 4, font = 'monospace', 
    #         line = False, opacity = 0, box = False, color = 1/255 * vec(112, 41, 99))
    
    #print(forces_visual[x].pos)
    #print(forces_visual[x].axis)

    
    known_forces[better_h * 2 - 2][0] = 1 * x_1 # The x transformion for the force on the element AB from A
    known_forces[better_h * 2 - 1][0] = 1 * y # The y transformion for the force on the element AB from A
    print("--------------------------")
#print("Known forces matrix")
#print(known_forces)
print("===========================================")

print("Solution Matrix")

unknown_forces = (np.linalg.inv(coeffeicent_matrix)).dot(known_forces)

print(unknown_forces)
print("===========================================")

max_pos_force = np.amax(unknown_forces)
max_neg_force = np.amin(unknown_forces)

for x in arange(0, np.size(unknown_forces) - 3, 1):
    force = unknown_forces[x][0]
    force_abs = abs(unknown_forces[x][0])
    
    if  force > 0 and force > 0.000001:
        element_visual_list[x].color = force/max_pos_force * vec(0.8, 0, 0)
        print(f'Element {x + 1} has a force of {force_abs:.3f} and is in tension.')
    elif force < 0 and force < -0.000001:
        element_visual_list[x].color = force/max_neg_force * vec(0, 0, 0.8)
        print(f'Element {x + 1} has a force of {force_abs:.3f} and is in compression.')
    else:
        print(f'Element {x + 1} is a zero force memeber.')

text_1 = vp.wtext(text = "Blue elements mean in compression\n")

text_2 = vp.wtext(text = "Red elements mean in tension")

vp.sleep(5000)

sys.exit(0)