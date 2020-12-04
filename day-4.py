# ********************************************* #
# Advent of Code Day 4                          #
# Trevor Loula                                  #
# Cedarville University Leaderboard             #
# ********************************************* #

import re

def valid(passport):
    # Birth Year
    byr_index = passport.find('byr:') + 4
    byr = passport[byr_index:byr_index+4]
    if not byr.isnumeric(): return False
    if int(byr) < 1920 or int(byr) > 2002:
        return False

    # Issue Year
    iyr_index = passport.find('iyr:') + 4
    iyr = passport[iyr_index:iyr_index+4]
    if not iyr.isnumeric(): return False
    if int(iyr) < 2010 or int(iyr) > 2020:
        return False

    # Expiration Year
    eyr_index = passport.find('eyr:') + 4
    eyr = passport[eyr_index:eyr_index+4]
    if not eyr.isnumeric(): return False
    if int(eyr) < 2020 or int(eyr) > 2030:
        return False

    # Height
    hgt_index = passport.find('hgt:') + 4
    hgt = passport[hgt_index:hgt_index+5]
    if hgt.find('cm') != -1:
        num = re.findall('[0-9]+', hgt)[0]
        if not num.isnumeric(): return False
        if int(num) < 150 or int(num) > 193:
            return False
    else:
        num = re.findall('[0-9]+', hgt)[0]
        if not num.isnumeric(): return False
        if int(num) < 59 or int(num) > 76:
            return False

    # Hair Color
    hcl_index = passport.find('hcl:#') + 5
    hcl = passport[hcl_index:hcl_index+6]
    if not all([char in "0123456789abcdef" for char in hcl]):
        return False

    # Eye Color
    ecl_index = passport.find('ecl:') + 4
    ecl = passport[ecl_index:ecl_index+3]
    colors = ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')
    if ecl not in colors:
        return False

    # Passport ID
    pid_index = passport.find('pid:') + 4
    pid = passport[pid_index:pid_index+9]
    if not pid.isnumeric(): return False

    return True

lines = list(line.strip() for line in open('input/day-4.txt'))
fields = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:#', 'ecl:', 'pid:']

sum_1 = 0
sum_2 = 0

passport = ""
for line in lines:
    if line != "":
        passport += line
    else:
        if all([passport.find(field) != -1 for field in fields]):
            sum_1 += 1
        passport = ""

passport = ""
for line in lines:
    if line != "":
        passport += line
    else:
        if all([passport.find(field) != -1 for field in fields]) and valid(passport):
            sum_2 += 1
        passport = ""

print("Sum 1:", sum_1)
print("Sum 2:", sum_2)