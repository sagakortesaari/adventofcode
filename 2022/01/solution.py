def most_calories(lines):
  most_cals = 0
  curr_cals = 0
  elf_cals = []

  for line in lines:
    if line == '\n':

      if curr_cals > most_cals:
        most_cals = curr_cals
      
      elf_cals.append(curr_cals)

      curr_cals = 0
      continue 

    curr_cals += int(line)
  
  elf_cals.sort(reverse=True)
  
  return most_cals, elf_cals

with open("input.txt", "r") as f:
  lines = f.readlines()

res = most_calories(lines)
print("The elf carrying the most calories is carrying", res[0], "calories")
print("The top three elves together carrying", sum(res[1][0:3]), "calories")