# Problem 11
# 11/12/2020

# input
file = open("input/input11.txt", "r")
input = file.read().split("\n")

# PART ONE

def update_square_1(i, j, occupied_limit):
    if list_now[i][j] == 'L':
        if count_adjacent_1(i, j, '#') == 0:
            return '#'
    if list_now[i][j] == '#':
        if count_adjacent_1(i, j, '#') >= occupied_limit:
            return 'L'
    
    # if arrive here, we don't have to update the square
    return list_now[i][j]
    

# return the number of adjacent chars == [character]   
def count_adjacent_1(i, j, character):
    count = 0

    for index_i in range(i -1, i +2):
        if index_i >= len_i or index_i < 0:
            continue

        for index_j in range(j -1, j +2):
            if index_j >= len_j or index_j < 0:
                continue
            if index_i == i and index_j == j:
                continue
            
            if list_now[index_i][index_j] == character:
                count +=1
    
    return count

list_now = input.copy()
list_next = []
len_i = len(input)
len_j = len(input[0])

# do-while loop 
while True:
    list_next = list()
    updated = False

    # we create the next state in a list_next, then we copy list_next in list_now
    for i in range(len(input)):
        string = ""
        for j in range(len(input)):
            string += update_square_1(i, j, 4)
            if string[j] != list_now[i][j]:
                updated = True
        
        list_next.append(string)
    
    list_now = list_next.copy()
    if not updated:
        break

# count occupied seats
def seats_occupied():
    counter = 0

    for i in range(len_i):
        for j in range(len_j):
            if list_now[i][j] == '#':
                counter +=1
    return counter

print ("Answer: " + str(seats_occupied()))

# PART TWO

def print_list(l):
    for  i in l: 
        print(i)

def update_square_2(i, j, occupied_limit, l):
    if l[i][j] == 'L':
        if count_adjacent_2(i, j, '#', l) == 0:
            return '#'
    if l[i][j] == '#':
        if count_adjacent_2(i, j, '#', l) >= occupied_limit:
            return 'L'
    
    # if arrive here, we don't have to update the square
    return l[i][j]

def count_adjacent_2(i, j, character, l):
    count = 0
    
    i_pos, j_pos = i, j -1
    while j_pos >= 0:   # left
        if l[i_pos][j_pos] == character:
            count +=1
            break
        if l[i_pos][j_pos] == "L":
            break
        j_pos -=1
    i_pos, j_pos = i, j +1
    while j_pos < len_j:   # right
        if l[i_pos][j_pos] == character:
            count +=1
            break
        if l[i_pos][j_pos] == "L":
            break
        j_pos +=1
    i_pos, j_pos = i -1, j
    while i_pos >= 0:   # up
        if l[i_pos][j_pos] == character:
            count +=1
            break
        if l[i_pos][j_pos] == "L":
            break
        i_pos -=1
    i_pos, j_pos = i +1, j
    while i_pos < len_i:   # down
        if l[i_pos][j_pos] == character:
            count +=1
            break
        if l[i_pos][j_pos] == "L":
            break
        i_pos +=1
    
    i_pos, j_pos = i -1, j -1
    while j_pos >= 0 and i_pos >= 0:   # left up
        if l[i_pos][j_pos] == character:
            count +=1
            break
        if l[i_pos][j_pos] == "L":
            break
        j_pos -=1
        i_pos -=1
    i_pos, j_pos = i -1, j +1
    while j_pos < len_j and i_pos >= 0:   # right up
        if l[i_pos][j_pos] == character:
            count +=1
            break
        if l[i_pos][j_pos] == "L":
            break
        j_pos +=1
        i_pos -=1
    i_pos, j_pos = i +1, j -1
    while j_pos >= 0 and i_pos < len_i:   # left down
        if l[i_pos][j_pos] == character:
            count +=1
            break
        if l[i_pos][j_pos] == "L":
            break
        j_pos -=1
        i_pos +=1
    i_pos, j_pos = i +1, j +1
    while j_pos < len_j and i_pos < len_i:   # right down
        if l[i_pos][j_pos] == character:
            count +=1
            break
        if l[i_pos][j_pos] == "L":
            break
        j_pos +=1
        i_pos +=1

    return count

list_now = input.copy()
list_next = list()

# do-while loop 
while True:
    list_next = list()
    updated = False
    # we create the next state in a list_next, then we copy list_next in list_now
    for i in range(len(input)):
        string = ""
        for j in range(len(input)):
            string += update_square_2(i, j, 5, list_now)
            if string[j] != list_now[i][j]:
                updated = True
        
        list_next.append(string)
    
    list_now = list_next.copy()
    if not updated:
        break

print ("Answer: " + str(seats_occupied()))