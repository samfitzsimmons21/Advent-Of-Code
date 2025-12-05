
with open('input.txt', 'r') as file:
    text = file.read()

first, second = text.strip().split("\n\n", 1)

p1_ans = 0
range_vals = []
for line in first.splitlines():
    a, b = line.split("-")
    range_vals.append((int(a), int(b)))
range_vals.sort()

for line in second.splitlines():
    id = line
    id_num = int(id)

    for val in range_vals:
        lower_range, upper_range = val
        if lower_range <= id_num <= upper_range:
            p1_ans += 1
            break

print("Part 1 Answer: ", p1_ans)

