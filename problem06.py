# Problem 6
# 6/12/2020

# input
file = open("input/input06.txt")
input_str = file.readlines()
input = []
group = []
for i in input_str:
    if i == "\n":
        input.append(group.copy())
        group = []
    else:
        i = i.replace("\n", "")
        group.append(i)
input.append(group.copy())

# PART ONE

counter = 0

# we create a set for each group, add all the letters to the set
# and increment the counter of len(set)
set_list = []       # useful for part two
for group in input:
    group_set = set()
    for person in group:
        for letter in person:
            group_set.add(letter)
    
    counter += len(group_set)       # increment the result
    set_list.append(group_set)

print("Answer: " + str(counter))

# PART TWO

counter = 0

# for each group we create a map {letter: nTimes it appears}
# this way we know that if a value in the map is len(group[i]),
# we have to increase counter
for i in range(len(input)):
    group_dict = dict()

    # add each element of the set in the dict
    for j in set_list[i]:
        group_dict[j] = 0
    
    # increment nTimes for each letter
    for person in input[i]:
        for letter in person:
            group_dict[letter] +=1
        
    # we increment the counter for each letter that group_dict[letter] = len(input[i])
    group_size = len(input[i])
    for j in group_dict:
        if group_dict[j] == group_size:
            counter +=1

print("Answer: " + str(counter))
