# Problem 22
# 22/12/2020

from queue import Queue

# input 
file = open("input/input22.txt", 'r')
input = file.read().split("\n\n")
input[0] = input[0].split('\n')[1:]
input[1] = input[1].split('\n')[1:]
for i in range(len(input)):
    for j in range(len(input[i])):
        input[i][j] = int(input[i][j])

# PART ONE

def score(queue):
    score = 0
    multiplier = queue.qsize()
    while not queue.empty():
        score += queue.get() * multiplier
        multiplier -= 1
    return score

max_size = len(input[0]) + len(input[1])
queue_1 = Queue(maxsize=max_size)
queue_2 = Queue(maxsize=max_size)
turns = 0

for i in input[0]:
    queue_1.put(i)
for i in input[1]:
    queue_2.put(i)

while not queue_1.empty() and not queue_2.empty():
    card_1 = queue_1.get()
    card_2 = queue_2.get()

    if card_1 > card_2:
        queue_1.put(card_1)
        queue_1.put(card_2)
    else:
        queue_2.put(card_2)
        queue_2.put(card_1)
    
    turns +=1

if queue_1.empty():
    print("Answer: " + str(score(queue_2)))
else:
    print("Answer: " + str(score(queue_1)))

# PART TWO (unsolved)

print("PART TWO UNSOLVED")