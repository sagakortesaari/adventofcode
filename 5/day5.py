f = open("input.txt", "r")
lines = f.readlines()
lines = [line.strip() for line in lines]

def binary_search():
    seat_ids = []

    for line in lines:
        low_row = 0
        high_row = 127
        high_column = 7
        low_column = 0

        middle = int((low_row + high_row)/2)
        for row in range(0,7):
            if line[row] == 'F':
                high_row = middle 
            if line[row] == 'B':
                low_row = middle + 1
            middle = int((low_row + high_row)/2)
        row_value = middle 

        middle = int((low_column + high_column)/2)
        for column in range(7,10):
            middle = int((low_column + high_column)/2)
            if line[column] == 'L':
                high_column = middle 
            if line[column] == 'R':
                low_column = middle + 1
            middle = int((low_column + high_column)/2)
        column_value = middle 
        seat_id = row_value * 8 + column_value
        seat_ids.append(seat_id)

    # part 2
    return seat_ids
    # part 1
    #return max(seat_ids)

def part_2(seats):
    seats.sort()

    for seat in range(0,len(seats)):
        if abs(seats[seat] - seats[seat+1]) == 2:
            return seats[seat] + 1
                
seats = binary_search()
print(part_2(seats))