from curses.ascii import isupper
from tabnanny import check


def check_priority(c):
  if isupper(c):
    return ord(c) - 65 + 27
  
  return ord(c) - 96


def count_rucksack(lines):
  priority_sum = 0

  for line in lines:
    middle = int(len(line) / 2)
    first = set(line[0:middle])
    second = set(line[middle:])
   
    same = first.intersection(second)
    
    priority_sum += check_priority("".join(same))
  
  return priority_sum

def count_badges(lines):

  badge_sum = 0

  for i in range(0,int(len(lines)/3)):
    group = lines[i*3:i*3+3]
    first = set(group[0])
    second = set(group[1])
    third = set(group[2])
    same = first.intersection(second).intersection(third)
    badge_sum += check_priority("".join(same))
  
  return badge_sum


with open("input.txt", "r") as f:
  lines = [l.strip() for l in f.readlines()]

print("Part 1: The sum of the priorities is", count_rucksack(lines))
print("Part 2: The sum of the priorities for the badges is", count_badges(lines))
