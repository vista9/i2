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
найти лучше студента по среднему баллу
"""

for student in students.items():
    student[1]['grades_mark'] = sum(student[1]['grades'].values()) / len(student[1]['grades'].values())

best_student_id = max(students, key=lambda x: students[x]['grades_mark'])
print(f"Лучший студент: {best_student_id} ({students[best_student_id]['name']}), ср. балл: {students[best_student_id]['grades_mark']:.2f}")