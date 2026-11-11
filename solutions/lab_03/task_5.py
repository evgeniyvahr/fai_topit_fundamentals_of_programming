def mean(values):
    """
    Контракт:
        Входные данные: values - список чисел.
        Выходные данные: среднее арифметическое.
        Особые случаи: пустой список -> None.
    """
    if not values:
        return None
    return sum(values) / len(values)


def minimum(values):
    """
    Контракт:
        Входные данные: values - список чисел.
        Выходные данные: минимальное значение.
        Особые случаи: пустой список -> None.
    """
    mn = 100000
    if not values:
        return None
    for i in values:
        if i < mn:
            mn = i
    return mn


def maximum(values):
    """
    Контракт:
        Входные данные: values - список чисел.
        Выходные данные: максимально значение.
        Особые случаи: пустой список -> None.
    """
    mx = 0
    if not values:
        return None
    for i in values:
        if i > mx:
            mx = i
    return mx


def classify(score):
    """
    Контракт:
        Входные данные: score - число (0 - 100).
        Выходные данные: строка (категория результата).
        Особые случаи: None -> нет данных
    """
    if score is None:
        return "Нет данных"
    elif score < 60:
        return "Недостаточный"
    elif score < 75:
        return "Удовлетворительный"
    elif score < 90:
        return "Хороший"
    else:
        return "Отличный"


def student_summary(name, results):
    """
    Контракт:
        Входные данные: name - строка (имя студента), results - список чисел.
        Выходные данные: словарь с ключами:
            Имя, Результаты, Средний результат, Минимальный результат, Максимальный результат, Категория
        Особые случаи: пустой список -> средний/минимальный/максимальный результаты = None, Категория = "нет данных"
    """
    return {
        "Имя": name,
        "Результаты": results,
        "Средний результат": mean(results),
        "Минимальный результат": minimum(results),
        "Максимальный результат": maximum(results),
        "Категория": classify(mean(results)),
    }


def find_top_students(students):
    """
    Контракт:
        Входные данные: students - словарь {имя: [результаты]}
        Выходные данные: список имён лидеров
        Особые случаи: пустой словарь -> []
    """
    if not students:
        return None
    means = {}
    for name, results in students.items():
        if results:
            means[name] = mean(results)
    if not means:
        return None
    max_mean = maximum(list(means.values()))
    return [name for name, mean_1 in means.items() if mean_1 == max_mean]


def group_summary(students):
    """
    Контракт:
        Входные данные: students - словарь {имя: [результаты]}
        Выходные данные: словарь с ключами
            Студенты (student_summary), Средний результат группы, Количество студентов в каждой категории, Лидеры
        Особые случаи: пустой словарь -> все значения None/0/[]
    """
    if not students:
        return "Нет данных"
    student_stats = []
    all_results = []
    category_counts = {
        "Нет данных": 0,
        "Недостаточный": 0,
        "Удовлетворительный": 0,
        "Хороший": 0,
        "Отличный": 0,
    }
    for name, results in students.items():
        summary = student_summary(name, results)
        student_stats.append(summary)
        all_results.extend(results)
        if summary["Категория"] in category_counts:
            category_counts[summary["Категория"]] += 1
    group_mean = mean(all_results) if all_results else None
    top_students = find_top_students(students)
    return {
        "Студенты": student_stats,
        "Средний результат группы": group_mean,
        "Количество студентов в каждой категории": category_counts,
        "Лидеры": top_students
    }


def format_report(student_data, group_data):
    """
    Контракт:
        Входные данные: student_data - список словарей student_summary, group_data - словарь group_summary
        Выходные данные: строка - текстовый отчёт
        Особые случаи: пустые данные -> "нет данных"
    """
    report = []
    report.append("Отчёт по результатам группы")
    if not student_data:
        report.append("Нет данных о студентах")
        return '\n'.join(report)
    report.append("\nСтатистика по студентам:")
    for s in student_data:
        report.append(f"Студент: {s['Имя']}")
        report.append(f"Результаты: {s['Результаты']}")
        if s["Средний результат"] is not None:
            report.append(f"Средний результат: {s['Средний результат']:.2f}")
            report.append(f"Минимальный результат: {s['Минимальный результат']}")
            report.append(f"Максимальный результат: {s['Максимальный результат']}")
            report.append(f"Категория: {s['Категория']}")
        else:
            report.append("Нет данных о результатах студента")
        report.append('\n')
    report.append(f"Статистика группы:")
    if group_data["Средний результат группы"] is not None:
        report.append(f"Средний результат группы: {group_data['Средний результат группы']:.2f}")
    else:
        report.append("Нет данных о результатах группы")
    report.append("\nКоличество студентов по категориям:")
    for cat, count in group_data["Количество студентов в каждой категории"].items():
        report.append(f"{cat}: {count}")
    report.append("\nЛидеры")
    if group_data["Лидеры"]:
        for name in group_data["Лидеры"]:
            report.append(f"- {name}")
    else:
        report.append("Нет данных о лидерах")
    return '\n'.join(report)


students_1 = {
    "Анна": [78, 91, 84, 88],
    "Борис": [60, 72, 68],
    "Дарья": [95, 93, 97, 90],
    "Илья": [55, 61],
}
students_2 = {"Анна": [79, 86, 92]}
students_3 = {
    "Анна": [80, 70, 90],
    "Борис": [80, 80, 80],
    "Дарья": [71, 75, 81]
}
students_4 = {}
students_5 = {
    "Анна": [100, 86, 78],
    "Борис": []
}
students_6 = {
    "Анна": [59],
    "Борис": [60],
    "Виктор": [74],
    "Глеб": [75],
    "Дарья": [89],
    "Евгений": [90],
}


def checker(data):
    student_data = [student_summary(name, results) for name, results in data.items()]
    group_data = group_summary(data)
    report = format_report(student_data, group_data)
    return report


print(f"Сценарий: Обычный набор данных\n {checker(students_1)}\n")
print(f"Сценарий: Один студент\n {checker(students_2)}\n")
print(f"Сценарий: Несколько лидеров\n {checker(students_3)}\n")
print(f"Сценарий: Пустая группа\n {checker(students_4)}\n")
print(f"Сценарий: Студент без результатов\n {checker(students_5)}\n")
print(f"Сценарий: Граничные значения категорий\n {checker(students_6)}\n")
