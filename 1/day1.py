f = open("input.txt", "r")
lines = f.readlines()
lines = [int(line.strip("\n")) for line in lines]

#part 2
def multiplyThree():
    for l0 in lines:
        for l1 in lines: 
            for l2 in lines:
                if l0 + l1 + l2 == 2020:
                    return(l0 * l1 * l2)

#part 1
def multiplyTwo():
    for line in lines:
        remainder = 2020 - int(line)
        if remainder in lines: 
            return remainder * line

print(multiplyTwo())
print(multiplyThree())