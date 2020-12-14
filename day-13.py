# ********************************************* #
# Advent of Code Day 13                         #
# Shuttle Search                                #
# Trevor Loula                                  #
# Cedarville University Leaderboard             #
# ********************************************* #

import sys

class ShuttleSearch:

    def __init__(self):
        self.input = list(line.strip() for line in open('input/day-13.txt'))
        self.target = int(self.input[0])
        self.buses = self.input[1].split(',')

    def part_1(self):
        return min((int(bus) - self.target % int(bus), int(bus)) for bus in self.buses if bus != 'x')

    def part_2(self):
        ids = [(start, int(id)) for start, id in enumerate(self.buses) if id != 'x']
        ts = 0
        lcm = 1
        for start, step in ids:
            while (ts + start) % step != 0:
                ts += lcm
            lcm *= step
        return ts


def main(args):

    ss = ShuttleSearch()
    num_1 = ss.part_1()
    num_2 = ss.part_2()

    print("Earliest Bus ID:", num_1[0] * num_1[1])
    print("Earliest Timestamp w/ Departure Offset:", num_2)

if __name__ == "__main__":
    main(sys.argv)
