# Problem 17
# 17/12/2020

# input
file = open("input/input17.txt", "r")
input = file.read().split("\n")

# PART ONE

STEPS = 6

cubes = set()
new_cubes = set()

# returns the number of cubes near (i, j, z)
def neighbors(i, j, z):
    count = 0
    global cubes

    for index_i in range(i -1, i +2):
        for index_j in range(j -1, j +2):
            for index_z in range(z -1, z +2):
                if index_i == i and index_j == j and index_z == z:
                    continue
                if (index_i, index_j, index_z) in cubes:
                    count += 1

    return count

def update():
    new_cubes = set()
    visited = set()     # contains a set of visited coordinates
    global cubes

    # for each cube we visit the cube itself and each neighbour
    for cube in cubes:
        i = cube[0]
        j = cube[1]
        z = cube[2]
        for index_i in range(i -1, i +2):
            for index_j in range(j -1, j +2):
                for index_z in range(z -1, z +2):
                    cube_tuple = (index_i, index_j, index_z)
                    if cube_tuple in visited:
                        continue
                    visited.add(cube_tuple)

                    count = neighbors(index_i, index_j, index_z)
                    
                    if cube_tuple in cubes: # it is a cube
                        if count == 2 or count == 3:
                            new_cubes.add(cube_tuple)
                    else:       # it is an empty space
                        if count == 3:
                            new_cubes.add(cube_tuple)
    
    cubes = new_cubes

# init cubes
for i in range(len(input)):
    for j in range(len(input[i])):
        if input[i][j] == '#':
            cubes.add((i, j, 0))

for i in range(STEPS):
    update()

print("Answer: " + str(len(cubes)))

# PART TWO

# same of part one, but with four dimensions

cubes = set()
new_cubes = set()

# returns the number of cubes near (i, j, z)
def neighbors_2(i, j, z, w):
    count = 0
    global cubes

    for index_i in range(i -1, i +2):
        for index_j in range(j -1, j +2):
            for index_z in range(z -1, z +2):
                for index_w in range(w -1, w +2):
                    if index_i == i and index_j == j and index_z == z and index_w == w:
                        continue
                    if (index_i, index_j, index_z, index_w) in cubes:
                        count += 1

    return count

def update_2():
    new_cubes = set()
    visited = set()     # contains a set of visited coordinates
    global cubes

    # for each cube we visit the cube itself and each neighbour
    for cube in cubes:
        i = cube[0]
        j = cube[1]
        z = cube[2]
        w = cube[3]
        for index_i in range(i -1, i +2):
            for index_j in range(j -1, j +2):
                for index_z in range(z -1, z +2):
                    for index_w in range(w -1, w +2):
                        cube_tuple = (index_i, index_j, index_z, index_w)
                        if cube_tuple in visited:
                            continue
                        visited.add(cube_tuple)

                        count = neighbors_2(index_i, index_j, index_z, index_w)
                    
                        if cube_tuple in cubes: # it is a cube
                            if count == 2 or count == 3:
                                new_cubes.add(cube_tuple)
                        else:       # it is an empty space
                            if count == 3:
                                new_cubes.add(cube_tuple)
    
    cubes = new_cubes

# init cubes
for i in range(len(input)):
    for j in range(len(input[i])):
        if input[i][j] == '#':
            cubes.add((i, j, 0, 0))

for i in range(STEPS):
    update_2()

print("Answer: " + str(len(cubes)))