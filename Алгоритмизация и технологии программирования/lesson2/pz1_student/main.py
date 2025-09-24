"""
Общие требования:
[+] Реализовать модульную архитектуру с четким разделением ответственности
[+] Применять функции модуля math для математических операций
[+] Обеспечить обработку ошибок и проверку входных данных
[+] Соблюдать принцип единственной ответственности для каждого модуля

Модуль 3: main.py (Основная программа)
Задачи:

Организовать демонстрацию работы всех модулей:
[+] Импортировать необходимые функции из других модулей
Продемонстрировать работу базовых и научных операций

Реализовать тестовые сценарии:
Демонстрация работы с отдельными математическими операциями
Примеры корректных вычислений и обработки ошибок
Примеры работы с тригонометрическими функциями

Организовать структурированный вывод:
[+] Отдельные секции для разных типов операций
[+] Четкое отображение входных данных и результатов
[+] Вывод сообщений об ошибках при некорректных операциях
Показать взаимодействие между модулями:
[+] Использование функций из calculator.py для вычислений
[+] Применение утилит из utils.py для преобразования и форматирования

Примеры тестовых сценариев для main.py
Арифметические операции с разными числами
Вычисление квадратных корней из положительных чисел и обработка попытки извлечения корня из отрицательного числа
Работа с тригонометрическими функциями (вычисление синуса, косинуса для углов в градусах и радианах)
Вычисление факториалов для разных чисел
Примеры с обработкой ошибок (деление на ноль, логарифм от отрицательного числа)
"""

from math import e as math_e
from math import pi as math_pi

import calculator as calc
import utils as util

print("--- Научный калькулятор ---\n")

prog_list = [
    '1 - Арифметические',
    '2 - Научные',
    '3 – Тест программы'
]

science_prog_list = [
    '1 - Возведение в степень',
    '2 - Извлечение квадратного корня',
    '3 - Натуральный логарифм',
    '4 - Логарифм по произвольному основанию',
    '5 - Косинус (градусы)',
    '6 - Синус (градусы)',
    '7 - Тангенс (градусы)',
    '8 - Косинус (радианы)',
    '9 - Синус (радианы)',
    '10 - Тангенс (радианы)',
    '11 - Факториал'
]

while True:
    operation = int(input(f"{'\n'.join(prog_list)}\nВыберите операцию: "))
    match operation:
        case 1:
            a = input("\nВведите первое число: ")
            b = input("Введите второе число: ")
            op = input("Введите операцию (+, -, *, /): ")
            try:
                a = float(a)
                b = float(b)
                match op:
                    case "+":
                        result = calc.add(a, b)
                    case "-":
                        result = calc.subtract(a, b)
                    case "*":
                        result = calc.multiply(a, b)
                    case "/":
                        result = calc.divide(a, b)
                    case _:
                        raise ValueError("Некорректная операция. Возврат в меню...")
                print(util.operation_format(op, a, b))
                print(util.format_result(result))
            except Exception as e:
                print(f"\nОшибка: {e}")
        case 2:
            suboperation = int(input(f"\n{'\n'.join(science_prog_list)}\nВыберите суб-операцию: "))
            try:
                match suboperation:
                    case 1:
                        a = float(input("\nВведите число: "))
                        b = float(input("Введите степень: "))
                        result = calc.power(a, b)
                        print(util.operation_format("возвести в степень", a, b))
                        print(util.format_result(result))
                    case 2:
                        a = float(input("\nВведите число: "))
                        result = calc.square_root(a)
                        print(util.operation_format("найти квадратный корень", a))
                        print(util.format_result(result))
                    case 3:
                        a = float(input("\nВведите число: "))
                        result = calc.natural_log(a)
                        print(util.operation_format("ln", a))
                        print(util.format_result(result))
                    case 4:
                        a = float(input("\nВведите число: "))
                        b = float(input("Введите основание логарифма: "))
                        result = calc.log_base(a, b)
                        print(util.operation_format(f"log{b}", a))
                        print(util.format_result(result))
                    case 5:
                        angle = float(input("\nВведите угол в градусах: "))
                        rad = util.deg2rad(angle)
                        result = calc.cos(rad)
                        print(util.operation_format("cos°", angle))
                        print(util.format_result(result))
                    case 6:
                        angle = float(input("\nВведите угол в градусах: "))
                        rad = util.deg2rad(angle)
                        result = calc.sin(rad)
                        print(util.operation_format("sin°", angle))
                        print(util.format_result(result))
                    case 7:
                        angle = float(input("\nВведите угол в градусах: "))
                        rad = util.deg2rad(angle)
                        result = calc.tan(rad)
                        print(util.operation_format("tan°", angle))
                        print(util.format_result(result))
                    case 8:
                        rad = float(input("\nВведите угол в радианах: "))
                        result = calc.cos(rad)
                        print(util.operation_format("cos(rad)", rad))
                        print(util.format_result(result))
                    case 9:
                        rad = float(input("\nВведите угол в радианах: "))
                        result = calc.sin(rad)
                        print(util.operation_format("sin(rad)", rad))
                        print(util.format_result(result))
                    case 10:
                        rad = float(input("\nВведите угол в радианах: "))
                        result = calc.tan(rad)
                        print(util.operation_format("tan(rad)", rad))
                        print(util.format_result(result))
                    case 11:
                        a = int(input("\nВведите число: "))
                        result = calc.factorial(a)
                        print(util.operation_format("!", a))
                        print(util.format_result(result))
                    case _:
                        raise ValueError("Некорректная суб-операция. Возврат в меню...")
            except Exception as e:
                print(f"\nОшибка: {e}")
        case 3:
            print("\n--- Тест программы ---")
            print("1. Арифметические операции:")
            a, b = 10, 5
            print(util.operation_format("+", a, b), util.format_result(calc.add(a, b)))
            print(util.operation_format("-", a, b), util.format_result(calc.subtract(a, b)))
            print(util.operation_format("*", a, b), util.format_result(calc.multiply(a, b)))
            print(util.operation_format("/", a, b), util.format_result(calc.divide(a, b)))
            print(util.operation_format("/", a, 0), end=" ")
            try:
                print(util.format_result(calc.divide(a, 0)))
            except Exception as e:
                print(f"Ошибка: {e}")
            print("\n2. Научные операции:")
            print(util.operation_format("возвести в степень", 2, 3), util.format_result(calc.power(2, 3)))
            print(util.operation_format("найти квадратный корень", 16), util.format_result(calc.square_root(16)))
            print(util.operation_format("найти квадратный корень", -4), end=" ")
            try:
                print(util.format_result(calc.square_root(-4)))
            except Exception as e:
                print(f"Ошибка: {e}")
            print(util.operation_format("ln", math_e), util.format_result(calc.natural_log(math_e)))
            print(util.operation_format("ln", -1), end=" ")
            try:
                print(util.format_result(calc.natural_log(-1)))
            except Exception as e:
                print(f"Ошибка: {e}")
            print(util.operation_format("log10", 100), util.format_result(calc.log_base(100, 10)))
            print(util.operation_format("log1", 10), end=" ")
            try:
                print(util.format_result(calc.log_base(10, 1)))
            except Exception as e:
                print(f"Ошибка: {e}")
            angle_deg = 60
            angle_rad = util.deg2rad(angle_deg)
            print(util.operation_format("cos°", angle_deg), util.format_result(calc.cos(angle_rad)))
            print(util.operation_format("sin°", angle_deg), util.format_result(calc.sin(angle_rad)))
            print(util.operation_format("tan°", angle_deg), util.format_result(calc.tan(angle_rad)))
            angle_rad = math_pi / 3
            print(util.operation_format("cos(rad)", angle_rad), util.format_result(calc.cos(angle_rad)))
            print(util.operation_format("sin(rad)", angle_rad), util.format_result(calc.sin(angle_rad)))
            print(util.operation_format("tan(rad)", angle_rad), util.format_result(calc.tan(angle_rad)))
            print(util.operation_format("!", 5), util.format_result(calc.factorial(5)))
            print(util.operation_format("!", -3), end=" ")
            try:
                print(util.format_result(calc.factorial(-3)))
            except Exception as e:
                print(f"Ошибка: {e}")
            print("\n--- Конец теста ---\n")
        case _:
            print("\nНекорректная начальная операция. Завершение программы...")
            break
                    
