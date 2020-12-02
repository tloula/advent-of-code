lines = list(line.strip() for line in open('day-2-input.txt'))

sum_1 = 0
sum_2 = 0

for line in lines:
    count_char, text = line.split(':')
    count, char = count_char.split(' ')
    bottom, top = list(map(int, count.split('-')))
    text = text.strip()

    num_chars = 0
    for letter in text:
        if letter == char:
            num_chars += 1
    if (num_chars >= bottom and num_chars <= top):
        sum_1 += 1

    if ((text[bottom-1] == char) ^ (text[top-1] == char)):
        sum_2 += 1

print("SUM 1", sum_1)
print("SUM 2", sum_2)