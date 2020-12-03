# ********************************************* #
# Advent of Code Day 3                          #
# Trevor Loula                                  #
# Cedarville University Leaderboard             #
# ********************************************* #

# Process a grid

grid = list(line.strip() for line in open('input/day-3.txt'))

sum_1 = 0
sum_2 = 0
sum_3 = 0
sum_4 = 0
sum_5 = 0

x, y = 0, 0
while (x < len(grid)):
    if grid[x][y] == '#':
        sum_1 += 1
    x += 1
    y += 1
    y %= len(grid[0])

x, y = 0, 0
while (x < len(grid)):
    if grid[x][y] == '#':
        sum_2 += 1
    x += 1
    y += 3
    y %= len(grid[0])

x, y = 0, 0
while (x < len(grid)):
    if grid[x][y] == '#':
        sum_3 += 1
    x += 1
    y += 5
    y %= len(grid[0])

x, y = 0, 0
while (x < len(grid)):
    if grid[x][y] == '#':
        sum_4 += 1
    x += 1
    y += 7
    y %= len(grid[0])

x, y = 0, 0
while (x < len(grid)):
    if grid[x][y] == '#':
        sum_5 += 1
    x += 2
    y += 1
    y %= len(grid[0])

print("Sum 1:", sum_1)
print("Sum 2:", sum_2)
print("Sum 3:", sum_3)
print("Sum 4:", sum_4)
print("Sum 5:", sum_5)
print("Product:", sum_1*sum_2*sum_3*sum_4*sum_5)