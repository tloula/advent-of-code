# ********************************************* #
# Advent of Code Day 11                         #
# Seating System                                #
# Trevor Loula                                  #
# Cedarville University Leaderboard             #
# ********************************************* #

# Rules
# If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
# If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
# Otherwise, the seat's state does not change.

import copy
import sys

class SeatingSystem:

    FLOOR = "."
    EMPTY = "L"
    OCCUPIED = "#"

    def __init__(self):
        self.grid = list(list(x for x in line.strip()) for line in open('input/day-11.txt'))

    def _get_adjacent(self, j, i):
        left = top_left = top = top_right = right = bottom_right = bottom = bottom_left = None
        if i-1 >= 0:                                            left = self.grid[j][i-1]            # LEFT
        if j-1 >= 0 and i-1 >= 0:                               top_left = self.grid[j-1][i-1]      # TOP LEFT
        if j-1 >= 0:                                            top = self.grid[j-1][i]             # TOP
        if j-1 >= 0 and i+1 < len(self.grid[j]):                top_right = self.grid[j-1][i+1]     # TOP RIGHT
        if i+1 < len(self.grid[j]):                             right = self.grid[j][i+1]           # RIGHT
        if j+1 < len(self.grid) and i+1 < len(self.grid[j]):    bottom_right = self.grid[j+1][i+1]  # BOTTOM RIGHT
        if j+1 < len(self.grid):                                bottom = self.grid[j+1][i]          # BOTTOM
        if j+1 < len(self.grid) and i-1 >= 0:                   bottom_left = self.grid[j+1][i-1]   # BOTTOM LEFT
        return left, top_left, top, top_right, right, bottom_right, bottom, bottom_left

    def _get_visible(self, j, i):
        left = top_left = top = top_right = right = bottom_right = bottom = bottom_left = None

        # LEFT
        for x in range(1, i+1):
            if self.grid[j][i-x] is not self.FLOOR:
                if self.grid[j][i-x] is self.OCCUPIED: left = self.OCCUPIED
                else: left = self.EMPTY
                break

        # TOP LEFT
        x, y = i-1, j-1
        while x >= 0 and y >= 0:
            if self.grid[y][x] is not self.FLOOR:
                if self.grid[y][x] is self.OCCUPIED: top_left = self.OCCUPIED
                else: top_left = self.EMPTY
                break
            x, y = x-1, y-1

        # TOP
        for y in range(1, j+1):
            if self.grid[j-y][i] is not self.FLOOR:
                if self.grid[j-y][i] is self.OCCUPIED: top = self.OCCUPIED
                else: top = self.EMPTY
                break

        # TOP RIGHT
        x, y = i+1, j-1
        while x <= len(self.grid[j]) - 1 and y >= 0:
            if self.grid[y][x] is not self.FLOOR:
                if self.grid[y][x] is self.OCCUPIED: top_right = self.OCCUPIED
                else: top_right = self.EMPTY
                break
            x, y = x+1, y-1

        # RIGHT
        for x in range(i+1, len(self.grid[j])):
            if self.grid[j][x] is not self.FLOOR:
                if self.grid[j][x] is self.OCCUPIED: right = self.OCCUPIED
                else: right = self.EMPTY
                break

        # BOTTOM RIGHT
        x, y = i+1, j+1
        while x <= len(self.grid[j]) - 1 and y <= len(self.grid) - 1:
            if self.grid[y][x] is not self.FLOOR:
                if self.grid[y][x] is self.OCCUPIED: bottom_right = self.OCCUPIED
                else: bottom_right = self.EMPTY
                break
            x, y = x+1, y+1

        # BOTTOM
        for y in range(j+1, len(self.grid)):
            if self.grid[y][i] is not self.FLOOR:
                if self.grid[y][i] is self.OCCUPIED: bottom = self.OCCUPIED
                else: bottom = self.EMPTY
                break

        # BOTTOM LEFT
        x, y = i-1, j+1
        while x >= 0 and y <= len(self.grid) - 1:
            if self.grid[y][x] is not self.FLOOR:
                if self.grid[y][x] is self.OCCUPIED: bottom_left = self.OCCUPIED
                else: bottom_left = self.EMPTY
                break
            x, y = x-1, y+1

        return left, top_left, top, top_right, right, bottom_right, bottom, bottom_left

    def _update_grid(self, func, tolerance):
        grid = copy.deepcopy(self.grid)
        for j in range(len(self.grid)):
            for i in range(len(self.grid[j])):
                if self.grid[j][i] is self.EMPTY:
                    if all(x is not self.OCCUPIED for x in func(j, i)):
                        grid[j][i] = self.OCCUPIED
                elif self.grid[j][i] is self.OCCUPIED:
                    if sum([x is self.OCCUPIED for x in func(j, i)]) >= tolerance:
                        grid[j][i] = self.EMPTY
        return grid

    @staticmethod
    def print_grid(grid):
        for row in grid:
            line = ""
            for x in row:
                line += x
            print(line)
        print()

    def _count_occupied(self):
        return sum([x is self.OCCUPIED for row in self.grid for x in row])

    def part_1(self):
        #SeatingSystem.print_grid(self.grid)
        while True:
            old_grid = self.grid
            self.grid = self._update_grid(self._get_adjacent, 4)
            #SeatingSystem.print_grid(self.grid)
            if self.grid == old_grid: break
        return self._count_occupied()

    def part_2(self):
        #SeatingSystem.print_grid(self.grid)
        while True:
            old_grid = self.grid
            self.grid = self._update_grid(self._get_visible, 5)
            #SeatingSystem.print_grid(self.grid)
            if self.grid == old_grid: break
        return self._count_occupied()


def main(args):

    ss = SeatingSystem()
    num_1 = ss.part_1()
    num_2 = ss.part_2()

    print("Number 1:", num_1)
    print("Number 2:", num_2)

if __name__ == "__main__":
    main(sys.argv)
