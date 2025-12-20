import math

class DisjointSetUnion:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        if self.size[root_x] < self.size[root_y]:
            root_x, root_y = root_y, root_x

        self.parent[root_y] = root_x
        self.size[root_x] += self.size[root_y]
        return True

    def get_component_sizes(self):
        sizes = {}
        for i in range(len(self.parent)):
            root = self.find(i)
            sizes[root] = self.size[root]
        return list(sizes.values())

def triplet_distance(val1, val2):
    dx = val1[0] - val2[0]
    dy = val1[1] - val2[1]
    dz = val1[2] - val2[2]
    return math.sqrt(dx * dx + dy * dy + dz * dz)

with open("input.txt", "r") as file:
    lines = file.read().splitlines()

vals = []
for line in lines:
    a, b, c = map(int, line.split(","))
    vals.append((a, b, c))

edges = []
for i in range(len(vals)):
    for j in range(i + 1, len(vals)):
        dist = triplet_distance(vals[i], vals[j])
        edges.append((dist, i, j))
edges.sort()

uf = DisjointSetUnion(len(vals))
connections_made = 0
for dist, i, j in edges:
    uf.union(i, j)
    connections_made += 1
    if connections_made == 1000:
        break

sizes = sorted(uf.get_component_sizes(), reverse=True)
print("Part 1 Answer: ", sizes[0] * sizes[1] * sizes[2])

uf = DisjointSetUnion(len(vals))
connections_made = 0
for dist, i, j in edges:
    uf.union(i, j)

    if len(uf.get_component_sizes()) == 1:
        break
    connections_made += 1

_, i, j = edges[connections_made]
print("Part 2 Answer: ", vals[i][0] * vals[j][0])