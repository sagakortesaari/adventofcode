f = open("input.txt", "r")
lines = f.readlines()
lines = [line.strip() for line in lines]

def part_1():
    total = []
    questions = set()
    for line in lines:
        if len(line) == 0:
            total.append(len(questions))
            questions.clear()
        for i in range(0,len(line)):
            questions.add(line[i])
    return(sum(total))

def part_2():
    total = []
    sets = [] 

    for line in lines:
        if len(line) == 0:
            intersection = set.intersection(*sets)
            total.append(len(intersection))
            sets.clear()
            continue
        
        tempset = set()
        for i in range(0,len(line)):
            tempset.add(line[i])
        sets.append(tempset)
    return sum(total)
            
print(part_1()) 
print(part_2())