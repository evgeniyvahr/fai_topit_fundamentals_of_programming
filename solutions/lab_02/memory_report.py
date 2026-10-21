import sys
import tracemalloc


def object_sizes():
    results = []
    objects = [("Пустой список", []), ("Список из 10 чисел", list(range(10))), ("Кортеж из 10 чисел", tuple(range(10))),
               ("Строка из 10 символов", "0123456789"), ("Целое число", 67), ("Объект None", None)]
    for name, obj in objects:
        results.append({"Сценарий": name, "Количество элементов": len(obj) if hasattr(obj, "__len__") else 1,
                        "Размер объекта": sys.getsizeof(obj), "Текущий объём памяти": None,
                        "Пиковый объём памяти": None})
    return results


def list_growth():
    results = []
    a = []
    c = sys.getsizeof(a)
    results.append({"Сценарий": "Пустой список", "Количество элементов": 0, "Размер объекта": c,
                    "Текущий объём памяти": None, "Пиковый объём памяти": None})
    for i in range(1, 101):
        a.append(i)
        x = sys.getsizeof(a)
        if c != x:
            c = x
            results.append({"Сценарий": "Список после добавления", "Количество элементов": len(a), "Размер объекта": c,
                    "Текущий объём памяти": None, "Пиковый объём памяти": None})
    return results


def tracemalloc_scenario(name):
    tracemalloc.start()
    if name == "list(range(n))":
        obj = list(range(100000))
    else:
        obj = range(100000)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return {"Сценарий": name, "Количество элементов": 100000, "Размер объекта": sys.getsizeof(obj),
            "Текущий объём памяти": current, "Пиковый объём памяти": peak}


def tracemalloc_compare():
    scenario_list = tracemalloc_scenario("list(range(n))")
    scenario_range = tracemalloc_scenario("range(n)")
    return [scenario_list, scenario_range]


results1 = object_sizes()
results2 = list_growth()
results3 = tracemalloc_compare()

print("  ИТОГОВЫЙ ОТЧЁТ: ПОТРЕБЛЕНИЕ ПАМЯТИ В PYTHON\n")
print("\n  ЧАСТЬ 1. Размер отдельных объектов\n")
print(f"{'Объект':<40} {'Элементов':>10} {'Размер объекта':>12}\n")
for i in results1:
    print(f"{i["Сценарий"]:<40} {i["Количество элементов"]:>10} {i["Размер объекта"]:>12} Б")

print("\n  ЧАСТЬ 2. Рост списка при append()\n")
print(f"{'Момент':<40} {'Элементов':>6} {'Размер объекта':>15}\n")
for i in results2:
    print(f"{i["Сценарий"]:<40} {i["Количество элементов"]:>10} {i["Размер объекта"]:>12} Б")

print("\n  ЧАСТЬ 3. Измерение через tracemalloc\n")
print(f"{'Сценарий':<45} {'Элементов':>10} {'Размер объекта':>12} {'current':>12} {'peak':>12}\n")
for i in results3:
    print(f"{i["Сценарий"]:<45} {i["Количество элементов"]:>10} {i["Размер объекта"]:>12} "
          f"{i["Текущий объём памяти"]:>12} {i["Пиковый объём памяти"]:>12}")
print(f"Отношение пиковых объёмов: {results3[0]["Пиковый объём памяти"] / results3[1]["Пиковый объём памяти"]}")
