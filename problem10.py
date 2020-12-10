# Problem 10
# 10/12/2020

# input
file = open("input/input10.txt")
input = file.read().split()
for i in range(len(input)):
    input[i] = int(input[i])
input_sort = input.copy()
input_sort.sort()
input_sort = [0] + input_sort       # charging outlet has 0 jolts

# PART ONE
counter_1 = 0
counter_3 = 1       # built-in voltage adapter

for i in range(len(input_sort) -1):
    difference = input_sort[i +1] - input_sort[i]

    # increment a counter
    if difference == 1:
        counter_1 +=1
    elif difference == 3:
        counter_3 +=1

print("Answer: " + str(counter_1 * counter_3))

# PART TWO

memo = dict()

# count the ways a given sorted list can be arranged 
def many_ways(sort_list):
    # using memoization
    list_to_str = str(sort_list)
    if list_to_str in memo:
        return memo[list_to_str]

    # exit condition
    if len(sort_list) <= 1:
        return 1

    ways = 0
    i = 1

    # we recall many_ways with each possible sublist
    while i < len(sort_list) and sort_list[0] +3 >= sort_list[i]:
        ways += many_ways(sort_list[i:])
        i +=1
    
    memo[list_to_str] = ways
    return memo[list_to_str]

print("Answer: " + str(many_ways(input_sort)))