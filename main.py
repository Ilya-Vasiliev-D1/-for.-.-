numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []
not_primes = []

for j in numbers:
    if j < 2:  # Числа меньше 2 не являются простыми
        continue  # Пропуска числа 1 и всех отрицательных чисел

    is_prime = True
    for i in range(2, int(j ** 0.5) + 1):  # Проверка делителя до квадратного корня числа
        if j % i == 0:
            is_prime = False
            break

    if is_prime:
        primes.append(j)
    else:
        not_primes.append(j)

print("Primes:", primes)
print("Not Primes:", not_primes)
