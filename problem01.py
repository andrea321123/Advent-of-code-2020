# Problem 1
# 1/12/2020

file = open("input/input01.txt", "r")
input = file.read().split()

TO_OBTAIN = 2020
HALF = int(TO_OBTAIN /2)
is_even = TO_OBTAIN % 2 == 0

# PART ONE

# create two lists: one contains all input numbers <= TO_OBTAIN/2
# the others stay in the input list
for i in range(len(input)):
    input[i] = int(input[i])
input.sort()

small_list = []
big_list = []
while input[0] <= HALF:
    small_list.append(input.pop(0))
big_list = input.copy()

found = False
result = 0

# edge case: there are at least two values HALF
if is_even and small_list.count(HALF) >= 2:
    found = True
    result = HALF **2

for i in range(len(small_list)):
    if found:
        break

    # we check if small_list[i] + big_list[j] == TO_OBTAIN
    j = 0
    while small_list[i] + big_list[j] < TO_OBTAIN:
        j +=1
    if small_list[i] + big_list[j] == TO_OBTAIN:
        found = True
        result = small_list[i] * big_list[j]
        break

if found:
    print("Answer: " + str(result))
else:
    print("Answer not found")

# PART TWO

found = False

# we first heck if the 3 number are all in small_list;
# the we check if two numbers are in small_list and one is in big_list
for i in range(len(small_list)):
    if found:
        break
    for j in range(i, len(small_list)):
        if found:
            break
        for z in range(j, len(small_list)):
            if found:
                break
            # look in small_list
            if small_list[i] + small_list[j] + small_list[z] == TO_OBTAIN:
                found = True
                result = small_list[i] * small_list[j] * small_list[z]
                break

            # look in big_list
            needed = TO_OBTAIN - (small_list[i] + small_list[j])
            if big_list.count(needed) > 0:
                found = True
                result = small_list[i] * small_list[j] * needed
                break

if found:
    print("Answer: " + str(result))
else:
    print("Answer not found")