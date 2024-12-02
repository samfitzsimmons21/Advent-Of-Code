with open("input.txt") as f:
    data = [list(map(int, line.split())) for line in f.readlines()]

def is_safe(sequence):
    inc_flag = False
    dec_flag = False
    n = len(sequence)
    for i in range(1, n):
        diff = abs(sequence[i] - sequence[i - 1])
        if diff not in range(1, 4):  
            return False
        
        if sequence[i] > sequence[i - 1]:
            inc_flag = True

        if sequence[i] < sequence[i - 1]:
            dec_flag = True

        if inc_flag and dec_flag: 
            return False
    return True

safe_amount = 0
for record in data:

    if is_safe(record):
        safe_amount += 1
        continue

    n = len(record)
    for i in range(n):

        parsed_record = record[:i] + record[i + 1:]
        if is_safe(parsed_record):
            safe_amount += 1
            break  

print(safe_amount)

        