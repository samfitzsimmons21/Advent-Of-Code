with open("input.txt") as f:
    data = [list(map(int, line.split())) for line in f.readlines()]

safe_amount = 0

def is_safe(sequence):
    inc_flag = False
    dec_flag = False
    n = len(sequence)
    for i in range(1, n):
        diff = abs(sequence[i] - sequence[i - 1])
        if diff < 1 or diff > 3:  
            return False
        if sequence[i] > sequence[i - 1]:
            inc_flag = True
        if sequence[i] < sequence[i - 1]:
            dec_flag = True
        if inc_flag and dec_flag: 
            return False
    return True

for line in data:

    if is_safe(line):
        safe_amount += 1
        continue

    n = len(line)
    for i in range(n):

        modified_line = line[:i] + line[i + 1:]
        if is_safe(modified_line):
            safe_amount += 1
            break  

print(safe_amount)

        