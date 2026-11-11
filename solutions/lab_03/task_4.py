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

print('\n')
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

func("boris")
print('\n')

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