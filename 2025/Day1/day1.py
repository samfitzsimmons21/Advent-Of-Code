
with open("input.txt") as f:
    lines = f.readlines()

dial = 50
lower_limit = 0
upper_limit = 99

zero_count_p1 = 0 # The actual password is the number of times the dial is left pointing at 0 after any rotation in the sequence.
zero_count_p2 = 0

for line in lines:
    vals = line.split()[0]
    inside = [vals][0]
    direction, steps = inside[0], int(inside[1:])

    while steps > 99:
        steps -= 100
        if steps != 0:
            zero_count_p2 += 1

    if direction == 'L':
        pre_dial = dial
        dial -= steps
        if dial < lower_limit:
            dial += (upper_limit + 1)

            if pre_dial != 0:
                zero_count_p2 += 1

    if direction == 'R':
        dial += steps
        if dial > upper_limit:
            dial -= (upper_limit + 1)
            if dial > lower_limit:
                zero_count_p2 += 1

    if dial == 0:
        zero_count_p1 += 1

print(f"Answer is: {zero_count_p1}") # Part 1 answer: 1023
print(f"Answer 2 is: {zero_count_p2 + zero_count_p1}") # Part 2 answer: 5899
