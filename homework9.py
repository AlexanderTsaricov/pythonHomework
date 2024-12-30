# Task 1
from collections.abc import Callable
from functools import wraps
from time import sleep


def how_are_you(func):
    def decorator(*args, **kwargs):
        print("How are you?")
        input("Your answer: ")
        print("Ok, i'm are not ok...")
        result = func(*args, **kwargs)
        return result
    return decorator

@how_are_you
def testFunc(a, b):
    return a + b


# Task 2

def wait(func):
    def decorator(*args, **kwargs):
        sleep(5)
        result = func(*args, **kwargs)
        return result
    return decorator
@wait
def testFunc(a, b):
    return a + b

# Task 3

def counter(func: Callable) -> Callable:
    counter.count = 0
    def decorator(*args, **kwargs):
        result = func(*args, **kwargs)
        counter.count += 1
        print(f'func use {counter.count}')
        return result
    return decorator
@counter
def testFunc(a, b):
    return f'{a} + {b} = {a + b}'


# Task 4
def myCache(func):
    arrCache = {}
    @wraps(func)
    def wrapper(*args):
        if args not in arrCache:
            print('Use func')
            arrCache[args] = func(*args)
        return arrCache[args]
    return wrapper

@myCache
def fibonacci(n: int) -> int:
    """
    Вычисляет n-ное число Фибоначчи с использованием итеративного подхода.
    :param n: Позиция числа Фибоначчи (нумерация с 0).
    :return: n-ное число Фибоначчи.
    """
    if n <= 1:
        return n  # Первые два числа Фибоначчи — 0 и 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b



