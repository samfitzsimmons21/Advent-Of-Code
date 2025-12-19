with open("input.txt", "r") as file:
    lines = file.read().splitlines()

S_line, diagram_lines = lines[0], lines[1:]

# Initial S
size = len(S_line)
S_location = S_line.index("S")

prev_indexes = {S_location}

p1_ans = 0
for line in diagram_lines:
    indexes_up = set()
    for pos in prev_indexes:
        if line[pos] == "^":
            if pos - 1 >= 0:
                indexes_up.add(pos - 1)
            if pos + 1 < size:
                indexes_up.add(pos + 1)
            p1_ans += 1
        else:
            indexes_up.add(pos)
    prev_indexes = indexes_up

print("Answer to part 1: ", p1_ans)

p2_ans = 0
prev_positions = {S_location: 1}
for line in diagram_lines:
    new_pos = {}
    for pos, count in prev_positions.items():
        if line[pos] == "^":
            if pos - 1 >= 0:
                new_pos[pos - 1] = new_pos.get(pos - 1, 0) + count
            if pos + 1 < size:
                new_pos[pos + 1] = new_pos.get(pos + 1, 0) + count
        else:
            new_pos[pos] = new_pos.get(pos, 0) + count

    prev_positions = new_pos
p2_ans = sum(prev_positions.values())
print("Answer to part 2: ", p2_ans)