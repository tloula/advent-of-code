# ********************************************* #
# Advent of Code Day 10                         #
# Trevor Loula                                  #
# Cedarville University Leaderboard             #
# ********************************************* #

# Adapter Array

import sys

class AdapterArray:

    def __init__(self):
        self.array = [0] + sorted(list(int(line.strip()) for line in open('input/day-10.txt')))

    def part_1(self):
        curr_n = diff_1 = diff_2 = diff_3 = 0
        for n in self.array:
            if n <= curr_n + 3:
                if n == curr_n + 1: diff_1 += 1
                elif n == curr_n + 2: diff_2 += 1
                elif n == curr_n + 3: diff_3 += 1
                curr_n = n
            else: print("No compatabile adapter: {} -> {}".format(curr_n, n))
        # Add built in adapter
        curr_n += 3
        diff_3 += 1

        return diff_1 * diff_3

    def part_2(self):
        placeholders = [1] + [0 for x in range(len(self.array)-1)]
        for x in range(len(self.array)):
            for offset in range(1, 4):
                if self.array[x] + offset in self.array:
                    placeholders[self.array.index(self.array[x] + offset)] += placeholders[x]

        return placeholders[-1]


def main(args):

    aa = AdapterArray()
    num_1 = aa.part_1()
    num_2 = aa.part_2()

    print("Number 1:", num_1)
    print("Number 2:", num_2)

if __name__ == "__main__":
    main(sys.argv)
