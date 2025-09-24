"""
Модуль 2: utils.py (Вспомогательные утилиты)
Задачи:

Реализовать утилиты преобразования единиц измерения:
[+] Функция преобразования градусов в радианы
[+] Функция преобразования радианов в градусы

Реализовать утилиты форматирования вывода:
[+] Функция форматирования математических операций для красивого вывода
[+] Функция создания строки с результатом вычисления

Реализовать утилиты для работы с данными:
[+] Функция проверки числа на целость
[+] Функция проверки числа на положительность

Требования:
[+] Все функции должны возвращать новые данные, не изменяя входные параметры
[+] Функции должны быть независимыми и самодостаточными
"""

import math
from typing import Any

def deg2rad(deg: int | float) -> float:
    return deg * (math.pi / 180)

def rad2deg(rad: int | float) -> float:
    return rad * (180 / math.pi)

def operation_format(op: str, a: int | float, b: int | float | None = None) -> str:
    return f"Операция: {a} {op} {b if b is not None else ''}"

def format_result(result: Any) -> str:
    return f"Результат: {result}"

def is_integer(num: int | float) -> bool:
    return num.is_integer()

def is_positive(num: int | float) -> bool:
    return num > 0