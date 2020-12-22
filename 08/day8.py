f = open("input.txt", "r")
lines = f.readlines()
lines = [line.strip() for line in lines]

def part_1(lines):
    acc = 0
    used = set()
    line = 0

    while line < len(lines):
        if line in used:
            return None, acc
        res = lines[line].split(" ")
        if res[0] == 'acc':
            acc += int(res[1])
            used.add(line)
        
        if res[0] == 'jmp':
            used.add(line)
            line += int(res[1])
            continue 
        line += 1
    return True, acc

print("Part 1: " + str(part_1(lines)[1]))

def part_2():
    line = 0

    while line < len(lines):
        res = lines[line].split(" ")
        if res[0] == 'jmp':
            lines[line] = lines[line].replace("jmp", "nop")
            res = part_1(lines)
            if res[0] != None:
                return res[1]
            else:
                lines[line] = lines[line].replace("nop", "jmp")
        elif res[0] == 'nop':
            lines[line] = lines[line].replace("nop", "jmp")
            res = part_1(lines)
            if res[0] != None:
                return res[1]
            else:
                lines[line] = lines[line].replace("jmp", "nop")
        line += 1


print("Part 2: " + str(part_2()))