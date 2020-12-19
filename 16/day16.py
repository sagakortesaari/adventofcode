f = open("input.txt", "r")
inputlines = f.readlines()
inputlines = [line.strip() for line in inputlines]

def fix_valids():
    valids = {}
    for line in range(0,20):
        parts = [l.strip() for l in inputlines[line].split(":")]
        name = parts[0]
        allowed_values = [l.strip() for l in parts[1].split("or")]
        allowed_values = [numpair.split("-") for numpair in allowed_values]
        valids[name] = allowed_values
    return valids

def part_1(valids):
    invalids = 0
    invalidrows = set()
    for line in inputlines[25:]:
        nums = line.split(",")
        for num in nums:
            found = False 
            for key in valids:
                r = valids[key]
                if (int(r[0][0]) <= int(num) <= int(r[0][1])) or (int(r[1][0]) <= int(num) <= int(r[1][1])):
                    found = True 
                    break
            if not found:
                invalids += int(num)
                invalidrows.add(line)
    return invalids, invalidrows

def part_2(invalidrows, valids):
    columns = {}

    while len(valids) > 0:
        column = 0
        results = {}
        while column < len(inputlines[25].split(",")):
            counted = {}
            for row in range(0,len(inputlines[25:])):
                if inputlines[25+row] in invalidrows:
                    continue
                value = int(inputlines[25+row].split(",")[column]) 
                for key in valids:       
                    r = valids[key]
                    if (int(r[0][0]) <= value <= int(r[0][1])) or (int(r[1][0]) <= value <= int(r[1][1])):
                        if key in counted:
                            counted[key] += 1
                        else:
                            counted[key] = 1
            for key in counted:
                if counted[key] == (len(inputlines[25:]) - len(invalidrows)):
                    if column in results:
                        results[column].append(key)
                    else: 
                        results[column] = [key]
            column += 1
        for key in results:
            if len(results[key]) == 1:
                columns[key] = results[key][0]
                del valids[results[key][0]]
        
    val = 1
    ticket = inputlines[22].split(",")
    for key in columns:
        if "departure" in columns[key]:
            val *= int(ticket[key])
    return val
        
valids = fix_valids()
print(("Part 1: " + str(part_1(valids)[0])))
invalidrows = (part_1(valids)[1])
print("Part 2: " + str(part_2(invalidrows, valids)))
