"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    result = []
    for arg in args:
        result.append(arg**2)
    return result


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(n):
    k = 0
    for i in range(2, n // 2 + 1):
        if (n % i == 0):
            k = k + 1
    if (k <= 0):
        return True
    else:
        return False


def filter_numbers(numbers, filter_type=None):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    def is_odd(n):
        return n % 2 != 0

    def is_even(n):
        return n % 2 == 0

    if filter_type == ODD:
        return list(filter(is_odd, numbers))
    elif filter_type == EVEN:
        return list(filter(is_even, numbers))
    elif filter_type == PRIME:
        return list(filter(is_prime, numbers))



