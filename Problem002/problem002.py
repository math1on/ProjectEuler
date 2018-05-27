num1 = 1
num2 = 1
num_sum = 0
fibonacci = [num1]
while num1 + num2 < 4000000:
    tmp  = num2
    num2 = num1 + num2
    num1 = tmp
    fibonacci.append(num2)
    if num2 % 2 == 0:
        num_sum += num2

print(num2)
print(fibonacci)
print(num_sum)
