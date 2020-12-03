# ********************************************* #
# Advent of Code Day 3                          #
# Trevor Loula                                  #
# Cedarville University Leaderboard             #
# ********************************************* #

def hits(grid, x_offset, y_offset):
    x, y, sum = 0, 0, 0
    while (x < len(grid)):
        if grid[x][y] == '#': sum += 1
        x += x_offset
        y += y_offset
        y %= len(grid[0])
    return sum

grid = list(line.strip() for line in open('input/day-3.txt'))

sum_1 = hits(grid, 1, 1)
sum_2 = hits(grid, 1, 3)
sum_3 = hits(grid, 1, 5)
sum_4 = hits(grid, 1, 7)
sum_5 = hits(grid, 2, 1)

print("Sum 1:", sum_1)
print("Sum 2:", sum_2)
print("Sum 3:", sum_3)
print("Sum 4:", sum_4)
print("Sum 5:", sum_5)
print("Product:", sum_1*sum_2*sum_3*sum_4*sum_5)