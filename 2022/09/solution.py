def check_grid(head, tail):
    grid = set()

    for row in range(head[0]-1, head[0]+2):
        for col in range(head[1]-1, head[1]+2):
            grid.add((row,col))

    if tail in grid:
        return True 
    else:
        return False

def check_row_col(head, tail):
    if head[0] == tail[0] or head[1] == tail[1]:
        return True 
    return False

def move(direction, x):
    x_x, x_y = x
    if direction == "L":
        x = (x_x - 1, x_y)
    elif direction == "U":
        x = (x_x, x_y - 1)
    elif direction == "R":
        x = (x_x + 1, x_y)
    elif direction == "D":
        x = (x_x, x_y + 1)
    
    return x

def check_hor_direction(head, tail):
    move = ""
    if head[1] < tail[1]: # head = (1, -2), tail = (3, -3)
        if head[0] > tail[0]:
            move = "NE"
        else:
            move = "NW"
    else:
        if head[0] > tail[0]:
            move = "SE"
        else:
            move = "SW"
    return move

def check_direction(head, tail):
    dir = ""
    if head[0] < tail[0]:
        dir = "L"
    elif head[0] > tail[0]:
        dir = "R"
    elif head[1] < tail[1]:
        dir = "U"
    else:
        dir = "D"
    
    return dir

def move_tail(head, tail):

    if not check_grid(head, tail):
        if check_row_col(head, tail): 
            tail = move(check_direction(head, tail), tail)
        else: 
            dir = check_hor_direction(head, tail)
            tail_x, tail_y = tail 
            if dir == "NE":
                tail = (tail_x + 1, tail_y - 1)
            elif dir == "NW":
                tail = (tail_x - 1, tail_y - 1)
            elif dir == "SE":
                tail = (tail_x + 1, tail_y + 1)
            elif dir == "SW":
                tail = (tail_x - 1, tail_y + 1)
    
    return tail

def solve_p1(lines):
    head_pos = (0,0)
    tail_pos = (0,0)
    positions = set()
    positions.add(tail_pos)

    for line in lines:
        res = line.split(" ")
        direction = res[0]
        steps = int(res[1])

        for i in range(0, steps):
            head_pos = move(direction, head_pos)
            prev_pos = tail_pos
            tail_pos = move_tail(head_pos, tail_pos)

            if prev_pos != tail_pos:
                positions.add(tail_pos)
    
    return len(positions)

def solve_p2(lines):
    head = (0,0)
    knots = [(0,0) for i in range(0,9)]
    positions = set()
    positions.add((0, 0))

    for line in lines:
        res = line.split(" ")
        direction = res[0]
        steps = int(res[1])

        for i in range(0, steps):
            head = move(direction, head)

            for knot in range(0,len(knots)):
                if knot == 0:
                    knots[knot] = move_tail(head, knots[knot])
                elif knot == 8:
                    prev_knot_pos = knots[knot]
                    knots[knot] = move_tail(knots[knot-1], knots[knot])
                    if knots[knot] != prev_knot_pos:
                        positions.add(knots[knot])
                else:
                    knots[knot] = move_tail(knots[knot-1], knots[knot])

    
    return len(positions)

with open("input.txt", "r") as f:
  lines = [l.strip() for l in f.readlines()]

print("Part 1: The amount of unique positions that the tail visits is", solve_p1(lines), "positions")
print("Part 2: The amount of unique positions that the tail visits is", solve_p2(lines), "positions")