# Problem 5
# 5/12/2020

# return the ID of a seat (row *8 + column)
def get_id(seat):
    return seat[0] *8 + seat[1]

# input
file = open("input/input05.txt")
input = file.read().split()
for i in range(len(input)):
    # we split the row from the position
    tmp = []
    tmp.append(input[i][:7])
    tmp.append(input[i][-3:])
    input[i] = tmp

# int_input is like input, buth with a decimal represantion of strings
char_to_bit = {'B':1, 'F':0, 'R':1, 'L':0}
int_input = []
for i in range(len(input)):
    seat = []
    row, column = 0, 0

    # obtain the row
    for j in range(len(input[i][0])):
        row += char_to_bit[input[i][0][j]] << (len(input[i][0]) -1) -j

    # obtain the column
    for j in range(len(input[i][1])):
        column += char_to_bit[input[i][1][j]] << (len(input[i][1]) -1) -j
    
    # we add the result to int_input
    seat.append(row)
    seat.append(column)
    int_input.append(seat)

# PART ONE

id_list = []    # sorted list of all IDs

for i in int_input:
    id_list.append(get_id(i))

id_list.sort()
print("Answer: " + str(id_list[-1]))    # the biggest of all IDs

# PART TWO

# since id_list is sorted, we have to find two numbers id[i] and id[i +1] 
# that id[i] == id[i +1] -2; id[i] +1 will be our ID
for i in range(len(id_list) -1):
    if id_list[i] == id_list[i +1] -2:
        print("Answer: " + str(id_list[i] +1))
        break