# ********************************************* #
# Advent of Code Day 2                          #
# Trevor Loula                                  #
# Cedarville University Leaderboard             #
# ********************************************* #

# Process a given list of strings

lines = list(line.strip() for line in open('input/day-2.txt'))

sum_1 = 0
sum_2 = 0

for line in lines:
    count_char, text = line.split(':')
    count, char = count_char.split(' ')
    bottom, top = list(map(int, count.split('-')))
    text = text.strip()

    num_chars = 0
    for letter in text:
        if letter == char: num_chars += 1
    if (num_chars >= bottom and num_chars <= top):
        sum_1 += 1

    if ((text[bottom-1] == char) ^ (text[top-1] == char)):
        sum_2 += 1

print("Strings with count of given char within acceptable range:", sum_1)
print("Strings with acceptable location of given char:", sum_2)