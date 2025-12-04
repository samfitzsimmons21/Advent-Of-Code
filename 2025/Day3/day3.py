
with open("input.txt") as f:
    lines = f.read().splitlines()

total_p1 = 0
for bank in lines:
    highest = -1
    second_highest = -2

    bank_size = len(bank)
    for i, battery in enumerate(bank):

        battery = int(battery)

        if battery > highest and i != bank_size - 1:
            highest = battery
            second_highest = int(bank[i + 1])

        elif battery > second_highest:
            second_highest = battery


    total_p1 += (highest * 10) + second_highest

print(f"Answer to part 1 is: {total_p1}")

total_p2 = 0
k_max = 12

for bank in lines:
    size = len(bank)
    ans = ""

    left = 0
    while left < size and len(ans) < k_max:
        right = size - (k_max - len(ans))
        if right < left:
            break

        window = bank[left : right + 1]
        int_list = list(map(int, window))
        if not int_list:
            break

        max_value = max(int_list)
        max_index = int_list.index(max_value)
        left = left + max_index + 1
        ans += str(max_value)

    print(f"for bank {bank} string {ans} int {int(ans)}")
    total_p2 += int(ans)

print(f"Answer to part 2 is: {total_p2}")





