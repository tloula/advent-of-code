# ********************************************* #
# Advent of Code Day 5                          #
# Trevor Loula                                  #
# Cedarville University Leaderboard             #
# ********************************************* #

# Seat ID Calculation

lines = list(line.strip() for line in open('input/day-5.txt'))
seat_ids = []

for line in lines:
    row, col = [0, 127], [0, 7]
    for char in line[:7]:
        if char == 'B': row[0] = int(row[0] + (row[1] - row[0]) / 2)
        elif char == 'F': row[1] = int(row[0] + (row[1] - row[0]) / 2)
        else: print("Invalid Row Reference")
    for char in line[7:]:
        if char == 'R': col[0] = int(col[0] + (col[1] - col[0]) / 2)
        elif char == 'L': col[1] = int(col[0] + (col[1] - col[0]) / 2)
        else: print("Invalid Column Reference")
    seat_ids.append(row[1] * 8 + col[1])
    #print("Row:", row[1], "Column:", col[1], "Seat ID:", seat_ids[-1:])

print("Highest Seat ID:", max(seat_ids))

for n in range(min(seat_ids), max(seat_ids)):
    if n not in seat_ids: print("Missing Seat", n)
