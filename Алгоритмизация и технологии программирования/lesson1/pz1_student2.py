students = {
    101: {
        "name": "Иван Иванов",
        "age": 20,
        "grades": {"math": 4, "physics": 5, "programming": 5},
        "group": "ИТ-101"
    },
    102: {
        "name": "Мария Петрова", 
        "age": 19,
        "grades": {"math": 5, "physics": 4, "programming": 4},
        "group": "ИТ-101"
    },
    103: {
        "name": "Алексей Сидоров",
        "age": 21, 
        "grades": {"math": 3, "physics": 3, "programming": 4},
        "group": "ИТ-102"
    }
}

"""
1
Выведите на экран информацию о всех студентах в читаемом формате. Для каждого студента отобразите:
ID студента
Имя
Возраст
Группу
Все оценки по предметам
"""

for student in students.items():
    print(f"ID студента: {student[0]}")
    print(f"Имя: {student[1]['name']}")
    print(f"Возраст: {student[1]['age']}")
    print(f"Группа: {student[1]['group']}")
    print("Оценки:")
    for subject, grade in student[1]['grades'].items():
        print(f"– {subject}: {grade}")
    print()

"""
2
Добавьте в словарь нового студента с ID 104:
Имя: "Екатерина Волкова"
Возраст: 20
Оценки: math=5, physics=5, programming=5
Группа: "ИТ-102"
Выведите сообщение о добавлении.
"""

last_index = max(students.keys())
students[last_index + 1] = {
    "name": "Екатерина Волкова",
    "age": 20,
    "grades": {"math": 5, "physics": 5, "programming": 5},
    "group": "ИТ-102"
}

"""
3
Для каждого студента рассчитайте и выведите средний балл по всем предметам. Сохраните результаты в отдельный словарь average_grades.
"""

average_grades = {}
for student in students.items():
    average_grades[student[0]] = sum(student[1]['grades'].values()) / len(student[1]['grades'])
    print(f"Ср. балл студента с ID {student[0]}: {average_grades[student[0]]:.2f}")

"""
4
Найдите студента с наивысшим средним баллом. Выведите его имя, средний балл и группу.
"""

best_student_id = max(students, key=lambda id: average_grades[id])
print()
print(f"Лучший студент по успеваемости:")
print(f"Имя: {students[best_student_id]['name']}")
print(f"Средний балл: {average_grades[best_student_id]:.2f}")
print(f"Группа: {students[best_student_id]['group']}")

"""
5
Соберите статистику по группам:
Количество студентов в каждой группе
Средний балл группы
Список студентов каждой группы
Выведите статистику для групп "ИТ-101" и "ИТ-102".
"""

students_count = {}
for student in students.items():
    if not student[1]['group'] in students_count:
        students_count[student[1]['group']] = 1
    else:
        students_count[student[1]['group']] += 1

print()
print("Количество студентов по группам:")
for count in students_count.items():
    print(f"– {count[0]}: {count[1]}")

"""
6
Для каждого студента вычислите хеш его имени с помощью функции hash(). Проверьте, есть ли коллизии хешей (одинаковые хеши для разных имен).
"""

name_hashes = {}
for student in students.items():
    new_hash = hash(student[1]['name'])
    if new_hash in name_hashes.values():
        print(f'[ОШИБКА] Обнаружен уже добавленный хэш: {new_hash}')
    else:
        name_hashes[student[0]] = new_hash

print()
print(name_hashes)

"""
7
Найдите и выведите:
Всех студентов с оценкой 5 по программированию
Всех студентов старше 20 лет
"""

print()
for student in students.items():
    if student[1]['grades']['programming'] == 5 and student[1]['age'] > 20:
        print(student[1]['name'])

"""
8
Добавьте всем студентам оценку по предмету "english":
ID 101: 4
ID 102: 5
ID 103: 3
ID 104: 5
Выведите обновленные данные для студента ID 101.
"""

new_marks = [
    { "id": 101, "lesson_name": "english", "mark": 4 },
    { "id": 102, "lesson_name": "english", "mark": 5 },
    { "id": 103, "lesson_name": "english", "mark": 3 },
    { "id": 104, "lesson_name": "english", "mark": 5 },
]

for new_mark in new_marks:
    students[new_mark['id']]['grades'][new_mark['lesson_name']] = new_mark['mark']

print()
print('Оценки студента с ID 101:')
for subject, grade in students[101]['grades'].items():
    print(f"– {subject}: {grade}")