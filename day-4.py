# ********************************************* #
# Advent of Code Day 4                          #
# Trevor Loula                                  #
# Cedarville University Leaderboard             #
# ********************************************* #

# Passport field validation

import re

# Birth Year
def validate_byr(byr):
    if not byr.isnumeric(): return False
    if int(byr) < 1920 or int(byr) > 2002:
        return False
    return True

# Issue Year
def validate_iyr(iyr):
    if not iyr.isnumeric(): return False
    if int(iyr) < 2010 or int(iyr) > 2020:
        return False
    return True

# Expiration Year
def validate_eyr(eyr):
    if not eyr.isnumeric(): return False
    if int(eyr) < 2020 or int(eyr) > 2030:
        return False
    return True

# Height
def validate_hgt(hgt):
    if hgt[-2:] == 'cm':
        num = hgt[:-2]
        if not num.isnumeric(): return False
        if int(num) < 150 or int(num) > 193:
            return False
    elif hgt[-2:] == 'in':
        num = hgt[:-2]
        if not num.isnumeric(): return False
        if int(num) < 59 or int(num) > 76:
            return False
    else: return False
    return True

# Hair Color
def validate_hcl(hcl):
    if hcl[0] != '#': return False
    if not all([char in "0123456789abcdef" for char in hcl[1:]]):
        return False
    return True

# Eye Color
def validate_ecl(ecl):
    colors = ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')
    if ecl not in colors: return False
    return True

# Passport ID
def validate_pid(pid):
    if len(pid) != 9: return False
    if not pid.isnumeric(): return False
    return True

def validate_passport(passport):
    for field in passport.split(' '):
        key, value = field[0:3], field[4:]
        if key == 'byr': valid = validate_byr(value)
        elif key == 'iyr': valid = validate_iyr(value)
        elif key == 'eyr': valid = validate_eyr(value)
        elif key == 'hgt': valid = validate_hgt(value)
        elif key == 'hcl': valid = validate_hcl(value)
        elif key == 'ecl': valid = validate_ecl(value)
        elif key == 'pid': valid = validate_pid(value)
        elif key == 'cid': valid = True
        else: valid = False
        if not valid: return False
    return True

lines = list(line.strip() for line in open('input/day-4.txt'))
fields = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']

sum_1 = 0
sum_2 = 0

passport = ""
for line in lines:
    if line != "":
        passport += line + " "
    else:
        passport = passport.strip()
        if all([passport.find(field) != -1 for field in fields]):
            sum_1 += 1
            if validate_passport(passport):
                sum_2 += 1
        passport = ""

print("Sum 1:", sum_1)
print("Sum 2:", sum_2)

# 105 is too high