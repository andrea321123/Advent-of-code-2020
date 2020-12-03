# Problem 3
# 3/12/2020

# return the number of trees encountered with
#  a slope of [down] down, [right] right
def tree_number(down, right):
    x_pos = 0
    y_pos = 0
    len_x = len(input[0])
    len_y = len(input)
    counter = 0

    # loop cycle
    while (True):
        x_pos = (x_pos + right) % len_x
        y_pos +=down

        # exit condition
        if y_pos >= len_y:
            break

        # check if we encountered a tree
        if input[y_pos][x_pos] == "#":
            counter +=1
    
    return counter

# input
file = open("input/input03.txt")
input = file.read()
input = input.split()

# PART ONE

print("Answer: " + str(tree_number(1, 3)))

# PART TWO

result = 1

result *= tree_number(1, 1)
result *= tree_number(1, 3)
result *= tree_number(1, 5)
result *= tree_number(1, 7)
result *= tree_number(2, 1)

print("Answer: " + str(result))