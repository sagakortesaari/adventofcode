def check_full_overlap(e1, e2):
  l1 = e1.split("-")
  l2 = e2.split("-")
  r1 = range(int(l1[0]), int(l1[1])+1)
  r2 = range(int(l2[0]), int(l2[1])+1)

  return set(r1).issubset(r2) or set(r2).issubset(r1)

def check_overlap(e1, e2):
  l1 = e1.split("-")
  l2 = e2.split("-")
  r1 = range(int(l1[0]), int(l1[1])+1)
  r2 = range(int(l2[0]), int(l2[1])+1)

  if (len(range(max(r1[0], r2[0]), min(r1[-1], r2[-1]) + 1)) > 0):
    return True 
  
  return False

def count_contained_pairs(lines):
  full_overlap_count = 0
  overlap_count = 0
  for line in lines:
    pairs = line.split(",")
    if check_full_overlap(pairs[0], pairs[1]):
      full_overlap_count += 1
    if check_overlap(pairs[0], pairs[1]):
      overlap_count += 1
  
  return full_overlap_count, overlap_count

with open("input.txt", "r") as f:
  lines = [l.strip() for l in f.readlines()]

res = count_contained_pairs(lines)
print("Part 1: The amount of pairs that fully overlaps is:", res[0])
print("Part 2: The amount of pairs that overlap is:", res[1])


