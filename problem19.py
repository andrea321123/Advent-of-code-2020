# Problem 19
# 19/12/2020

# input
file = open("input/input19.txt")
input = file.read().split("\n\n")
rules = input[0].split('\n')
input_strings = input[1].split('\n')

input_map = dict()
for i in rules:
    if 'a' in i or 'b' in i:
        formatted_rule = i.replace('"', '')
        formatted_rule = formatted_rule.replace(' ', '')
        formatted_rule = formatted_rule.split(':')
        input_map[formatted_rule[0]] = [formatted_rule[1]]
    else:       # list of rules
        formatted_rule = i.replace('|', ':')
        formatted_rule = formatted_rule.split(':')
        
        # remove spaces and split the rules
        for j in range(1, len(formatted_rule)):
            formatted_rule[j] = formatted_rule[j].split()
        
        input_map[formatted_rule[0]] = [[]] + formatted_rule[1:]

# PART ONE

# cartesian product of two lists
def product(list_1, list_2):
    result_list = []
    for i in list_1:
        for j in list_2:
            result_list.append(i + j)
    
    return result_list

# map <rule number, list of strings that match the rule>
rule_to_strings = dict()

# return a list of string that match the rule
def match(rule):
    # use memoization
    if rule in rule_to_strings:
        return rule_to_strings[rule]

    
    # base case: the rule is to match a single character
    if len(input_map[rule]) == 1:
        return [input_map[rule][0]]
    
    result_list = []
    for rules in input_map[rule][1:]:
        tmp = list()
        for single_rule in range(len(rules)):
            if single_rule == 0:
                tmp = match(rules[single_rule])
            else:
                tmp = product(tmp, match(rules[single_rule]))
        
        result_list += tmp
    
    rule_to_strings[rule] = result_list
    return rule_to_strings[rule]

# generate all possible strings
pool = set(match('0'))

# check if input string are in the pool
counter = 0
for i in input_strings:
    if i in pool:
        counter +=1

print("Answer: " + str(counter))

# PART TWO

result_1 = counter

# new rules
# 8: 42 | 42 8
# 11: 42 31 | 42 11 31

base_length = len(match('0')[0])

# create a list with strings that are longer than base_length
longer_strings = []
for i in input_strings:
    if len(i) > base_length:
        longer_strings.append(i)

rule_42 = match('42')
len_rule_42 = len(rule_42[0])
rule_31 = match('31')
len_rule_31 = len(rule_31[0])
rule_42 = set(match('42'))
rule_31 = set(match('31'))

# now each string must follow rule 11
def remove_31(string):
    # exit condition
    if string[-len_rule_31:] not in rule_31:
        return False
    counter = 0
    while len(string) > len_rule_31 and string[-len_rule_31:] in rule_31:
        string = string[:-len_rule_31]
        counter +=1
    
    return [string, counter]

def check_42(string, counter):
    if check_42_rec(string) > counter:
        return True
    
    return False

# return the number of substrings that follow rule 42
# or False if there's a substring that doesn't follow rule 42
def check_42_rec(string):
    # exit condition
    if string == '':
        return 0
    if len(string) < len_rule_42:
        return -1
    
    if string[:len_rule_42] in rule_42:
        tmp = check_42_rec(string[len_rule_42:])
        if tmp != -1:
            return 1 + tmp
    
    
    return False

counter = 0

for i in range(len(longer_strings)):
    longer_strings[i] = remove_31(longer_strings[i])
    if longer_strings[i] == False:
        continue
    
    if check_42(longer_strings[i][0], longer_strings[i][1]):
        counter +=1

print("Answer: " + str(result_1 + counter))