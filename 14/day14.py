f = open("input.txt", "r")
inputlines = f.readlines()
inputlines = [line.strip() for line in inputlines]

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
            temp_mask = mask
            binary_val = str(binary_val)
            result = ""
            for i in range(0,len(binary_val)):
                if temp_mask[i] == 'X':
                    result += binary_val[i]
                else:
                    result += temp_mask[i] 
            addresses[memory_address] = int(result,2)
    
    sum = 0
    for key in addresses:
        sum += addresses[key]
    return sum

res = part_1()
print("Part 1: " + str(res))