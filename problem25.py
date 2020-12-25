# Problem 25
# 26/12/2020

# input
file = open("input/input25.txt", 'r')
input = file.read().split('\n')
input[0] = int(input[0])
input[1] = int(input[1])

# PART ONE

transform_memo = dict()
    
def loop_size(public_key):
    counter = 0
    key = 1
    while key != public_key:
        key = (key * 7) % 20201227
        counter +=1
    return counter

key_loop_size = loop_size(input[0])
door_loop_size = loop_size(input[1])

answer_1 = 1
for i in range(door_loop_size):
    answer_1 = (answer_1 * input[0]) % 20201227

print("Answer: " + str(answer_1))

# PART TWO (unsolved)

print("PART TWO UNSOLVED")