# Problem 16
# 16/12/2020

# input
file = open("input/input16.txt", 'r')
input = file.read().split("\n\n")

ranges = input[0].split("\n")
for i in range(len(ranges)):
    ranges[i] = ranges[i].replace(" or ", ':').replace('\n', ':').split(':')
    for j in range(1, len(ranges[i])):
        ranges[i][j] = ranges[i][j].replace('-', ' ').split()
        ranges[i][j][0]= int(ranges[i][j][0])
        ranges[i][j][1]= int(ranges[i][j][1])


my_ticket = input[1].split('\n')[1].replace(',', ' ').split()
for i in range(len(my_ticket)):
    my_ticket[i] = int(my_ticket[i])

other_tickets = input[2].replace(',', ' ').split('\n')[1:]
for i in range(len(other_tickets)):
    other_tickets[i] = other_tickets[i].split()
    for j in range(len(other_tickets[i])):
        other_tickets[i][j] = int(other_tickets[i][j])

# PART ONE

# we create a set containing all valid values
valid_set = set()

for i in range(len(ranges)):
    for j in range(1, len(ranges[i])):
        for z in range(ranges[i][j][0], ranges[i][j][1]):
            if z not in valid_set:
                valid_set.add(z)

# we check the values not in the set
error_rate = 0
valid_tickets = []
for i in other_tickets:
    valid = True
    for j in i:
        if j not in valid_set:
            error_rate += j
            valid = False
    
    # useful for part 2
    if valid:
        valid_tickets.append(i)

print("Answer: " + str(error_rate))

# PART TWO

# we mantain a map of set based on each field (such as "departure location")
sets = dict()
for i in ranges:
    new_set = set()
    for j in range(1, len(i)):
        for z in range(i[j][0], i[j][1] +1):
            new_set.add(z)
    sets[i[0]] = new_set

# we mantain a map <field: column of the ticket>; default -1
field_to_column = dict()
for i in ranges:
    field_to_column[i[0]] = []

for i in range(len(valid_tickets[0])):          # for each column
    for z in range(len(ranges)):                # for each field

        valid = True
        for j in range(len(valid_tickets)):     # for each row
            if valid_tickets[j][i] not in sets[ranges[z][0]]:
                valid = False
                break

        if valid:
            field_to_column[ranges[z][0]].append(i)

# now we have to get the unique column for each field,
# which can be obtained by assign the field with only one valid
# column and remove the column from all the others field.
# At the end, each field should have only 1 column

end = False
already_removed = set()
while not end:
    end = True

    for i in field_to_column:
        if len(field_to_column[i]) == 1 and field_to_column[i][0] not in already_removed:
            already_removed.add(field_to_column[i][0])
            end = False

            # remove the column from all the other fields
            to_remove = field_to_column[i][0]
            for j in field_to_column:
                # check to not remove the column from the right field
                if len(field_to_column[j]) == 1 and field_to_column[j][0] == to_remove:
                    continue
                if to_remove in field_to_column[j]:
                    field_to_column[j].remove(to_remove)


# now we consider only the fields starting with 'departure'
result = 1
for i in field_to_column:
    if 'departure' in i:
        result *= my_ticket[field_to_column[i][0]]

print("Answer: " + str(result))