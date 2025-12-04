
with open('input.txt', 'r') as file:
    lines = file.read().splitlines()

directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

n = len(lines)
m = len(lines[0])

p1_ans = 0
limit = 4
for i in range(n):
    for j in range(m):
        if lines[i][j] == '@':
            count = 0
            for di, dj in directions:
                if 0 <= i + di < n and 0 <= j + dj < m:
                    if lines[i + di][j + dj] == '@':
                        count += 1

            if count < limit:
                p1_ans += 1

print("Part 1 Answer:", p1_ans)

p2_ans = 0


while True:
    stored = []
    for i in range(n):
        for j in range(m):
            if lines[i][j] != '@':
                continue

            count = 0
            for di, dj in directions:
                if 0 <= i + di < n and 0 <= j + dj < m:
                    if lines[i + di][j + dj] == '@':
                        count += 1

            if count < limit:
                p2_ans += 1
                stored.append((i, j))

    if len(stored) == 0:
        break

    for i, j in stored:
        lines[i] = lines[i][:j] + '.' + lines[i][j+1:]

print("Part 2 Answer:", p2_ans)
