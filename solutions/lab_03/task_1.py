def get_level(score, absences):
    a = ["отличный", "хороший", "удовлетворительный", "недостаточный"]
    i = 0
    if score >= 90:
        i = 0
    elif score >= 75:
        i = 1
    elif score >= 60:
        i = 2
    else:
        i = 3
    if absences > 3 and i < 3:
        i += 1
    return a[i]


def get_type(work_type):
    match work_type:
        case "exam":
            return "экзаменационная работа"
        case "project":
            return "проектная работа"
        case "practice":
            return "практическая работа"
        case _:
            return "неизвестный тип работы"


def process(score, work_type, absences):
    if score < 0 or score > 100:
        print("Недопустимое значение результата")
        return None
    if absences < 0 or absences > 5:
        print("Недопустимое значения пропусков")
        return None

    level = get_level(score, absences)
    work_desc = get_type(work_type)

    result = (f"Результат: {score}, Тип работы: {work_type} ({work_desc}), Пропуски: {absences}, Уровень: {level}")
    return result


records = [
        (0, "exam", 0),
        (59, "exam", 0),
        (60, "project", 2),
        (74, "practice", 3),
        (75, "exam", 0),
        (89, "project", 1),
        (90, "practice", 0),
        (100, "exam", 1),
        (65, "practice", 4),
        (-5, "exam", 0),
]
level_counts = {"отличный": 0, "хороший": 0, "удовлетворительный": 0, "недостаточный": 0}
for score, work_type, absences in records:
    result = process(score, work_type, absences)
    if result: print(result)
    level = get_level(score, absences)
    level_counts[level] += 1

print("\nИтоговая сводка:")
for level, count in level_counts.items():
    print(f" {level}: {count}")
