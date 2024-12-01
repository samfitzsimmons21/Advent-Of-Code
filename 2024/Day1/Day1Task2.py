with open("input.txt") as f:
    data = [tuple(map(int, line.split())) for line in f if line.strip()]

l1, l2 = [], []
for tup in data:
    l1.append(tup[0])
    l2.append(tup[1])

l2Map = {}
for val in l2:
    if val not in l2Map:
        l2Map[val] = 1
    else:
        l2Map[val] += 1


total = 0
for val1 in l1:
    if val1 in l2Map:
        total += (val1 * l2Map[val1])

print(total)