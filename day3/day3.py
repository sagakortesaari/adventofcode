f = open("input.txt", "r")
lines = f.readlines()
lines = [line.strip() for line in lines]

def day_3(right, downtwo):
    trees = 0
    x = 0
    everyother = True
    for line in lines:
        if not everyother and downtwo:
            everyother = True 
            continue
        if line[x] == "#":
            trees += 1
        x += right 
        if x >= len(line):
            x = x % len(line)
        everyother = False
    return trees



right1 = day_3(1, False)
right3 = day_3(3, False)
## Part 1
print(right3)
right5 = day_3(5, False)
right7 = day_3(7, False)
right1down2 = day_3(1, True)
## Part 2
print(right1*right3*right5*right7*right1down2)


        

            
            
            

            



