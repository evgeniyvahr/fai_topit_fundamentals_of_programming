import copy
# эксперимент A
# a = 10
# b = a
#
# print(a, b)
# print(id(a), id(b))
#
# a += 1
#
# print(a, b)
# print(id(a), id(b))

# эксперимент B
# first = [10, 20]
# second = first
#
# print(first, second)
# print(id(first), id(second))
#
# second.append(30)
#
# print(first, second)
# print(id(first), id(second))
# # дополнение 1
# second = [10, 20, 30]
#
# # дополнение 2
# print("first == second", first == second)
# print("first is second", first is second)
#
# # дополнение 3
# second.append(40)
# print("first == second", first == second)

# практическая задача
config1 = {
    "name": "Проект 1",
    "participants": ["Первый", "Второй"],
    "parameters": [{"mode": "обычный", "count": 3}, {"mode": "сложный", "count": 5}]
}
config2 = config1
print("Состояние до изменений: ")
print("config1", config1)
print("config2", config2)
config2["name"] = "Проект 4"
config2["parameters"][0]["mode"] = "средний"
print("Состояние после изменений: ")
print("config1", config1)
print("config2", config2)
print("Вывод: при простом присваивании конфигурации ссылаются на один объект в памяти")

config3 = copy.deepcopy(config1)
print("Состояние до изменений: ")
print("config1", config1)
print("config3", config3)
config3["name"] = "Проект 6"
config3["parameters"][1]["mode"] = "ультрасложный"
print("Состояние после изменений: ")
print("config1", config1)
print("config3", config3)
print("Вывод: при использовании copy.deepcopy() создаётся независимый объект")

# подтверждение независимости 1 и 3
assert config1 is not config3, "Это разные объекты"
assert config1["participants"] is not config3["participants"], "Списки участников независимы"
assert config1["parameters"] is not config3["parameters"], "Списки параметров независимы"
assert config1["parameters"][0] is not config3["parameters"][0], "Вложенные словари параметров независимы"
assert config1["parameters"][1] is not config3["parameters"][1], "Вложенные словари параметров независимы"

# подтверждение зависимости 1 и 2
assert config1 is config2, "config1 и config2 должны быть одним объектом"
assert config1["participants"] is config2["participants"], "Списки участников общие"
assert config1["parameters"] is config2["parameters"], "Списки параметров общие"

print("\nВсе проверки пройдены")

print("\nИтог:")
print("config1 и config2 - общие")
print("config1 и config3 - независимые")