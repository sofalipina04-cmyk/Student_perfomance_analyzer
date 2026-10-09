# Система анализа успеваемости студентов
# Язык программирования: Python

students = {
    "Анна": {"Математика": 5, "Информатика": 5, "Английский": 4},
    "Иван": {"Математика": 3, "Информатика": 4, "Английский": 4},
    "Мария": {"Математика": 5, "Информатика": 4, "Английский": 5},
    "Дмитрий": {"Математика": 2, "Информатика": 3, "Английский": 4},
    "Елена": {"Математика": 4, "Информатика": 5, "Английский": 5},
}


def average_grade(grades):
    """Возвращает средний балл по списку оценок."""
    return sum(grades.values()) / len(grades)


def performance_level(average):
    """Определяет условный уровень успеваемости."""
    if average >= 4.5:
        return "Отличная"
    elif average >= 3.5:
        return "Хорошая"
    elif average >= 3:
        return "Удовлетворительная"
    return "Требует внимания"


def show_student_report(name, grades):
    average = average_grade(grades)
    print(f"\nСтудент: {name}")
    for subject, grade in grades.items():
        print(f"  {subject}: {grade}")
    print(f"  Средний балл: {average:.2f}")
    print(f"  Уровень: {performance_level(average)}")


def show_all_students():
    print("\n=== УСПЕВАЕМОСТЬ СТУДЕНТОВ ===")
    for name, grades in students.items():
        show_student_report(name, grades)


def show_ranking():
    ranking = sorted(
        students.items(),
        key=lambda item: average_grade(item[1]),
        reverse=True
    )
    print("\n=== РЕЙТИНГ ГРУППЫ ===")
    for position, (name, grades) in enumerate(ranking, start=1):
        print(f"{position}. {name} — {average_grade(grades):.2f}")


def show_subject_statistics():
    subjects = students[next(iter(students))].keys()
    print("\n=== СТАТИСТИКА ПО ПРЕДМЕТАМ ===")
    for subject in subjects:
        grades = [data[subject] for data in students.values()]
        average = sum(grades) / len(grades)
        best = max(grades)
        print(
            f"{subject}: средний балл {average:.2f}; "
            f"максимальная оценка {best}"
        )


def show_group_summary():
    averages = {
        name: average_grade(grades)
        for name, grades in students.items()
    }
    group_average = sum(averages.values()) / len(averages)
    best_student = max(averages, key=averages.get)
    needs_help = [
        name for name, average in averages.items() if average < 3.5
    ]

    print("\n=== ИТОГОВЫЙ ОТЧЁТ ===")
    print(f"Количество студентов: {len(students)}")
    print(f"Средний балл группы: {group_average:.2f}")
    print(
        f"Лучший результат: {best_student} "
        f"({averages[best_student]:.2f})"
    )
    if needs_help:
        print("Студенты, которым может понадобиться помощь:")
        for name in needs_help:
            print(f"  - {name}")
    else:
        print("Студентов с низким средним баллом нет.")


def main():
    while True:
        print("\n===== АНАЛИЗ УСПЕВАЕМОСТИ =====")
        print("1. Отчёт по всем студентам")
        print("2. Рейтинг группы")
        print("3. Статистика по предметам")
        print("4. Итоговый отчёт")
        print("5. Выход")

        choice = input("Выберите действие: ").strip()

        if choice == "1":
            show_all_students()
        elif choice == "2":
            show_ranking()
        elif choice == "3":
            show_subject_statistics()
        elif choice == "4":
            show_group_summary()
        elif choice == "5":
            print("Работа программы завершена.")
            break
        else:
            print("Ошибка: выберите пункт от 1 до 5.")


if __name__ == "__main__":
    main()
