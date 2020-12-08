# ********************************************* #
# Advent of Code Day 7                          #
# Trevor Loula                                  #
# Cedarville University Leaderboard             #
# ********************************************* #

# Bag Contents

lines = list(line.strip() for line in open('input/day-7.txt'))

sum_1 = 0
sum_2 = 0

# light red bags contain 1 bright white bag, 2 muted yellow bags
# adjective 1 | adjective 2 | "bags" | "contain" | [num bags, adjective 1, adjective 2, "bags"]

# bags = {"Bag Type": {Bags Contained: Quantity}}
bags = dict()

# Compile dictionary of all bags
for line in lines:
    bag, contains = line.split(' bags contain ')
    contents = dict()
    if contains != "no other bags.":
        for contain in contains.split(', '):
            contain = contain.split(' ')
            contents[contain[1] + " " + contain[2]] = int(contain[0])
    bags[bag] = contents

# Determine how many outer bags can contain a shiny gold bag
processed_layers = {"shiny gold": 1}
layer = {"shiny gold": 1}
while len(layer):
    new_layer = dict()
    for item in layer:
        for bag, contents in bags.items():
            if item in contents and bag not in processed_layers:
                new_layer[bag] = contents[item]
    layer = new_layer
    processed_layers.update(layer)
    sum_1 += len(layer)

# Determine how many bags can fit inside a shiny gold bag
layer = {"shiny gold": 1}
while len(layer):
    new_layer = dict()
    for bag in layer:
        for new_bag, count in bags[bag].items():
            if new_bag in new_layer: new_layer[new_bag] += layer[bag] * count
            else: new_layer[new_bag] = layer[bag] * count
    sum_2 += sum(list(new_layer.values())) 
    layer = new_layer

print("SUM 1:", sum_1) # 378
print("SUM 2:", sum_2) # 27526
