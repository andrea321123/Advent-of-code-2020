# Problem 7
# 7/12/2020

# input
file = open("input/input07.txt")
input = file.read().split("\n")
input_map = dict()
for i in range(len(input)):
    split_list = input[i].split()
    
    # input will be saved as a map {bag: list_of_bags}
    key = split_list[0] + " " + split_list[1]       # bag color
    value = []
    if ('no' not in split_list):
        offset = 4
        while offset != len(split_list):
            bag_description = split_list[offset +1] +" "+ split_list[offset +2]
            bag_number = int(split_list[offset])
            bag = [bag_number, bag_description]
            value.append(bag)
            offset +=4
    input_map[key] = value

target = "shiny gold"

# PART ONE

memo = dict()

# return if bag [bag] contains bag target (shiny gold)
def contains_target(bag):
    # using memoization
    if bag in memo:
        return memo[bag]

    bag_list = input_map[bag]
    for i in bag_list:
        # direct check
        if (target in i):
            memo[bag] = True
            return True
        
        # indirect check
        if contains_target(i[1]):
            memo[bag] = True
            return True
    
    memo[bag] = False
    return False

counter = 0
for i in input_map:
    if contains_target(i):
        counter +=1

print("Answer: " + str(counter))


# PART TWO

memo = dict()

# return the number of bags contained in [bag]
def bags_in(bag):
    # using memoization
    if bag in memo:
        return memo[bag]

    n = 0

    for i in input_map[bag]:
        n += i[0]                   # direct bags contained
        n += i[0] * bags_in(i[1])   # indirect bags contained
    
    memo[bag] = n
    return n

print("Answer: " + str(bags_in(target)))