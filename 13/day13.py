f = open("input.txt", "r")
inputlines = f.readlines()
inputlines = [line.strip() for line in inputlines]

def part_1():
    waitingtimes = {}
    timestamp = int(inputlines[0])
    bus_ids = [int(x) for x in inputlines[1].split(",") if x != "x"]
    for bus in bus_ids:
        diff = (-1 * (int(timestamp / bus) * bus)) % timestamp
        waitingtime = bus - diff
        waitingtimes[bus] = waitingtime
    pairs = waitingtimes.items()
    sortedpairs = sorted(pairs, key=lambda x: x[1])
    return sortedpairs[0][0] * sortedpairs[0][1]


def part_2():
    buses = inputlines[1].split(",")

    pairs = [(int(buses[i]), int(buses[i]) - i) for i in range(0, len(buses)) if buses[i] != "x"]

    # chinese number theorem
    # tried using a brute force solution at first, was impossible
    M = 1
    for num, m_i in pairs:
        M *= num

    total = 0
    for num, m_i in pairs:
        b = int(M / num)
        total += m_i * b * pow(b, num - 2, num)
        total %= M

    return total


res = part_1()
print(res)
res = part_2()
print(res)
