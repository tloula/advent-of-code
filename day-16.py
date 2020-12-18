# ********************************************* #
# Advent of Code Day 16                         #
# Ticket Translation                            #
# Trevor Loula                                  #
# Cedarville University Leaderboard             #
# ********************************************* #

import copy
import sys

class TicketTranslation:

    def __init__(self):
        self.input = "".join([line for line in open('input/day-16.txt')]).split('\n\n')
        self.ranges = [[int(ran.split('-')[0]), int(ran.split('-')[1])] for line in self.input[0].split('\n') for ran in line.split(': ')[1].split(' or ')]
        self.ticket = [int(x) for x in self.input[1].split('\n')[1].split(',')]
        self.tickets = [list(map(int, x)) for x in [line.split(',') for line in self.input[2].split('\n')[1:]]]

        self.fields = dict()
        self.field_list = list()
        for line in self.input[0].split('\n'):
            line = line.split(': ')
            self.fields[line[1].split(' or ')[0]] = line[0]
            self.fields[line[1].split(' or ')[1]] = line[0]
            self.field_list.append(line[0])

    def _in_range(self, seat):
        out = list()
        for ran in self.ranges:
            if ran[0] <= seat and seat <= ran[1]: out.append(ran)
        if len(out) == 0: return False
        else: return out

    def _determine_field(self, seats):
        if type(seats) == bool: return []
        return [self.fields[x] for x in [str(str(seat[0]) + '-' + str(seat[1])) for seat in seats]]

    def part_1(self):
        error_rate = 0
        for ticket in self.tickets:
            for seat in ticket:
                if self._in_range(seat) == False: error_rate += seat
        return error_rate

    # Well this is gross...
    def part_2(self):
        for ticket in self.tickets:
            for seat in ticket:
                if self._in_range(seat) == False:
                    self.tickets.remove(ticket)
                    break

        mapping = [copy.copy(self.field_list) for i in range(len(self.ticket))]
        for ticket in self.tickets:
            for i, seat in enumerate(ticket):
                lst = self._determine_field(self._in_range(seat))
                for field in self.field_list:
                    if field not in lst and len(lst) > 0 and field in mapping[i]:
                        mapping[i].remove(field)

        changed = True
        kill = list()
        while changed:
            changed = False
            for row in mapping:
                if len(row) == 1: kill.append(row[0])
                else:
                    for item in row:
                        if item in kill:
                            row.remove(item)
                            changed = True

        prod = 1
        for i, field in enumerate(mapping):
            if field[0].find('departure') != -1: prod *= self.ticket[i]
            print ("{}: {}".format(self.ticket[i], field))
        
        return prod

def main(args):

    tt = TicketTranslation()
    num_1 = tt.part_1()
    num_2 = tt.part_2()

    print("Number 1:", num_1)
    print("Number 2:", num_2)

if __name__ == "__main__":
    main(sys.argv)
