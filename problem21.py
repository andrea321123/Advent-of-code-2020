# Problem 21
# 21/12/2020

# input
file = open("input/input21.txt", 'r')
input = file.read().split('\n')
for i in range(len(input)):
    input[i] = input[i].replace(',', ' ').replace(')', '').split("(contains ")
    input[i][0] = set(input[i][0].split())
    input[i][1] = set(input[i][1].split())

# PART ONE

input_c = input.copy()

# we create a set of allergens
allergens = set()
for i in input_c:
    for j in i[1]:
        if j not in allergens:
            allergens.add(j)

allergens_c = list(allergens.copy())
allergens_c.sort()
allergen_to_ingredient = dict()

def print_allergens():
    for allergen in allergens:
        same_allergen = []
        for i in range(len(input_c)):
            if allergen in input_c[i][1]:
                same_allergen.append([i, set(input_c[i][0])])

        intersection = same_allergen[0][1]  
        for i in range(1, len(same_allergen)):
            intersection = intersection.intersection(same_allergen[i][1])

for n in range(len(allergens)):
    # we search if there are unique ingredients between foods with the same allergen
    for allergen in allergens:
        same_allergen = []
        for i in range(len(input_c)):
            if allergen in input_c[i][1]:
                same_allergen.append([i, set(input_c[i][0])])

        intersection = same_allergen[0][1]  
        for i in range(1, len(same_allergen)):
            intersection = intersection.intersection(same_allergen[i][1])
    
        # if len(intersection) == 1, we remove the allergen from all foods
        if len(intersection) == 1:
            food = list(intersection)[0]
            for i in input_c:
                if food in i[0]:
                    i[0].remove(food)
                if allergen in i[1]:
                    i[1].remove(allergen)
            allergens.remove(allergen)
            allergen_to_ingredient[allergen] = food
            break

# get the number of ingredients left
counter = 0
for i in input_c:
    counter += len(i[0])

print("Answer: " + str(counter))

# PART TWO

answer = ''
for i in allergens_c:
    answer += allergen_to_ingredient[i] + ','
answer = answer[:-1]

print("Answer: " + answer)