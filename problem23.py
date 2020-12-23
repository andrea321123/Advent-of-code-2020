# Problem 23
# 23/12/2020

# input
file = open("input/input23.txt", 'r')
input_string = file.read()
input = []
for i in input_string:
    input.append(int(i))

MOVES = 100

# implementing a linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    

# we create a linked list with head the value 1
i = 0
while (input[i] != 1):
    i += 1

head = Node(1)
current = None
previous = head
for j in range(i +1, len(input) +i):
    previous.next = Node(input[j % len(input)])
    previous = previous.next
    if j % len(input) == 0:
        current = previous
previous.next = head

# return the biggest number n that n < value and n not in removed_list
def lower_value(value, start_removed):
    if value == 1:
        return lower_value(len(input) +1, start_removed)
    
    tmp = start_removed
    for i in range(3):
        if tmp.value == value -1:
            return lower_value(value -1, start_removed)
        tmp = tmp.next
        
    return value -1

def solve(moves):
    global current
    for i in range(moves):
        start_removed = current.next
        end_removed = start_removed.next.next

        for j in range(3):
            current.next = current.next.next
    
        lower = lower_value(current.value, start_removed)

        previous_start_removed = current
        while previous_start_removed.value != lower:
            previous_start_removed = previous_start_removed.next

        current = current.next

        # we add the removed sublist after new current
        end_removed.next = previous_start_removed.next
        previous_start_removed.next = start_removed

solve(100)
tmp = head
result = ''
for i in range(len(input)):
    result += str(tmp.value)
    tmp = tmp.next
print("Answer: " + str(result[1:]))

# PART TWO (unsolved)

print("PART TWO UNSOLVED")