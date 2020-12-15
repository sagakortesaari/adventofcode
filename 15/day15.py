input = [20,9,11,0,1,2]

def day_15(num):
    turn = 1
    lastspokennums = {}
    lastspoken = 0
    while turn <= num:
        if turn <= len(input):
            lastspokennums[input[turn-1]] = [turn]
            lastspoken = input[turn-1]
        else:
            if len(lastspokennums[lastspoken]) == 1:
                lastspoken = 0
            else:
                lastspoken = (turn-1) - lastspokennums[lastspoken][len(lastspokennums[lastspoken]) - 2]
            if lastspoken in lastspokennums:
                lastspokennums[lastspoken].append(turn)
            else:
                lastspokennums[lastspoken] = [turn]
        turn += 1
    return lastspoken 

part_1 = day_15(2020)
part_2 = day_15(30000000)
print("Part 1: " + str(part_1))
print("Part 2: " + str(part_2))


