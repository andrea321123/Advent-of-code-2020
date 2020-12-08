# Problem 8
# 8/12/2020

# input
file = open("input/input08.txt")
input = file.read().split("\n")
for i in range(len(input)):
    input[i] = input[i].split()

# PART ONE

# return a list [accumulator, program_finished]
def run():
    accumulator = 0
    pointer = 0
    visited = set()

    while (pointer not in visited) and (pointer < len(input)):
        visited.add(pointer)

        # execute instruction
        if input[pointer][0] == "acc":
            accumulator += int(input[pointer][1])
        elif input[pointer][0] == "jmp":
            pointer += int(input[pointer][1]) -1    # later we'll pointer++
        
        pointer +=1
    
    if pointer >= len(input):
        return [accumulator, True]
    
    return [accumulator, False]

print("Answer: " + str(run()[0]))

# PART TWO

# we try to invert each nop and jmp instruction
for i in range(len(input)):
    if input[i][0] == "nop":
        input[i][0] = "jmp"
        if run()[1] == True:
            print("Answer: " + str(run()[0]))
            break
        input[i][0] = "nop"     # set the old value
    elif input[i][0] == "jmp":
        input[i][0] = "nop"
        if run()[1] == True:
            print("Answer: " + str(run()[0]))
            break
        input[i][0] = "jmp"     # set the old value