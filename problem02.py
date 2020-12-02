# Problem 2
# 2/12/2020

# input
file = open("input/input02.txt", "r")
input = file.read().split("\n")
for i in range(len(input)):
    input[i] = input[i].replace("-", " ")
    input[i] = input[i].replace(":", " ")
    input[i] = input[i].split()
# input format
# input[i][0] = min
# input[i][1] = max
# input[i][2] = char
# input[i][3] = string

# PART ONE

counter = 0
for i in input:
    min = int(i[0])
    max = int(i[1])
    char = i[2]
    string = i[3]

    # check if count >= min and count <= max
    char_in_string = string.count(char)
    if char_in_string >= min and char_in_string <= max:
        counter +=1

print("Answer: " + str(counter))

# PART TWO

counter = 0
for i in input:
    index_0 = int(i[0]) -1
    index_1 = int(i[1]) -1
    char = i[2]
    string = i[3]

    # check if string[only one of the indexes] == char
    valid = False
    if string[index_0] == char:
        valid = not valid
    if string[index_1] == char:
        valid = not valid    
    if valid:
        counter += 1

print("Answer: " + str(counter))