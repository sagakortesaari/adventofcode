def check_cycle(cycle, x):
    if (cycle-20) % 40 == 0:
        return cycle * x

    return 0

def check_x(cycle, x):
    c = (cycle - 1) % 40

    if x-1 <= c <= x+1:
        return True 
    
    return False


def count_signal_strength(lines):
    x = 1
    cycle = 0
    signal_strength_sum = 0
    letters = ""

    for line in lines:

        if line[0:4] == "noop":
            cycle += 1
            signal_strength_sum += check_cycle(cycle, x)
            if check_x(cycle, x):
                letters += "#"
            else:
                letters += " "
        else:
            val = line.split(" ")

            for i in range(0, 2):
                cycle += 1
                signal_strength_sum += check_cycle(cycle, x)
                if check_x(cycle, x):
                    letters += "#"
                else:
                    letters += " "

                if i == 1:
                    x += int(val[1])
    
    return signal_strength_sum, letters

with open("input.txt", "r") as f:
  lines = [l.strip() for l in f.readlines()]

day10 = count_signal_strength(lines)
print("Part 1: The sum of the signal strengths is", day10[0])

letters = ""
for i in range(0,len(day10[1])):
    if i % 40 == 0:
        letters += "\n"
    letters += day10[1][i]

print("Part 2: The solution is:", "\n", letters)