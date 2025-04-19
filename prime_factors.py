'''
Реализовать функцию (или тело функции), которая
при введении натурального числа n разбивает его на 
простые множители (представить его в виде произведения простых чисел).
'''


def prime_factors(n: int) -> list[int]:
    factors = []
    
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    
    i = 3
    max_factor = int(n**0.5) + 1
    while i <= max_factor:
        while n % i == 0:
            factors.append(i)
            n = n // i
            max_factor = int(n**0.5) + 1 
        i += 2
    
    if n > 1:
        factors.append(n)
    
    return factors


n = 56
print(prime_factors(n))  # Вывод: [2, 2, 2, 7]

# Оптимальность решения по времени O(√n) и памяти O(1)
