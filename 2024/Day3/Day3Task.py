import re

pattern = r"mul\(\d+,\d+\)|do\(\)|don't\(\)" 
matches = re.findall(pattern, open("input.txt").read()) 

ans = 0
enabled = True
for match in matches:
    if match == "do()":
        enabled = True
    elif match == "don't()":
        enabled = False
    else:
        if enabled:
            x, y = map(int, match[4:-1].split(","))
            ans += x * y

print(ans)
