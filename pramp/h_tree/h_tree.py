x = 0
y = 0
length = 3
depth = 2

def h_tree(center_x, center_y, length, depth):
    if depth == 0: return
    #Define the coords to pass to h_line
    distance = length/2
    h_line([(center_x-distance, center_y), (center_x+distance, center_y)])
    h_line([(center_x-distance, center_y+distance), (center_x-distance, center_y-distance)])
    h_line([(center_x+distance, center_y+distance), (center_x+distance, center_y-distance)])

    #New 4 centers
    new_length = length/(2**0.5)
    print("-------------------")
    h_tree(center_x - distance, center_y + distance, new_length, depth-1)
    h_tree(center_x - distance, center_y - distance, new_length, depth-1)
    h_tree(center_x + distance, center_y + distance, new_length, depth-1)
    h_tree(center_x + distance, center_y - distance, new_length, depth-1)

def h_line(*args):
    print(*args)

h_tree(x, y, length, depth)

