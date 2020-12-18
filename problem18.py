# Problem 18
# 18/12/2020

from enum import Enum

# input
file = open("input/input18.txt", 'r')
input = file.read().replace(' ', '').split('\n')

class Symbol(Enum):
    OPEN_BRACKET = 1
    CLOSE_BRACKET = 2
    CONSTANT = 3
    ADDITION = 4
    MULTIPLICATION = 5

# token =   (Symbol, value)
#           (CONSTANT, 135)
#           (OPEN_BRACKET, '(')

digits = ('0','1','2','3','4','5','6','7','8','9')

# return [number read, index of the char after the last digit of the number]
def read_number(string, i_start_number):
    number = string[i_start_number]
    i_start_number +=1

    while i_start_number < len(string) and string[i_start_number] in digits:
        number += string[i_start_number]
        i_start_number +=1
    
    return [int(number), i_start_number]

# return a list of tokens starting from a string
def lexing(string):
    token_list = []

    size = len(string)
    i = 0
    while i < size:
        char = string[i]
        if char in digits:      # it is a constant
            number = read_number(string, i)
            i = number[1] -1
            token_list.append((Symbol.CONSTANT, number[0]))
        else:                   # it isn't a constant
            if char == '(':
                token_list.append((Symbol.OPEN_BRACKET, '('))
            elif char == ')':
                token_list.append((Symbol.CLOSE_BRACKET, ')'))
            elif char == '+':
                token_list.append((Symbol.ADDITION, '+'))
            elif char == '*':
                token_list.append((Symbol.MULTIPLICATION, '*'))
        
        i +=1
    
    return token_list

class Tree:
    def __init__(self, token):
        self.token = token
        self.left = None
        self.right = None
    
    def solve(self):
        if self.token[0] == Symbol.CONSTANT:
            return self.token[1]
        
        # it is an operator
        if self.token[0] == Symbol.ADDITION:
            return self.left.solve() + self.right.solve()
        
        # it is a multiplication
        return self.left.solve() * self.right.solve()
    
    def to_string_rec(self, depth):
        ret = ''
        for _ in range(depth):
            ret += "  "
        ret += str(self.token) + "\n"

        if self.left != None:
            ret += self.left.to_string_rec(depth +1)
        if self.right != None:
            ret += self.right.to_string_rec(depth +1)
        
        return ret

    def to_string(self):
        return self.to_string_rec(0)

# PART ONE

def parsing_1(token_list, start, end):
    if start +1 == end:
        head = Tree(token_list[start])
        return head

    # split by the last operator
    bracket_count = 0
    last_operator_index = -1
    for i in range(start, end):
        if token_list[i][0] == Symbol.OPEN_BRACKET:
            bracket_count +=1
        elif token_list[i][0] == Symbol.CLOSE_BRACKET:
            bracket_count -=1
        elif token_list[i][0] == Symbol.ADDITION or token_list[i][0] == Symbol.MULTIPLICATION:
            if bracket_count == 0:
                last_operator_index = i
    
    # if no operator found, remove the brackets
    if last_operator_index == -1:
        return parsing_1(token_list, start +1, end -1)
        
    head = Tree(token_list[last_operator_index])
    head.left = parsing_1(token_list, start, last_operator_index)
    head.right = parsing_1(token_list, last_operator_index +1, end)

    return head
    
sum = 0
for i in input:
    token_list = lexing(i)
    ast = parsing_1(token_list, 0, len(token_list))
    sum += ast.solve()

print("Answer: " + str(sum))

# PART TWO

# same of parsing_1 but with operator precedences
def parsing_2(token_list, start, end):
    if start +1 == end:
        head = Tree(token_list[start])
        return head

    # split by the last operator
    bracket_count = 0
    last_addition_index = -1
    last_multiplication_index = -1
    for i in range(start, end):
        if token_list[i][0] == Symbol.OPEN_BRACKET:
            bracket_count +=1
        elif token_list[i][0] == Symbol.CLOSE_BRACKET:
            bracket_count -=1
        elif token_list[i][0] == Symbol.ADDITION:
            if bracket_count == 0:
                last_addition_index = i
        elif token_list[i][0] == Symbol.MULTIPLICATION:
            if bracket_count == 0:
                last_multiplication_index = i
    
    # if no operator found, remove the brackets
    if last_addition_index == -1 and last_multiplication_index == -1:
        return parsing_2(token_list, start +1, end -1)
    
    # if no multiplication found, split by the addition
    if last_multiplication_index == -1:
        head = Tree(token_list[last_addition_index])
        head.left = parsing_2(token_list, start, last_addition_index)
        head.right = parsing_2(token_list, last_addition_index +1, end)
        return head

    # split by the multiplication
    head = Tree(token_list[last_multiplication_index])
    head.left = parsing_2(token_list, start, last_multiplication_index)
    head.right = parsing_2(token_list, last_multiplication_index +1, end)
    return head

sum = 0
for i in input:
    token_list = lexing(i)
    ast = parsing_2(token_list, 0, len(token_list))
    sum += ast.solve()

print("Answer: " + str(sum))