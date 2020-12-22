f = open("input.txt", "r")
lines = f.readlines()
lines = [line.strip() for line in lines]

def two_sum(list, target):
    previous = {}

    for i in range(0,len(list)):
        remainder = int(target) - int(list[i])
        if remainder in previous:
            return True 
        else:
            previous[int(list[i])] = int(list[i])
    return False 

def part_1():
    preamble_index = 0
    check_index = 25

    while check_index < len(lines):
        check = two_sum(lines[preamble_index:check_index], lines[check_index])
        if check:
            check_index += 1
            preamble_index += 1
        else:
            return lines[check_index]

def part_2(target):
    for i in range(0,len(lines)):
        curr_sum = int(lines[i])

        j = i+1

        while j < len(lines):
            curr_sum += int(lines[j])
            if curr_sum == target:
                arr = lines[i:j+1]
                maximum = int(max(arr))
                minimum = int(min(arr))
                return maximum + minimum
            j+= 1


num = int(part_1())
print("Part 1: " + str(num))
print("Part 2: " + str(part_2(num)))


