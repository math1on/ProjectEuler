list = range(1,1000)
result = 0
for num in list:
    if num % 3 == 0:
        result += num
    elif num % 5 == 0:
        result += num

print(result)
