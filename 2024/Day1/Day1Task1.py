with open("input.txt") as f:
    data = [tuple(map(int, line.split())) for line in f if line.strip()]

l1, l2 = [], []
for tup in data:
    l1.append(tup[0])
    l2.append(tup[1])

l1Map = {val : i for i, val in enumerate(l1)}
l2Map = {val : i for i, val in enumerate(l2)}

l1.sort()
l2.sort()

dist = 0
for val1, val2 in zip(l1, l2):
    dist += abs(val1 - val2)


print(dist)