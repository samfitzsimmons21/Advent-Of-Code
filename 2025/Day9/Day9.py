def calc_area(p1, p2):
    return (abs(p2[0] - p1[0]) + 1) * (abs(p2[1] - p1[1]) + 1)

with open("input.txt") as f:
    lines = f.read().splitlines()

points = [tuple(map(int, line.split(","))) for line in lines]

largest_i = float('-inf')
largest_j = float('-inf')
largest_area = 0
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        area = calc_area(points[i], points[j])
        if area > largest_area:
            largest_area = area
            largest_i = i
            largest_j = j
print(f"Answer to part 1: ", largest_area)
