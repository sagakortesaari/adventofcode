f = open("input.txt", "r")
lines = f.readlines()
lines = [line.strip() for line in lines]

def part_1(lines):
    parameters = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    res = set()
    count = 0
    for i in range(0,len(lines)):
        line = lines[i].split()
        if len(line) < 1:
            res.clear()
            continue
        for i in range(0,len(line)):
            param = line[i].split(":")
            if param[0] == "cid":
                continue
            else:
                res.add(param[0])
            if res == parameters:
                count += 1
    return count


def part_2(lines):
    parameters = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    res = set()
    eyecolors = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
    count = 0

    for i in range(0,len(lines)):
        line = lines[i].split()
        if len(line) < 1:
            res.clear()
            continue
        for i in range(0,len(line)):
            param = line[i].split(":")
            if param[0] == "byr":
                if int(param[1]) < 1920 or int(param[1]) > 2002:
                    continue 
            if param[0] == "iyr":
                if int(param[1]) < 2010 or int(param[1]) > 2020:
                    continue
            if param[0] == "eyr":
                if int(param[1]) < 2020 or int(param[1]) > 2030:
                    continue
            if param[0] == "hgt":
                if "cm" in param[1]:
                    new = param[1].split("c")
                    if int(new[0]) < 150 or int(new[0]) > 193:
                        continue 
                elif "in" in param[1]:
                    new = param[1].split("i")
                    if int(new[0]) < 59 or int(new[0]) > 76:
                        continue
                else:
                    continue
            if param[0] == "hcl":
                if "#" in param[1]:
                    if not param[1][1:].isalnum():
                        continue
                else:
                    continue
            if param[0] == "ecl":
                if not param[1] in eyecolors:
                    continue
            if param[0] == "pid":
                if len(param[1]) != 9:
                    continue
            if param[0] == "cid":
                continue
            else:
                res.add(param[0])
            if res == parameters:
                count += 1
    return count

#part 1
print(part_1(lines))
#part 2
print(part_2(lines))