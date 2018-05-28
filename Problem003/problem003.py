def is_prime_number(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    else:
        xs = range(2,n-1)
        for x in xs:
            if n % x == 0:
                return False
    return True

prob_num = 600851475143
nums = range(2,prob_num)
max_prime_num = 2
prime_nums = []
for num in nums:
    if is_prime_number(num):
        max_prime_num = num
        prime_nums.append(num)

print(prime_nums)
print(max_prime_num)