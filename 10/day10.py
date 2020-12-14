f = open("input.txt", "r")
lines = f.readlines()
lines = [int(line.strip()) for line in lines]
alreadycalculated = {}

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

def part_2(adapter_jolts, max_distance = 3, curr = 0):
    if curr in alreadycalculated:
        return alreadycalculated[curr]

    if len(adapter_jolts) == 1:
        return 2

    elif len(adapter_jolts) == 0:
        return 0

    valids = 0

    withinrange = [adapter for adapter in adapter_jolts if adapter - curr <= 3]

    for elem in withinrange:
        valids += part_2(adapter_jolts[adapter_jolts.index(elem)+1:], curr = elem)
    
    alreadycalculated[curr] = valids
    
    return valids

print(part_2(sorted(lines)))