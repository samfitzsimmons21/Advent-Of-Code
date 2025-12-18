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

data = open('input.txt', 'r').read().splitlines()
operation_line = data[-1]

where_to_split = []
for i in range(1, len(operation_line)):
    if operation_line[i] == '+' or operation_line[i] == '*':
        where_to_split.append(i-1)

columns = []
start = 0
for split in where_to_split:
    columns.append([line[start:split] for line in data])
    start = split+1
columns.append([line[start:] for line in data])

operations = {
    '+': lambda a, b: a + b,
    '*': lambda a, b: a * b
}

# Part 2
p2_total = 0
for col in columns:
    operation = col[-1].strip()
    max_size = max(len(c) for c in col[:-1])

    string_dict = {i: "" for i in range(1, max_size + 1)}
    for val in col[:-1]:
        for i in range(1, len(val) + 1):
            string_dict[i] += val[i - 1]

        for i in range(len(val) + 1, max_size + 1):
            string_dict[i] += ' '

    col_val = 0
    for nums in string_dict.values():
        int_val = int(nums.replace(' ', ''))
        if col_val == 0:
            col_val = int_val
            continue
        col_val = operations[operation](col_val, int_val)
    p2_total += col_val

print("Part 2 Answer:", p2_total)