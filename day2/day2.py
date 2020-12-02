f = open("input.txt", "r")
lines = f.read()
arr = lines.split()

def part_1():
    valid = 0
    count = 0
    while count < len(arr):
        interval = arr[count].split("-")
        times_min = int(interval[0])
        times_max = int(interval[1])
        char = arr[count+1][0]
        stringen = arr[count+2]

        counter = stringen.count(char)

        if counter >= int(times_min) and counter <= int(times_max):
            valid += 1

        count += 3

    return valid

def part_2():
    valid = 0
    count = 0

    while count < len(arr):
        nums = arr[count].split("-")
        position1 = int(nums[0])
        position2 = int(nums[1])
        char = arr[count+1][0]
        text = arr[count+2]

        if (text[position1 - 1] == char and not text[position2 - 1] == char) or (not (text[position1 - 1] == char) and text[position2 - 1] == char):
            valid += 1

        count += 3

    return valid

print(part_1())
print(part_2())


