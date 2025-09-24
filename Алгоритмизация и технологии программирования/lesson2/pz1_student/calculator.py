"""
Модуль 1: calculator.py (Математическое ядро)
Задачи:

Реализовать базовые арифметические операции:
[+] Сложение, вычитание, умножение, деление
[+] Проверка деления на ноль с выбрасыванием исключения
Реализовать научные операции с использованием math:
[+] Возведение в степень
[+] Квадратный корень (с проверкой отрицательного входного значения)
[+] Натуральный логарифм и логарифм по произвольному основанию
[+] Тригонометрические функции (синус, косинус, тангенс)
[+] Факториал (с проверкой неотрицательного целого числа)

Требования к функциям:
[+] Все функции должны проверять корректность входных параметров
[+] При ошибках - выбрасывать исключения с понятными сообщениями
[+] Каждая функция должна возвращать результат вычислений
"""

import math

# Сложение
def add(a: int | float, b: int | float) -> int | float:
    return a + b

# Вычитание
def subtract(a: int | float, b: int | float) -> int | float:
    return a - b

# Умножение
def multiply(a: int | float, b: int | float) -> int | float:
    return a * b

# Деление
def divide(a: int | float, b: int | float) -> float:
    if b == 0:
        raise ValueError("Деление на ноль невозможно.")
    return a / b

# Возведение в степень
def power(a: int | float, b: int | float) -> int | float:
    return math.pow(a, b)

# Квадратный корень
def square_root(a: int | float) -> float:
    if a < 0:
        raise ValueError("Невозможно вычислить квадратный корень из отрицательного числа.")
    return math.sqrt(a)

# Натуральный логарифм
def natural_log(a: int | float) -> float:
    if a <= 0:
        raise ValueError("Натуральный логарифм определен только для положительных чисел.")
    return math.log(a)

# Логарифм по произвольному основанию
def log_base(a: int | float, base: int | float) -> float:
    if a <= 0 or base <= 0:
        raise ValueError("Логарифм определен только для положительных чисел.")
    return math.log(a, base)

# Тригонометрические функции
def sin(angle: int | float) -> float:
    return math.sin(angle)

def cos(angle: int | float) -> float:
    return math.cos(angle)

def tan(angle: int | float) -> float:
    return math.tan(angle)

# Факториал
def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Факториал определен только для неотрицательных целых чисел.")
    return math.factorial(n)