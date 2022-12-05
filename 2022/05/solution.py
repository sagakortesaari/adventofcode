def move_boxes_p1(lines, stacks):
  for line in lines:
      moving_boxes = []
      for i in range(0,int(line[0])):
          index = stacks[int(line[1])-1]
          if (len(index) > 0):
              moving_boxes.append(stacks[int(line[1])-1].pop())
              
      stacks[int(line[2])-1] = stacks[int(line[2])-1] + moving_boxes

def move_boxes_p2(lines, stacks):
  for line in lines:
      moving_boxes = []
      for i in range(0,int(line[0])):
          index = stacks[int(line[1])-1]
          if (len(index) > 0):
              moving_boxes.append(stacks[int(line[1])-1].pop())

      if len(moving_boxes) > 0:
          moving_boxes.reverse()

      stacks[int(line[2])-1] = stacks[int(line[2])-1] + moving_boxes

stacks_p1 = [['Z','P','M','H','R'], ['P','C','J','B'], ['S','N','H','G','L','C','D'], ['F','T','M','D','Q','S','R','L'], ['F','S','P','Q','B','T','Z','M'], ['T','F','S','Z','B','G'], ['N','R','V'], ['P','G','L','T','D','V','C','M'], ['W','Q','N','J','F','M','L']]
stacks_p2 = [['Z','P','M','H','R'], ['P','C','J','B'], ['S','N','H','G','L','C','D'], ['F','T','M','D','Q','S','R','L'], ['F','S','P','Q','B','T','Z','M'], ['T','F','S','Z','B','G'], ['N','R','V'], ['P','G','L','T','D','V','C','M'], ['W','Q','N','J','F','M','L']]

with open("input.txt", "r") as f:
  lines = [l.strip() for l in f.readlines()]
  lines = [l.split(" ") for l in lines]
  lines = [(l[1], l[3], l[5]) for l in lines[10:]]

move_boxes_p1(lines, stacks_p1)
move_boxes_p2(lines, stacks_p2)

crates_p1 = ''
for stack in stacks_p1:
  crates_p1 += stack[-1]

crates_p2 = ''
for stack in stacks_p2:
  crates_p2 += stack[-1]


print("Part 1: The crates on top of each stack are", crates_p1)
print("Part 2: The crates on top of each stack are", crates_p2)