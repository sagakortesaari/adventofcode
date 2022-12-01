f = open("input.txt", "r")
inputlines = f.readlines()
inputlines = [line.strip() for line in inputlines]

def add(binary_val, temp_mask, result, character):
    for i in range(0,len(binary_val)):
        if temp_mask[i] == character:
            result += binary_val[i]
        else:
            result += temp_mask[i] 
    return result 

def part_1():
    mask = 0
    addresses = {}
    for line in inputlines:
        res = line.split("=")
        operand = res[0][0:-1]
        value = res[1][1:]
        if operand == 'mask':
            mask = value
        else:
            memory_address = int(operand[4:-1])
            binary_val = (bin(int(value))[2:]).zfill(36)
            binary_val = str(binary_val)
            result = ""
            result = add(binary_val, mask, result, 'X')
            addresses[memory_address] = int(result,2)
    
    sum = 0
    for key in addresses:
        sum += addresses[key]
    return sum

def part_2():
    mask = 0 
    addresses = {}
    for line in inputlines:
        res = line.split("=")
        operand = res[0][0:-1]
        value = res[1][1:]
        if operand == 'mask':
            mask = value
        else:
            memory_address = bin(int(operand[4:-1]))[2:].zfill(36)
            address = add(memory_address, mask, "", '0')
            num_x = address.count('X')
            highest_bin = "1" * num_x
            counter = 0
            current_bin = 0
            while int(current_bin) <= int(highest_bin):
                current_bin = bin(counter)[2:].zfill(num_x)
                temp_address = address
                for i in range(0,num_x):
                    index = temp_address.find('X')
                    temp_address = temp_address[0:index] + current_bin[i] + temp_address[index+1:]
                addresses[temp_address] = value
                counter += 1
    sum = 0
    for key in addresses:
        sum += int(addresses[key])
    return sum

res = part_1()
print("Part 1: " + str(res))
res = part_2()
print("Part 2: " + str(res))