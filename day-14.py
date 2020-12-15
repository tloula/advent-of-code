# ********************************************* #
# Advent of Code Day 13                         #
# Docking Data                                  #
# Trevor Loula                                  #
# Cedarville University Leaderboard             #
# ********************************************* #

from itertools import permutations
import sys

class DockingData:

    def __init__(self):
        self.input = list(tuple(line.strip().split(" = ")) for line in open('input/day-14.txt'))

    @staticmethod
    def apply_mask(mask, num, zero=True):
        out = list('{:036b}'.format(num))
        for key, val in enumerate(mask):
            if val == '1': out[key] = '1'
            elif zero and val == '0': out[key] = '0'
            elif not zero and val == 'X': out[key] = 'X'
        return "".join(out)

    @staticmethod
    def gen_mask_perms(mask):
        perms = list(list(bin(x)[2:]) for x in range(2**mask.count('X')))       # Generate list of permutations
        perms = [[int(x) for x in perm] for perm in perms]                      # Convert chars to ints
        perms = [[0] * (len(max(perms)) - len(perm)) + perm for perm in perms]  # Prepend 0's
        masks = list()
        for perm in perms:
            mask_list = list(mask)
            for i, bit in enumerate(mask_list):
                if bit == 'X': mask_list[i] = perm.pop(0)
            masks.append("".join([str(x) for x in mask_list]))
        return masks

    def part_1(self):
        mem = dict()
        mask = ""
        for line in self.input:
            if line[0] == "mask": mask = line[1]
            else: mem[int(line[0][4:-1])] = int(self.apply_mask(mask, int(line[1])), 2)
        return sum(mem.values())

    def part_2(self):
        mem = dict()
        mask = ""
        for line in self.input:
            if line[0] == "mask": mask = line[1]
            else:
                init_mask = self.apply_mask(mask, int(line[0][4:-1]), False)
                for perm in self.gen_mask_perms(init_mask):
                    mem[int(self.apply_mask(perm, int(line[0][4:-1]), True), 2)] = int(line[1])
        return sum(mem.values())


def main(args):

    dd = DockingData()
    num_1 = dd.part_1()
    num_2 = dd.part_2()

    print("Number 1:", num_1)
    print("Number 2:", num_2)

if __name__ == "__main__":
    main(sys.argv)
