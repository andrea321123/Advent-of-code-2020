# Problem 20
# 20/12/2020

# input
file = open("input/input20.txt", 'r')
input = file.read().split("\n\n")
for i in range(len(input)):
    input[i] = input[i].split(':')
    input[i][0] = input[i][0].split()[1]
    input[i][1] = input[i][1][1:]
    input[i][1] = input[i][1].split('\n')

# PART ONE

# return a list with four string representing the edges of the matrix
def edges(matrix):
    return_list = []

    # up edge
    return_list.append(matrix[0])
    return_list.append(return_list[-1][::-1])

    # right edge
    tmp = ''
    for  i in matrix:
        tmp += i[-1]
    return_list.append(tmp)
    return_list.append(return_list[-1][::-1])

    # down edge
    return_list.append(matrix[-1])
    return_list.append(return_list[-1][::-1])

    # left edge
    tmp = ''
    for i in matrix:
        tmp += i[0]
    return_list.append(tmp)
    return_list.append(return_list[-1][::-1])

    return return_list

#map <tile, list of edges>
tile_to_edges = dict()
for i in input:
    tile_to_edges[i[0]] = edges(i[1])

# map <edge, list of tiles that have that edge>
edge_to_tiles = dict()
for i in tile_to_edges:
    edge_list = tile_to_edges[i]
    for j in edge_list:
        if j not in edge_to_tiles:
            edge_to_tiles[j] = [i]
        else:
            edge_to_tiles[j].append(i)

# corner tiles have unique edges
corner_tiles = set()
border_tiles = dict()
for i in edge_to_tiles:
    if len(edge_to_tiles[i]) == 1:
        if edge_to_tiles[i][0] not in border_tiles:
            border_tiles[edge_to_tiles[i][0]] = 1
        else:
            if border_tiles[edge_to_tiles[i][0]] == 3:
                corner_tiles.add(edge_to_tiles[i][0])
            else:
                border_tiles[edge_to_tiles[i][0]] +=1


# result of part one is the product of corner tiles
product = 1
for i in corner_tiles:
    product *= int(i)

print("Answer: " + str(product))

# PART TWO (unsolved)

print("PART TWO UNSOLVED")