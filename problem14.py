# Problem 14
# 14/12/2020

file = open("input/input14.txt", "r")
input = file.read().replace('[',' ').replace(']',' ').replace('=',' ').splitlines()
for i in range(len(input)):
    input[i] = input[i].split()

# PART ONE

def setBit(int_type, offset):
    mask = 1 << offset
    return(int_type | mask)

def clearBit(int_type, offset):
    mask = ~(1 << offset)
    return(int_type & mask)

# returns a list [or-mask, and-mask] 
# or only or_mask if and_mask is not needed
def get_masks(mask_str, need_and_mask):
    or_mask = 0
    and_mask = 0b111111111111111111111111111111111111

    # replace bits in the masks
    for i in range(len(mask_str)):
        if mask_str[i] == '0':
            if need_and_mask:
                and_mask = clearBit(and_mask, len(mask_str) - i -1)
        elif mask_str[i] == '1':
            or_mask = setBit(or_mask, len(mask_str) - i -1)
    
    if need_and_mask:
        return [or_mask, and_mask]
    
    return or_mask

# apply [or_mask, and_mask] on number
def apply_masks(number, masks):
    return (number & masks[1]) | masks[0]

masks = []
memory = dict()

# run the initialization program
for i in input:
    if i[0] == "mask":
        masks = get_masks(i[1], True)
    if i[0] == "mem":
        if i[1] not in memory:
            memory[i[1]] = 0    # create new memory cell
        memory[i[1]] = apply_masks(int(i[2]), masks)

sum = 0
for i in memory:
    sum += memory[i]

print("Answer: " + str(sum))

# PART TWO

def perm(address, mask, offset):
    for i in range(offset, len(mask)):
        if mask[i] == 'X':
            return_list = perm(clearBit(address, len(mask) - i -1), mask, i +1)
            return_list += perm(setBit(address, len(mask) - i -1), mask, i +1)
            return return_list
    return [address]

# return a list of addresses based on the address and the mask
def get_masked_addresses(address, mask):
    or_mask = get_masks(mask, False)
    address = address | or_mask

    # now we have to generate all permutations of address based on mask
    return perm(address, mask, 0)

mask = ''
memory = dict()
for i in input:
    if i[0] == 'mask':
        mask = i[1]
    if i[0] == "mem":
        addresses_list = get_masked_addresses(int(i[1]), mask)
        for j in addresses_list:
            if j not in memory:
                memory[j] = 0
            memory[j] = int(i[2])

sum = 0
for i in memory:
    sum += memory[i]

print("Answer: " + str(sum))