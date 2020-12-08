# ********************************************* #
# Advent of Code Day 8                          #
# Trevor Loula                                  #
# Cedarville University Leaderboard             #
# ********************************************* #

# Assembly Run and Fixup

import copy
import sys

class Assembler:
    def __init__(self):
        self.prgm = list([line.strip()[:3], int(line.strip()[4:])] for line in open('input/day-8.txt'))
        self.modified_prgm = list()
        self.accu = 0
        self.pc = 0
        self.pc_complete = set()
        self.pc_changed = -1

    def reset(self):
        self.modified_prgm = copy.deepcopy(self.prgm)
        self.accu = 0
        self.pc = 0
        self.pc_complete = set()

    def nop(self, n):
        self.pc += 1

    def acc(self, n):
        self.accu += n
        self.pc += 1

    def jmp(self, n):
        self.pc += n

    def step(self, prgm):
        inst, n = prgm[self.pc]
        if inst == "nop": self.nop(n)
        elif inst == "acc": self.acc(n)
        elif inst == "jmp": self.jmp(n)
        else: print("Unknown Inst")

    def modify_prgm(self):
        self.reset()
        for i in range(self.pc_changed+1, len(self.prgm)):
            inst, _ = self.prgm[i]
            if inst == "nop":
                self.modified_prgm[i][0] = "jmp"
                self.pc_changed = i
                return True
            elif inst == "jmp":
                self.modified_prgm[i][0] = "nop"
                self.pc_changed = i
                return True
        return False # Error

    def run(self, prgm=None):
        if prgm is None: prgm = self.prgm
        while self.pc not in self.pc_complete:
            if self.pc == len(prgm):
                return True, self.accu
            self.pc_complete.add(self.pc)
            self.step(prgm)
        return False, self.accu

    def fixup(self):
        complete = False
        while not complete:
            if not self.modify_prgm():
                print("Unable to Fix Program")
                return 0
            complete, acc = self.run(self.modified_prgm)
        return acc

def main(args):
    asm = Assembler()
    complete, acc_value = asm.run()
    fixed_acc_value = asm.fixup()

    if complete: print("Program Complete")
    print("Accumulator Value:", acc_value) # 1594
    print("Accumulator Value of Fixed Program:", fixed_acc_value) # 758

if __name__ == "__main__":
    main(sys.argv)
