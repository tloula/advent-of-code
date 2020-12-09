# ********************************************* #
# Advent of Code Day 9                          #
# Trevor Loula                                  #
# Cedarville University Leaderboard             #
# ********************************************* #

# Sliding Window Two-Sum

import sys

class Day9:

    def __init__(self, window_size):
        self.lines = list(int(line.strip()) for line in open('input/day-9.txt'))
        self.window_size = window_size
        self.target = 0

    @staticmethod
    def two_sum(nums, target):
        for num in nums:
            complement = int(target) - int(num)
            if complement in nums: return [num, complement]
        return False

    def part_1(self):
        for i in range(self.window_size, len(self.lines)):
            if not Day9.two_sum(self.lines[i-self.window_size:i], self.lines[i]):
                self.target = self.lines[i]
                return self.target
        print("No number without property")

    def part_2(self):
        for lo in range(len(self.lines)):
            cont_sum = 0
            for hi in range(lo, len(self.lines)):
                cont_sum += self.lines[hi]
                if cont_sum == self.target:
                    return min(self.lines[lo:hi]) + max(self.lines[lo:hi])
                elif cont_sum > self.target:
                    break
        print("Contiguous sum not found")

def main(args):
    if len(args) != 2:
        print("Usage: python day-9.py window_size")

    day_9 = Day9(int(args[1]))
    num_1 = day_9.part_1()
    num_2 = day_9.part_2()

    print("First number without property:", num_1)
    print("Sum of min and max numbers in contiguous set adding to target:", num_2)

if __name__ == "__main__":
    main(sys.argv)
