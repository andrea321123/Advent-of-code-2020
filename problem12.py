# Problem 12
# 12/12/2020

# input
file = open("input/input12.txt")
input = file.read().split("\n")

char_to_int = {'L':-1,'R':1,'E':0,'S':1,'W':2,'N':3}

# PART ONE

# returns a list with ['M', direction, increment]
# or a list with ['R', rotation]
# or a list with ['F', increment]
# M: move
# R: rotate
# F: front
def decode_input(string):
    if string[0] in ['L', 'R']:
        return ['R', int((char_to_int[string[0]] * int(string[1:])) /90)]
    if string[0] == 'F':
        return ['F', int(string[1:])]
    
    # if arrives here it is move in a direction
    return ['M', char_to_int[string[0]], int(string[1:])]

def manhattan_distance(dir):
    return abs(dir[0] - dir[2]) + abs(dir[1] - dir[3])

pointer = 0     # contains the actual direction (starting from east)
directions = [0, 0, 0, 0]   # contains the units walked in that direction

for i in input:
    decoded = decode_input(i)
    if decoded[0] == 'F':
        directions[pointer] += decoded[1]
    elif decoded[0] == 'M':
        directions[decoded[1]] += decoded[2]
    elif decoded[0] == 'R':
        pointer = (pointer + decoded[1]) %4

print("Answer: " + str(manhattan_distance(directions)))

# PART TWO

pointer = 0
ship_dir = [0, 0, 0, 0]

# relative position with 2 coordinates [E/W, S/N], E,S > 0, W,N < 0
waypoint_dir = [10, 0, 0, 1]     # relative position of the waypoint

for i in input:
    decoded = decode_input(i)
    if decoded[0] == 'R':       # rotate
        if decoded[1] > 0:      # rotate right
            for i in range(decoded[1]):
                waypoint_dir.insert(0, waypoint_dir.pop(len(waypoint_dir) -1))
        else:                   # rotate left
            for i in range(-decoded[1]):
                waypoint_dir.append(waypoint_dir.pop(0))
    elif decoded[0] == 'M':     # move
        waypoint_dir[decoded[1]] += decoded[2]
    elif decoded[0] == 'F':     # front (move ship)
        for i in range(len(waypoint_dir)):
            if waypoint_dir[i] != 0:
                ship_dir[i] += waypoint_dir[i] * decoded[1]

print("Answer: " + str(manhattan_distance(ship_dir)))
