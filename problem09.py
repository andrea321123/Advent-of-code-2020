# Problem 9
# 9/12/2020

file = open("input/input09.txt")
input = file.read().split()
for i in range(len(input)):
    input[i] = int(input[i])

# PART ONE

OFFSET = 25

queue = []
part_one_solution = 0

# init the queue
for i in range(OFFSET):
    for j in range(i +1, OFFSET):
        queue.append(input[i] + input[j])

for i in range(OFFSET, len(input)):
    # check if number is valid
    if input[i] not in queue:
        print("Answer: " + str(input[i]))
        part_one_solution = input[i]
        break

    # remove the sums with the input[i - OFFSET] numbers
    for j in range((i - OFFSET) +1, i):
        queue.remove(input[(i - OFFSET)] + input[j])
    
    # add the sums with the new number
    for j in range((i - OFFSET) +1, i):
        queue.append(input[j] + input[i])

# PART TWO

to_find = part_one_solution

for i in range(len(input)):
    offset = 1
    sum = input[i]
    while sum < to_find:
        sum += input[i + offset]
        offset +=1
    
    if sum == to_find:
        # get the sublist and sort it
        sublist = input[i: i + offset]
        sublist.sort()
        
        print("Answer: " + str(sublist[0] + sublist[-1]))
        break

