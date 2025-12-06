from itertools import zip_longest

with open('input.txt', 'r') as file:
    lines = [ln.rstrip('\n') for ln in file if ln.strip()]

rows = [ln.split() for ln in lines]
columns = [list(col) for col in zip_longest(*rows, fillvalue=None)]

p1_total = 0
operations = {'+' : lambda x, y: x + y, '*' : lambda x, y: x * y}
for col in columns:
    operation = col[-1]

    col_val = 0
    for val in col[:-1]:

        int_val = int(val)
        if col_val == 0:
            col_val = int_val
            continue
        col_val = operations[operation](col_val, int_val)
    p1_total += col_val

print("Part 1 Answer: ", p1_total)