import math 

def monkey_business(lines, part):

    monkeys = []
    monkey_dict = {}

    for i in range(0, len(lines), 7):
        monkeys.append(lines[i:i+7])

    for i in range(0, len(monkeys)):
        monkey = {}
        monkey['items'] = monkeys[i][1][len('Starting items:'):].replace(" ", "").split(",")
        monkey['operation'] = monkeys[i][2][len('Operation: '):][len('new = '):]
        monkey['test'] = int(monkeys[i][3][len('Test: divisible by '):])
        monkey['true'] = int(monkeys[i][4][len('If true: throw to monkey '):])
        monkey['false'] = int(monkeys[i][5][len('If false: throw to monkey '):])
        monkey['count'] = 0
        monkey_dict[i] = monkey
    
    mod_all = 1
    for div_by in [m['test'] for m in monkey_dict.values()]:
        mod_all *= div_by
    
    if part == "1":
        amount = 20
    else:
        amount = 10000

    for i in range(0, amount):
        for monkey in monkey_dict.keys():
            items = monkey_dict[monkey]['items']
            for item in items:
                monkey_dict[monkey]['count'] += 1
                #print("item", item)
                old = int(item)
                worry = eval(monkey_dict[monkey]['operation'])

                if part == "1":
                    worry = math.floor(worry / 3)
                else:
                    worry = worry % mod_all

                monkey_dict[monkey]['items'] = monkey_dict[monkey]['items'][1:]
                if worry % monkey_dict[monkey]['test'] == 0:
                    monkey_dict[monkey_dict[monkey]['true']]['items'].append(worry)
                else:
                    monkey_dict[monkey_dict[monkey]['false']]['items'].append(worry)
    
    worry_levels = []
    for monkey in monkey_dict.keys():
        worry_levels.append(monkey_dict[monkey]['count'])
    worry_levels.sort(reverse = True)
    return worry_levels[0] * worry_levels[1]

with open("input.txt", "r") as f:
  lines = [l.strip() for l in f.readlines()]

print("Part 1: The level of monkey business after 20 rounds is", monkey_business(lines, '1'))
print("Part 2: The level of monkey business after 20 rounds is", monkey_business(lines, '2'))

