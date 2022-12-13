def count_trees_p1(lines):
    count = 0

    count += 2*(len(lines) - 2) # Add the outer trees 
    count += 2*len(lines[0]) # Add the outer trees

    counted_trees = set()

    for row in range(1,len(lines)-1): # Count trees from left -> right
        previous = lines[row][0]
        for col in range(1,len(lines[row])-1):
            if lines[row][col] > previous:
                counted_trees.add((row, col))
                previous = lines[row][col]
    
    col_length = len(lines[0]) - 1
    
    for row in range(1,len(lines)-1): # Count trees from right -> left
        previous = lines[row][col_length]
        for col in range(col_length - 1, 0, -1):
            if lines[row][col] > previous:
                counted_trees.add((row, col))
                previous = lines[row][col]
    
    for col in range(1, len(lines[0]) - 1): # Count trees up -> down
        previous = lines[0][col]
        for row in range(1, len(lines) - 1):
            if lines[row][col] > previous:
                counted_trees.add((row, col))
                previous = lines[row][col]

    row_length = len(lines) - 1

    for col in range(1, col_length): # Count trees down -> up
        previous = lines[row_length][col]
        for row in range(row_length - 1, 0, -1):
            if lines[row][col] > previous:
                counted_trees.add((row, col))
                previous = lines[row][col]

    return len(counted_trees) + count


def count_direction(start, lines):
    north = 0
    south = 0
    west = 0
    east = 0

    start_tree = lines[start[0]][start[1]]

    for row in range(start[0] - 1, -1, -1): # Count north 
        current_tree = lines[row][start[1]]
        north += 1 

        if current_tree == start_tree or current_tree > start_tree:
            break
    
    for row in range(start[0] + 1, len(lines)): # Count south
        current_tree = lines[row][start[1]]
        south += 1

        if current_tree == start_tree or current_tree > start_tree:
            break

    for col in range(start[1] + 1, len(lines[0])): # Count east
        current_tree = lines[start[0]][col]
        east += 1

        if current_tree == start_tree or current_tree > start_tree:
            break
    
    for col in range(start[1] - 1, -1, -1): # Count west
        current_tree = lines[start[0]][col]
        west += 1

        if current_tree == start_tree or current_tree > start_tree:
            break

    return north * south * west * east 


def count_trees_p2(lines):
    tree_scores = []

    for line in range(1,len(lines)-1):
        for col in range(1, len(lines[0])-1):
            score = count_direction((line, col), lines)
            tree_scores.append(score)
    
    return max(tree_scores)

with open("input.txt", "r") as f:
  lines = [l.strip() for l in f.readlines()]

print("Part 1: The amount of trees visible from the outside grid is", count_trees_p1(lines))
print("Part 2: The highest scenic score possible is", count_trees_p2(lines))