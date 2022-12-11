def assemble_path(path):
  if len(path) == 1:
      return "/"

  dir_path = ""
  for dir in path[1:]:
      dir_path += "/" + dir 
  return dir_path

def exec_commands(lines):
  dirs = {"/": []}
  path = ["/"]

  i = 0
  while i < len(lines):
      current_line = lines[i]
      if current_line[0] == "$": # command
          command = current_line[2:4]
          if command == "cd": # command cd
              arg = current_line[5:]
              if arg == "..":
                  path.pop()
              elif arg == "/":
                  path = ["/"]
              else:
                  path.append(arg)
                  dirs[assemble_path(path)] = []
          else: # command ls
              pass
      else: # files/dirs printed after ls   
          cur_path = assemble_path(path)      
          if current_line[0].isnumeric():
              file = current_line.split(" ")
              dirs[cur_path].append(("f", file[0]))
          else:
              dir = current_line.split(" ")
              dirs[cur_path].append(("dir", "/" + dir[1]))
      i += 1
  return dirs

def count_size_p1(dir_name, dir_contents, file_system, dir_map):
  size = 0

  for item in dir_contents:
      if item[0] == "f":
          size += int(item[1])
      else:
          if dir_name == "/":
              next_dir = item[1]
          else:
              next_dir = dir_name + item[1]
          size += count_size_p1(next_dir, file_system[next_dir], file_system, dir_map)[0]

  if size <= 100000:
      dir_map[dir_name] = size
  return size, dir_map

def count_size_p2(dir_name, dir_contents, file_system, dir_map):
  size = 0

  for item in dir_contents:
      if item[0] == "f":
          size += int(item[1])
      else:
          if dir_name == "/":
              next_dir = item[1]
          else:
              next_dir = dir_name + item[1]
          size += count_size_p2(next_dir, file_system[next_dir], file_system, dir_map)[0]

  dir_map[dir_name] = size
  return size, dir_map

with open("input.txt", "r") as f:
  lines = [l.strip() for l in f.readlines()]

file_system = exec_commands(lines)
part1 = count_size_p1("/", file_system["/"], file_system, {})
print("Part 1: The sum of the directories with size <= 100 000 is", sum(part1[1].values()))

part2 = count_size_p2("/", file_system["/"], file_system, {})
unused = 70000000 - part2[0]
remainder = 30000000 - unused
print("Part 2: The smallest directory to be deleted in order to free up space has the size", min([size for size in part2[1].values() if size >= remainder]))


