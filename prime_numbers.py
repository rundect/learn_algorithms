def prime_numbers(n):
    list_prime_numbers = []
    for i in range(2, n + 1):
        k = 0
        for j in range(1, i + 1):
            if i % j == 0:
                k = k + 1
        if k <= 2:
            list_prime_numbers.append(i)
    return list_prime_numbers


print(prime_numbers(43))
