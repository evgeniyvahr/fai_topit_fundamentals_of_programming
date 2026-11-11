# Цель работы
   Научиться переводить условие задачи в алгоритм, выбирать подходящую структуру данных и разделять программу на небольшие функции с понятными контрактами.

# Задание 1
## Таблица тестовых сценариев

| №  | score | work_type | absences | Ожидаемый уровень | Фактический уровень |
|----|-------|-----------|----------|-------------------|---------------------|
| 1  | 0     | exam      | 0        | недостаточный     | недостаточный       |
| 2  | 59    | exam      | 0        | недостаточный     | недостаточный       |
| 3  | 60    | project   | 2        | удовлетворительный| удовлетворительный  |
| 4  | 74    | practice  | 3        | удовлетворительный| удовлетворительный  |
| 5  | 75    | exam      | 0        | хороший           | хороший             |
| 6  | 89    | project   | 1        | хороший           | хороший             |
| 7  | 90    | practice  | 0        | отличный          | отличный            |
| 8  | 100   | exam      | 1        | отличный          | отличный            |
| 9  | 65    | practice  | 4        | недостаточный     | недостаточный       |
| 10 | -5    | exam      | 0        | Ошибка            | Ошибка              |

### Порядок проверки условий

1. Сначала проверяются диапазоны `score` (0–100) и `absences` (0–5). Если хотя бы одно значение выходит за рамки — выводится сообщение об ошибке и дальнейшая классификация **не выполняется**.
2. Затем определяется уровень по результату.
3. После этого, если `absences > 3`, уровень снижается на одну ступень (но не ниже «недостаточный»).
4. В конце через формируется пояснение типа работы.

### Недостижимые ветви

При выбранном порядке проверки (`score >= 90`, затем `>= 75`, затем `>= 60`, иначе `недостаточный`) все ветви достижимы, так как диапазоны покрывают всё множество [0, 100] без пропусков и перекрытий.

В блоке `match / case` ветка `case _` (неизвестный тип работы) недостижима при вводе только корректных значений `exam`, `project`, `practice`, но она предусмотрена на случай некорректного ввода типа работы.

### Практическое расширение
<img width="1033" height="443" alt="image" src="https://github.com/user-attachments/assets/596fd875-7d14-4bf9-a240-70722466ce66" />



# Задание 2

| Операция | Временная сложность |
|---|---------------------|
| Вычисление суммы | O(n)                |
| Поиск минимального значения | O(n)                |
| Поиск максимального значения | O(n)                |
| Подсчёт чётных значений | O(n)                |
| Подсчёт значений > среднего (2-й проход) | O(n)                |
| Бинарный поиск | O(log n)            |

Число операций всегда зависит от длины массива. 

Необходимая доп память: для переменных, в которых сохраняется результат.

Проверка делителей до квадратного корня корректна, потому что если число не делится на некое число `n`, то число не будет делиться и на `x / n`. Соответственно при проверке всех делителей до корня мы также проверяем все делители больше корня.

## Практическое расширение
<img width="285" height="255" alt="image" src="https://github.com/user-attachments/assets/040099d6-2fcc-4fad-8a9c-c1d0eb3ee63f" />  



<img width="429" height="799" alt="image" src="https://github.com/user-attachments/assets/501f1d93-0f31-4b4f-9f49-42cbf8799954" />



#### Сравнительная таблица
| Размер массива | Сравнений при линейном поиске | Сравнений при бинарном поиске |
|---|---|---|
| 10 | 10 | 4 |
| 100 | 38 | 6 |
| 1000 | 711 | 10 |


# Задание 3
 - Множество подходит для хранения уникальных значений, потому что set автоматически отбрасывает дубликаты при добавлении
 - Кортеж можно использовать, как ключ словаря, потому что кортеж - неизменяемый тип данных, что и требуется для возможности быть ключом
 - Список нельзя использовать как ключ словаря потому что список - изменяемый
 - Словарь предпочтительнее списка для частого поиска результата по составному ключу, потому что словарь ищет за O(1), а список за O(n)

### Построения
<img width="394" height="837" alt="image" src="https://github.com/user-attachments/assets/cf405237-425f-45f0-b9e6-e3f97097523c" />


### Добавление записи:
<img width="644" height="509" alt="image" src="https://github.com/user-attachments/assets/864b5d00-b2f6-4004-8bc0-9d0de5026816" />


### Оценка средней сложности операций для использованных коллекций

| Коллекция | Операция | Средняя сложность |
|---|---|---|
| **set** | Добавление элемента (`add`) | O(1) |
| **set** | Поиск элемента (`in`) | O(1) |
| **dict** | Добавление/обновление ключа | O(1) |
| **dict** | Поиск по ключу (`get`) | O(1) |
| **list** | Добавление в конец (`append`) | O(1) |
| **list** | Добавление в начало/середину (`insert`) | O(n) |
| **list** | Поиск элемента (`in`, `index`) | O(n) |
| **tuple** | Поиск элемента (`in`) | O(n) |
| **tuple** | Добавление элемента | — |

### Практическое расширение
<img width="672" height="803" alt="image" src="https://github.com/user-attachments/assets/96ffca51-d9ba-4b99-9767-899a7efbd72a" />
<img width="586" height="579" alt="image" src="https://github.com/user-attachments/assets/f9a6a9b9-4efd-426d-9a41-fe6fc8a2625c" />

# Задание 4
```python
def arithmetic_mean(values: list[float]) -> float:
    if not values:
        return 0.0
    return sum(values) / len(values)


def normalize_name(name: str) -> str:
    if not name:
        return ""
    parts = name.strip().split()
    normalized_parts = [part.capitalize() for part in parts]
    return " ".join(normalized_parts)


def build_report(
    student: str,
    results: list[int],
    *,
    precision: int = 2,
    prefix: str = "Результат",
) -> str:
    if not results:
        return f"{prefix}: отсутствуют результаты студента {student}"
    mean = arithmetic_mean([float(r) for r in results])
    mean_rounded = round(mean, precision)
    return (
        f"{prefix} студента {student}: "
        f"результаты = {results}, "
        f"среднее = {mean_rounded}"
    )


def collect_tags(*tags: str, lowercase: bool = True) -> tuple[str, ...]:
    cleaned = []
    seen = set()
    for tag in tags:
        if not tag or not tag.strip():
            continue
        processed = tag.strip()
        if lowercase:
            processed = processed.lower()
        if processed not in seen:
            seen.add(processed)
            cleaned.append(processed)
    return tuple(cleaned)


# assert проверки функции arithmetic_mean
assert arithmetic_mean([1.0, 2.0, 3.0, 4.0]) == 2.5, "Среднее равно 2.5"
assert arithmetic_mean([37.234]) == 37.234, "Среднее равно 37.234"
assert arithmetic_mean([]) == 0.0, "Список пуст"

# assert проверки функции normalize_name
assert normalize_name("anna") == "Anna", "Верно Anna"
assert normalize_name("    evgenIY   vahranev  ") == "Evgeniy Vahranev", "Верно Evgeniy Vahranev"
assert normalize_name("") == "", "Верно пустая строка"

# assert проверки функции build_report
assert build_report("anna", [3, 4, 5]) == ("Результат студента anna: результаты = [3, 4, 5], "
                                           "среднее = 4.0"), "Ошибка"
assert build_report("dmitriy", [6, 7, 8], prefix="Оценка") == ("Оценка студента dmitriy: "
                                                               "результаты = [6, 7, 8], среднее = 7.0"), "Ошибка"
assert build_report("boris", []) == "Результат: отсутствуют результаты студента boris", "Ошибка"

# assert проверки функции collect_tags
assert collect_tags("java", "", "  ", "java", "c++") == ("java", "c++"), "Ошибка"
assert collect_tags("  hello  ", "HELLO") == ("hello",), "Ошибка"
assert collect_tags() == (), "Ошибка"


# Вызовы функций с позиционными и именованными аргументами
print(f"arithmetic_mean([10.0, 20.0, 30.0]) = {arithmetic_mean([10.0, 20.0, 30.0])}") # позиционные аргументы
print(f"normalize_name('  anna   ivanova  ') = '{normalize_name('  anna   ivanova  ')}'") # позиционный аргумент
print(f"build_report('dmitriy, [6, 7, 8], prefix='Оценка') = {build_report("dmitriy", 
                                        [6, 7, 8], prefix="Оценка")}") # позиционные и именованный аргументы
print(f"collect_tags('A', 'B', lowercase=False) = {collect_tags('A', 'B', lowercase=False)}")

print('\n')

# распаковка списка и словаря
tags_list = ["python", "java", "python", "c++"]
print(f"tags_list = {tags_list}")
print(f"collect_tags(*tags_list) = {collect_tags(*tags_list)}")

parameters = {"precision": 1, "prefix": "Итог"}
print(f"parameters = {parameters}")
print(f"build_report('boris', [4, 5], **parameters) = '{build_report('boris', [4, 5], **parameters)}'")
```

### Исследования LEGB
```python
# исследование LEGB
course = "Fundamentals of programming"
def func(name):
    grade = "unknown"
    def in_func(new_grade):
        nonlocal grade
        grade = new_grade
        print(f"[in_func] Курс: {course}")
        print(f"[in_func] Студент: {name}")
        print(f"[in_func] Оценка: {grade}")
    print(f"[func] grade={grade}")
    in_func("good")
    print(f"[in_func] grade={grade}")
    return grade
```
#### Схема областей видимости
- **B** Built-in: `len`, `print`, `range`, `int`, ...
  - **G** Global: `course = "Fundamentals of Programming"`
    - **E** Enclosing (`func`): `name`, `grade`
      - **L** Local (`in_func`): `new_grade`

### Ошибка изменяемого значения по умолчанию
```python
# ошибка изменяемого значения по умолчанию
def add_result(value, results=[]):
    results.append(value)
    return results


print(add_result(1))
print(add_result(2))
print(add_result(3))


def new_add_result(value, results=None):
    if results is None:
        results = []
    results.append(value)
    return results


print(new_add_result(1))
print(new_add_result(2))
print(new_add_result(3))
```
Значение по умолчанию results=[] вычисляется только 1 раз в момент определения функции, поэтому при каждом последующем вызове используется один и тот же объект списка

### Практическое расширение
```python
# практическое расширение
def apply_to_results(operation, values):
    return [operation(x) for x in values]


def make_threshold_checker(threshold):
    def checker(value):
        return value > threshold
    return checker


results = [1, 5, 2, 3, 1, 4, 2, 3]


def cube(x):
    return x ** 3


cubed = apply_to_results(cube, results)
print(f"\napply_to_results(cube, results) = {cubed}")
arr = apply_to_results(lambda x: x * 3, results)
print(f"\napply_to_results(lambda x: x * 3, results) = {arr}")
check_3 = make_threshold_checker(3)
check_4 = make_threshold_checker(4)
print(f"\nmake_threshold_checker(3): \n check_3(5) = {check_3(5)}")
print(f"make_threshold_checker(4): \n check_4(3) = {check_4(3)}")
print(f"\napply_to_results(check_3, results): {apply_to_results(check_3, results)}")
print(f"apply_to_results(check_4, results): {apply_to_results(check_4, results)}")
```

В замыкании сохраняется ссылка на `thresholsd` из функции `make_threshold_checker`. Значение `threshold` замораживается в момент создания `checker`

# Задание 5
```python
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
```

### Декомпозиция программы
| Функции | Назначение |
|---|---|
| `mean`, `minimum`, `maximum` | Работа с одним списком чисел |
| `classify` | Работа с одним числом |
| `student_summary` | Работа с одним студентом |
| `group_summary`, `find_top_students` | Работа со всей группой студентов |
| `format_report` | Формирование отчёта |

Зависимости:
- `student_summary` использует `mean`, `minimum`, `maximum`, `classify`
- `group_summary` использует `student_summary`, `mean`, `maximum`, `find_top_students`
- `find_top_students` использует `mean`, `maximum`
- `format_report` использует данные из `student_summary` и `group_summary`

### Оценка сложности построения общей статистики
Пусть n - количество студентов, m - количество результатов для студента

| Операция                                  | Сложность | Пояснение |
|-------------------------------------------|-----------|---|
| Вычисление статистики по каждому студенту | O(n * m)  | Для каждого студента проходим по его результатам |
| Подсчёт категорий                         | O(n)      | Один проход по списку студентов |
| Поиск лидеров                             | O(n)      | Один проход по словарю средних |
| Форматирование отчёта                     | O(n × m)  | Вывод результатов каждого студента |
| Итого                                     |  O(n × m) |  Линейно по общему количеству результатов |

