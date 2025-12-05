
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

# Part 2
n = len(range_vals)

changes = 1
while changes > 0:
    changes = 0

    n = len(range_vals)
    new_ranges = []

    for start, end in range_vals:
        if not new_ranges:
            new_ranges.append([start, end])
        else:
            last_start, last_end = new_ranges[-1]

            if start <= last_end:
                new_ranges[-1][-1] = max(last_end, end)
            else:
                new_ranges.append([start, end])

    range_vals = new_ranges
    changes = len(new_ranges) - n

p2_ans = 0
for val in range_vals:
    lower_range, upper_range = val
    p2_ans += upper_range - lower_range + 1


print("Part 2 Answer: ", p2_ans)

