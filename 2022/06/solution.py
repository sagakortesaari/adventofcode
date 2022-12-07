def find_packet_start(line):
    characters = set()
    substring_start = 0
    for i in range(0,len(line)):
        if len(characters) == 4:
            return i

        char = line[i]

        if char in characters:
            first = line[substring_start:i].rfind(char)
            substring_start = substring_start + first + 1
            characters = set(line[substring_start:i+1])
        else:
            characters.add(char)

def find_message_start(line):
    characters = set()
    substring_start = 0
    for i in range(0,len(line)):
        if len(characters) == 14:
            return i

        char = line[i]

        if char in characters:
            first = line[substring_start:i].rfind(char)
            substring_start = substring_start + first + 1
            characters = set(line[substring_start:i+1])
        else:
            characters.add(char)

with open("input.txt", "r") as f:
  lines = [l.strip() for l in f.readlines()]

print("Part 1: The first start-of-packet marker is detected at character", find_packet_start(lines[0]))
print("Part 1: The first start-of-message marker is detected at character", find_message_start(lines[0]))
