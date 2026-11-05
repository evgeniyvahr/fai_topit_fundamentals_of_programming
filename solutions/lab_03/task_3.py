submissions = [
    ("anna", "lab_01", 5),
    ("boris", "lab_01", 4),
    ("anna", "lab_02", 5),
    ("daria", "lab_01", 3),
    ("boris", "lab_02", 5),
    ("anna", "lab_01", 4),
]

students = set()
for student, lab, score in submissions:
    students.add(student)

labs = set()
for student, lab, score in submissions:
    labs.add(lab)

student_attempts = {}
for student, lab, score in submissions:
    if student not in student_attempts:
        student_attempts[student] = []
    student_attempts[student].append((lab, score))

best_results = {}
for student, lab, score in submissions:
    key = (student, lab)
    if key not in best_results or score > best_results[key]:
        best_results[key] = score

attempts_count = {}
for student, lab, score in submissions:
    key = (student, lab)
    if key not in attempts_count:
        attempts_count[key] = 1
    else:
        attempts_count[key] += 1

students_per_lab = {}
for student, lab, score in submissions:
    if lab not in students_per_lab:
        students_per_lab[lab] = set()
    students_per_lab[lab].add(student)
completed_all = students_per_lab["lab_01"]
completed_all &= students_per_lab["lab_02"]

# добавление новой записи
submissions.append(("dmitriy", "lab_01", 3))
student, lab, score = submissions[6]
students.add(student)
labs.add(lab)
if student not in student_attempts:
    student_attempts[student] = []
student_attempts[student].append((lab, score))
key = (student, lab)
if key not in best_results or score > best_results[key]:
    best_results[key] = score
if key not in attempts_count:
    attempts_count[key] = 1
else:
    attempts_count[key] += 1
if lab not in students_per_lab:
    students_per_lab = set()
students_per_lab[lab].add(student)

# практическое расширение


def process(request):
    parts = request.strip().split()
    if not parts:
        print("Пустой запрос")
        return
    command = parts[0]
    if command == "student":
        if len(parts) < 2:
            print("Неверное количество аргументов")
            return
        name = parts[1]
        attempts = student_attempts[name]
        if attempts is None:
            print("Студент не найден")
        else:
            print(f"Попытки {name}: ")
            for lab, score in attempts:
                print(f"{lab}: {score}")
    elif command == "best":
        if len(parts) < 3:
            print("Неверное количество аргументов")
            return
        name, lab = parts[1], parts[2]
        key = (name, lab)
        score = best_results[key]
        if score is None:
            print("Попыток не найдено")
        else:
            print(f"Лучший результат {name} по {lab}: {score}")
    elif command == "attempts":
        if len(parts) < 3:
            print("Неверное количество аргументов")
            return
        name, lab = parts[1], parts[2]
        key = (name, lab)
        count = attempts_count[key]
        if count is None:
            print("Попыток не найдено")
        else:
            print(f"Количество попыток {name} по {lab}: {count}")
    elif command == "completed":
        if len(parts) < 2:
            print("Неверное количество аргументов")
            return
        lab = parts[1]
        studs = students_per_lab[lab]
        if studs is None:
            print("Попыток не найдено")
        else:
            print(f"Студенты, сдававшие {lab}: {studs}")
    else:
        print("Неизвестная команда")
