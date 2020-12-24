# Problem 24
# 24/12/2020

# input
file = open("input/input24.txt", 'r')
input = file.read().split('\n')
coords = []
for i in input:
    tmp = list()
    j = 0
    while j < len(i):
        if i[j] == 's':
            j += 1
            if i[j] == 'e':         # se
                tmp.append("se")
            elif i[j] == 'w':       # sw
                tmp.append("sw")
        elif i[j] == 'n':
            j += 1
            if i[j] == 'e':         # ne
                tmp.append("ne")
            elif i[j] == 'w':       # nw
                tmp.append("nw")
        elif i[j] == 'e':           # e
                tmp.append("e")
        elif i[j] == 'w':           # w
                tmp.append("w")
        
        j +=1
    coords.append(tmp)

# for each line we flip a tile
# to represent tiles, we use cubic representation 
# (https://www.redblobgames.com/grids/hexagons/#coordinates)
black_tiles = set()
for i in coords:
    x, z, y, = 0, 0, 0
    for j in i:
        if j == "e":
            z += 1
            y -= 1
        elif j == "se":
            x -=1
            z +=1
        elif j == "w":
            z -=1
            y +=1
        elif j == "sw":
            x -=1
            y +=1
        elif j == "nw":
            x +=1
            z -=1
        elif j == "ne":
            x +=1
            y -=1
    
    coords_tuple = (x, z, y)
    if coords_tuple not in black_tiles:
        black_tiles.add(coords_tuple)
    else:
        black_tiles.remove(coords_tuple)

print("Answer: " + str(len(black_tiles)))

# PART TWO

# return a list of all adjacent hexagons
def adjacent(x, z, y):
    adjacent_list = []
    adjacent_list.append((x,z-1,y+1))
    adjacent_list.append((x-1,z,y+1))
    adjacent_list.append((x-1,z+1,y))
    adjacent_list.append((x,z+1,y-1))
    adjacent_list.append((x+1,z,y-1))
    adjacent_list.append((x+1,z-1,y))
    return adjacent_list


# return the number of black tiles adjacent the (x, z, y) hexagon
def black_adjacent(x, z, y):
    adjacent_hex = adjacent(x, z, y)

    counter = 0
    for i in adjacent_hex:
        if i in black_tiles:
            counter +=1
    
    return counter

# return the new configuration of black tiles
def update():
    new_black_tiles = set()
    black_to_check = set()
    white_to_check = set()

    # we add all black tiles to check in black_to_check
    for i in black_tiles:
        black_to_check.add(i)
    
    # add also the adjacent hex to each black hex
    for i in black_tiles:
        tmp = adjacent(i[0], i[1], i[2])
        for j in tmp:
            if j not in white_to_check:
                white_to_check.add(j)
    
    for i in black_to_check:
        n_adjacent = black_adjacent(i[0], i[1], i[2])
        if not (n_adjacent == 0 or n_adjacent > 2):
            new_black_tiles.add(i)
    
    for i in white_to_check:
        n_adjacent = black_adjacent(i[0], i[1], i[2])
        if n_adjacent == 2:
            new_black_tiles.add(i)
    
    return new_black_tiles

print("Answer: " + str(len(black_tiles)))