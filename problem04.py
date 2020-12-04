# Problem 4
# 4/12/2020

# input
file = open("input/input04.txt", "r")
input = file.readlines()

passports = []
single_passport = []
for i in input:
    if i == "\n":       # end of passport
        passports.append(single_passport.copy())
        single_passport = []
    else:
        line = i.split()
        for j in line:
            key_value = j.split(":")
            single_passport.append(key_value)
passports.append(single_passport)

# PART ONE
counter = 0
valid_passports = []        # useful for part two
for i in passports:
    if len(i) == 8:         # valid passport
        counter +=1
        valid_passports.append(i)
    if len(i) == 7:      # valid North Pole Credentials
        # check if cid is not present
        cid = False
        for j in i:
            if j[0] == "cid":
                cid = True
                break
        
        if not cid:
            counter +=1
            valid_passports.append(i)

print("Answer: " + str(counter))

# PART TWO

counter = 0
for i in valid_passports:
    # check if each field of the passport is correct
    valid = True
    for j in i:
        if j[0] == "byr":
            year = int(j[1])
            if year < 1920 or year > 2002:
                valid = False
        elif j[0] == "iyr":
            issue = int(j[1])
            if issue < 2010 or issue > 2020:
                valid = False
        elif j[0] == "eyr":
            expiration = int(j[1])
            if expiration < 2020 or expiration > 2030:
                valid = False
        elif j[0] == "hgt":
            unit = j[1][-2:]
            if unit != "in" and unit != "cm":
                valid = False
            else:
                size = int(j[1][:-2])
                if unit == "cm":
                    if size < 150 or size > 193:
                        valid = False
                else:
                    if size < 59 or size > 76:
                        valid = False
        elif j[0] == "hcl":
            if len(j[1]) == 7 and j[1][0] == "#":
                for z in j[1][1:]:
                    if z not in ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']:
                        valid = False
            else:
                valid = False
        elif j[0] == "ecl":
            if j[1] not in ["amb","blu","brn","gry","grn","hzl","oth"]:
                valid = False
        elif j[0] == "pid":
            if len(j[1]) != 9:
                valid = False
            else:
                for z in j[1]:
                    if z not in ['0','1','2','3','4','5','6','7','8','9']:
                        valid = False

    if valid:
        counter +=1

print("Answer: " + str(counter))