f = open("input.txt", "r")
inputlines = f.readlines()
inputlines = [line.strip() for line in inputlines]

def part_1():
    runningsum = 0
    for line in inputlines:
        def calc(seq):
            lastseennum = 0
            lastseenop = '+'
            count = 0
            index = 0
            while index < len(seq):
                if seq[index].isalnum():
                    currentnum = int(seq[index])
                else:
                    currentnum = None
                if seq[index] == ' ':
                    index += 1
                    continue
                if seq[index] == ')':
                    return index+1, count 
                if seq[index] == '(':
                    ind, res = calc(seq[index+1:])
                    currentnum = res
                    index += ind
                if lastseennum != None and currentnum != None:
                    if lastseenop == '+':
                        count = int(lastseennum) + currentnum
                    else:
                        count = int(lastseennum) * currentnum
                    lastseennum = count
                    index += 1
                    continue 
                if seq[index].isalnum():
                    lastseennum = seq[index] 
                else:
                    lastseenop = seq[index] 
                index += 1
            return count 
        runningsum += calc(line)
    return runningsum

print(part_1())
