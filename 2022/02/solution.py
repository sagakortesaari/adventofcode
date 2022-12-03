def check_win(m1, m2):
  win = {
    "Paper": "Rock",
    "Scissors": "Paper",
    "Rock": "Scissors"
  }

  if m1 == m2:
    return 3
  
  if m1 == win[m2]:
    return 6 
  
  return 0

def handle_outcome(m1, outcome):
  win = {
    "Rock": "Paper",
    "Paper": "Scissors",
    "Scissors": "Rock"
  }

  lose = {
    "Paper": "Rock",
    "Scissors": "Paper",
    "Rock": "Scissors"
  }

  if outcome == "Z":
    return win[m1], 6
  elif outcome == "X":
    return lose[m1], 0
  else:
    return m1, 3

def count_points(lines):
  moves_dict = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors",
    "X": "Rock",
    "Y": "Paper",
    "Z": "Scissors"
  }

  points_dict = {
    "Rock": 1,
    "Paper": 2,
    "Scissors": 3
  }

  # Part 1
  first_score = 0
  for line in lines:
      moves = line.split()
      elf_move = moves_dict[moves[0]]
      my_move = moves_dict[moves[1]]
      first_score += points_dict[my_move]
      first_score += check_win(elf_move, my_move)

  # Part 2
  second_score = 0
  for line in lines: 
    moves = line.split()
    elf_move = moves_dict[moves[0]]
    outcome = moves[1]
    result = handle_outcome(elf_move, outcome)
    second_score += result[1]
    second_score += points_dict[result[0]]

  return first_score, second_score

with open("input.txt", "r") as f:
  lines = f.readlines()

result = count_points(lines)
print("Part 1: The total score you would get by following the strategy guide would be", result[0], "points!")
print("Part 2: The total score you would get by following the strategy guide would be", result[1], "points!")
