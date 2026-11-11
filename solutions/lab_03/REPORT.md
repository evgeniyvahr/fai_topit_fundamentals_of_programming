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


