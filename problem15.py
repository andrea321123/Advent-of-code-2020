# Problem 15
# 15/12/2020

# input
file = open("input/input15.txt", "r")
input = file.read().split(",")
for i in range(len(input)):
    input[i] = int(input[i])

# PART ONE

UPPER_BOUND_1 = 2020

def solve(upper_bound):
    # map <number: last turn where the number was spoken>
    numbers = dict()
    last_spoken = 0
    first_time = True

    for i in range(len(input)):
        numbers[input[i]] = i +1
        last_spoken = input[i]

    for i in range(len(input) +1, upper_bound +1):
        # it is a new number
        if first_time:
            last_spoken = 0
            if last_spoken in numbers:
                first_time = False
            else:
                numbers[last_spoken] = i
        else:   # not a new number
            tmp = (i -1) - numbers[last_spoken]
            numbers[last_spoken] = i -1     # update the turn of the spoken value

            last_spoken = tmp               # update last spoken

            if last_spoken not in numbers:
                first_time = True
                numbers[last_spoken] = i
    
    return last_spoken
    
print("Answer: " + str(solve(UPPER_BOUND_1)))

# PART TWO
# solution needs 20-30 seconds

UPPER_BOUND_2 = 30000000
print("Answer: " + str(solve(UPPER_BOUND_2)))