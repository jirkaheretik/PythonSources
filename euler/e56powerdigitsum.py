def sum_number(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
    return sum

# main:
max_sum = 0
for a in range(99, 20, -1):
    for b in range(99, 20, -1):
        sum = sum_number(a ** b)
        if sum > max_sum:
            max_sum = sum
            print(f"{a}^{b} has sum {sum}")