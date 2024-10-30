numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = False
i = 0
j = 0
for i in range(0, len(numbers)):
    if numbers[i] == 1 :
        i += i
    if numbers[i] == 2 :
        primes.append(numbers[i])
    for j in range(0, i ):
        if numbers[j] != 1:
            if numbers[i] % numbers[j] == 0:
                is_prime = False
                not_primes.append(numbers[i])
                break
            else:
                is_prime = True
                j += j
    else:
        j += j
    if is_prime == True:
        primes.append(numbers[i])
    i += i

print(primes, not_primes)