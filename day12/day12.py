f = open("input.txt", "r")
inputlines = f.readlines()
inputlines = [line.strip() for line in inputlines]

def part_1():
    facing = 'east'
    current_degree = 0
    facing_degrees = {0: 'east', 90: 'north', 180: 'west', 270: 'south'}
    y = 0
    x = 0

    for line in inputlines:
        action = line[0]
        value = int(line[1:])
        if action == 'L':
            current_degree = (current_degree + value) % 360
            facing = facing_degrees[current_degree]
        if action == 'R':
            current_degree = (current_degree - value) % 360
            facing = facing_degrees[current_degree]
        if action == 'N':
            y += value 
        if action == 'S':
            y -= value 
        if action == 'E':
            x += value 
        if action == 'W':
            x -= value 
        if action == 'F':
            if facing == 'north':
                y += value 
            elif facing == 'south':
                y -= value 
            elif facing == 'west':
                x -= value 
            elif facing == 'east':
                x += value 
    return abs(x) + abs(y)

def part_2():
    way_y = 1
    way_x = 10
    ship_x = 0
    ship_y = 0

    for line in inputlines:
        action = line[0]
        value = int(line[1:])
        if action == 'L':
            for i in range(0,int(value/90)):
                temp = way_x 
                way_x = -1*way_y 
                way_y = temp

        if action == 'R':
            for i in range(0,int(value/90)):
                temp = way_x 
                way_x = way_y 
                way_y = -1*temp

        if action == 'N':
            way_y += value 
        if action == 'S':
            way_y -= value 
        if action == 'E':
            way_x += value 
        if action == 'W':
            way_x -= value 
        if action == 'F':
            ship_y += value*way_y
            ship_x += value*way_x
    return abs(ship_x) + abs(ship_y)    

res = part_1()
print("Part 1: " + str(res))
res = part_2()
print("Part 2: " + str(res))

        