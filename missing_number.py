'''
Реализовать функцию (или тело функции), которая находит единственное отсутствующее число 
из последовательности натуральных чисел 1, 2, …, n.
'''

def missing_number(nums: list[int]) -> int:
    n = len(nums) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum


nums = [1, 2, 3, 4, 5, 6, 8, 9, 10, 11]
print(missing_number(nums))  # 7

# Оптимальность решения по времени O(n) и памяти O(1).
