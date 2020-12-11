f = open("input.txt", "r")
lines = f.readlines()
lines = [int(line.strip()) for line in lines]

def part_1():
    adapter_jolts = sorted(lines)
    previous = 0
    onejoltdiff = 0
    threejoltdiff = 0

    while len(adapter_jolts) > 0:
        adapter = adapter_jolts.pop(0)
        difference = adapter - previous
        previous = adapter
        if difference == 3:
            threejoltdiff += 1
        else:
            onejoltdiff += 1

    return onejoltdiff * (threejoltdiff + 1)

print(part_1())
