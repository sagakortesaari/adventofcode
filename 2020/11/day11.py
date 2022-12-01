f = open("input.txt", "r")
inputlines = f.readlines()
inputlines = [line.strip() for line in inputlines]

def checkAdjacent(rownum, seatnum, seatlist):
    last = len(seatlist[rownum]) - 1
    lastrow = len(seatlist) - 1
    first = 0 
    count = 0

    if seatnum != last and seatlist[rownum][seatnum+1] == '#':
        count += 1
    if seatnum != first and seatlist[rownum][seatnum-1] == '#':
        count += 1
    if rownum != first and seatnum != last and seatlist[rownum-1][seatnum+1] == '#':
        count += 1
    if rownum != first and seatnum != first and seatlist[rownum-1][seatnum-1] == '#':
        count += 1
    if rownum != first and seatlist[rownum-1][seatnum] == '#':
        count += 1
    if rownum != lastrow and seatlist[rownum+1][seatnum] == '#':
        count += 1
    if rownum != lastrow and seatnum != last and seatlist[rownum+1][seatnum+1] == '#':
        count += 1
    if rownum != lastrow and seatnum != first and seatlist[rownum+1][seatnum-1] == '#':
        count += 1
    return count 

def checkAdjacent2(rownum, seatnum, seatlist):
    last = len(seatlist[rownum]) - 1
    lastrow = len(seatlist) - 1
    first = 0 
    count = 0

    for i in range(-1,2):
        for j in range(-1,2):
            counter = 1
            if i == 0 and j == 0:
                continue
            while first <= rownum + counter*i <= lastrow and first <= seatnum + counter*j <= last:
                if seatlist[rownum + counter*i][seatnum + counter*j] == '#':
                    count += 1
                    break
                elif seatlist[rownum + counter*i][seatnum + counter*j] == 'L':
                    break
                else:
                    counter += 1
    return count

def day_11(lines, part, limit):
    copy = lines[0:]
    for i in range(0,len(lines)):
        for j in range(0,len(lines[i])):
            if lines[i][j] == '.':
                continue
            if part == 1:
                count = checkAdjacent(i, j, lines)
            else:
                count = checkAdjacent2(i, j, lines)
            if count == 0 and lines[i][j] == 'L':
                line = copy[i]
                line = line[0:j] + '#' + line[j+1:]
                copy[i] = line
            if lines[i][j] == '#':
                if count >= limit:
                    line = copy[i]
                    line = line[0:j] + 'L' + line[j+1:]
                    copy[i] = line
    if copy == lines:
        return copy
    return day_11(copy, part, limit)


def count_occupied(res):
    count = 0
    for line in res:
        for seat in line:
            if seat == '#':
                count += 1 
    return count

result = day_11(inputlines, 1, 4)
print("Part 1 " + str(count_occupied(result)))
result = day_11(inputlines, 2, 5)
print("Part 2 " + str(count_occupied(result)))
