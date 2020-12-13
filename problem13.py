# Problem 13
# 13/12/2020

import math

file = open("input/input13.txt")
start_time = int(file.readline())
input = file.read().split(',')

# PART ONE
time_list = []  # contains the minutes of the first time it can get each bus

for i in input:
    if i == 'x':
        continue
    
    id = int(i)
    time_list.append([id, math.ceil(start_time / id) * id])

# choose the min time from time list
time_min = time_list[1]
for i in time_list:
    if i[1] < time_min[1]:
        time_min = i

print("Answer: " + str((time_min[1] - start_time) * time_min[0]))

# PART TWO
# WARNING: very slow (can take several hours)

i_max = 0
tmp_max = int(input[0])
bus_list = []

for i in range(len(input)):
    if input[i] == 'x':
        continue

    input[i] = int(input[i])
    if input[i] > tmp_max:
        tmp_max = input[i]
        i_max = i
    
    # append [input[i], i] to the list
    bus_list.append([input[i], i])

# we remove the biggest from the list
bus_list.remove([tmp_max, i_max])

# we check if possible value until we find the right one
i = tmp_max
while (True):
    without_offset = i - i_max
    valid = True

    for j in range(len(bus_list)):
        if (without_offset + bus_list[j][1]) % bus_list[j][0] != 0:
            valid = False
            break
    
    # check if the value is correct
    if (valid):
        print("Answer: " + str(without_offset))
        break

    # increment i
    i += tmp_max
