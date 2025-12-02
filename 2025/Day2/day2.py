import math
def factors(n):
    result = set()
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if i != n:
                result.add(i)
            other = n // i
            if other != n:
                result.add(other)
    return sorted(result)

with open("input.txt") as f:
    line = f.readlines()
    line = line[0].strip()

p1_total = 0
p2_total = 0

for val_range in line.split(","):
    start, end = map(int, val_range.split("-"))

    for i in range(start, end + 1):
        val = str(i)

        mid = len(val) // 2
        if val[:mid] == val[mid:]:
            p1_total += i

        # CASES ARE:
        # 1. a factor of the length has same numbers
        # 2. all digits same

        for factor_vals in factors(len(val)):
            match_vals = val[:factor_vals]
            if all(val[j:j+factor_vals] == match_vals for j in range(0, len(val), factor_vals)):
                p2_total += i
                break

print(f"Answer 1 is: {p1_total}") # 8576933996
print(f"Answer 2 is: {p2_total}") # 25663320831