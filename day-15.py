# ********************************************* #
# Advent of Code Day 15                         #
# Rambunctious Recitation                       #
# Trevor Loula                                  #
# Cedarville University Leaderboard             #
# ********************************************* #

import sys

class RambunctiousRecitation:

    def __init__(self):
        self.nums = list(int(x) for line in open('input/day-15.txt') for x in line.strip().split(','))

    def part_1(self, target):
        while len(self.nums) - 1 < target:
            last_spoken = self.nums[-1]
            if last_spoken not in self.nums[:-1]:
                self.nums.append(0)
            else:
                indices = [i for i, x in enumerate(self.nums) if x == last_spoken]
                self.nums.append(indices[-1] - indices[-2])
        return last_spoken

    def part_2(self, target):
        d = { num:index for index, num in enumerate(self.nums, 1) } 
        current = self.nums[-1]
        index   = len(self.nums)

        while index <= target:
            previous = d.get(current)
            d[current] = index
            current = index - previous if previous else 0
            index += 1

        return list(d.keys())[list(d.values()).index(target)]


def main(args):

    rr = RambunctiousRecitation()
    num_1 = rr.part_1(2020)
    num_2 = rr.part_2(30000000)

    print("Number 1:", num_1)
    print("Number 2:", num_2)

if __name__ == "__main__":
    main(sys.argv)
