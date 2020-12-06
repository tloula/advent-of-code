# ********************************************* #
# Advent of Code Day 6                          #
# Trevor Loula                                  #
# Cedarville University Leaderboard             #
# ********************************************* #

# Customs Calculations

import string

lines = list(line.strip() for line in open('input/day-6.txt'))

sum_1 = 0
sum_2 = 0

group = ""
for line in lines:
    if line != "":
        group += line + " "
    else:
        group = group.strip()
        group_ = group.replace(' ', '')

        # Count all unique answers
        sum_1 += len(set(group_))

        # Count where all answers are the same
        num_people = len(list(group.strip().split(' ')))
        for char in string.ascii_lowercase:
            if group_.count(char) == num_people:
                sum_2 += 1

        group = ""

print("SUM 1:", sum_1)
print("SUM 2:", sum_2)
