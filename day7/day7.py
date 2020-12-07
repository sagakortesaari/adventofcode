f = open("input.txt", "r")
lines = f.readlines()
lines = [line.strip() for line in lines]


def part_1():
    dict_of_bags = {}
    count = 0

    for line in lines:
        bags = line.split("contain")
        bag = bags[0].split("bags")
        bag = bag[0][0:-1]
        contains = bags[1]
        contains = contains[0:-1]
        contains = contains.split(",")
        arr = []
        for b in contains:
            b = b[3:]
            arr.append(b)
        dict_of_bags[bag] = arr
        # print(dict_of_bags[bag])

    def find_bag(name):
        count = 0
        shiny_gold = set()
        for bag in dict_of_bags:
            for b in dict_of_bags[bag]:
                if b[-1] == "s":
                    b = b[0:-1]
                if b[0:-4] == name:
                    shiny_gold.add(bag)
                    shiny_gold.update(find_bag(bag))
        return shiny_gold

    return len(find_bag("shiny gold"))


def part_2():
    dict_of_bags = {}

    for line in lines:
        bags = line.split("contain")
        bag = bags[0].split("bags")
        bag = bag[0][0:-1]
        contains = bags[1]
        contains = contains[0:-1]
        contains = contains.split(",")
        arr = []
        bagcount = {}
        for b in contains:
            if b[-1] == "s":
                b = b[0:-1]
            bagcount[b[3:-4]] = b[1]
            arr.append(bagcount)
        dict_of_bags[bag] = bagcount

    def find_bag(bag, count):
        amount = 0
        bags = dict_of_bags[bag]
        for bag in bags:
            if bags[bag] == "n":
                return 0
            amount += count * int(bags[bag])
            amount += find_bag(bag, count * int(bags[bag]))
        return amount

    return find_bag("shiny gold", 1)


print("Part 1: " + str(part_1()))
print("Part 2: " + str(part_2()))
