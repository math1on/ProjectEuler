import math

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

# エラトステネスの篩
# step1:探索リストに2からnまでの整数を昇順で入れる。
# step2:探索リストの先頭の数を素数リストに移動し、その倍数を探索リストから篩い落とす。
# step3:上記の篩い落とし操作を探索リストの先頭値がxの平方根に達するまで行う。
# step4:探索リストに残った数を素数リストに移動して処理終了。
def sieve_of_eratosthenes(n):
    prime_num_list = []
    search_list = range(2,n)

    goal_num = math.sqrt(n)
    while search_list[0] < goal_num:
        move_num = search_list.pop(0)
        prime_num_list.append(move_num)

        try:
            while True:
                move_num *= 2
                i = search_list.index(move_num)
                prime_num_list.append(search_list[i])
        except ValueError:
            continue

    return prime_num_list


prob_num = 600851475143
prime_num_list = sieve_of_eratosthenes(prob_num)
print(prime_num_list)
print(prime_num_list[len(prime_num_list)])
