import gc

# first = []
# second = []
#
# first.append(second)
# second.append(first)
#
# print("first ссылается на second:", first[0] is second)
# print("second ссылается на first:", second[0] is first)
#
# print(f"\nСостояние сборщика мусора: {'включён' if gc.isenabled() else 'отключён'}")
# print(f"Пороги поколений: {gc.get_threshold()}")
# print(f"Статистика поколений до удаления: {gc.get_count()}")
# id_1 = id(first)
# id_2 = id(second)
# del first
# del second
# print(f"Статистика поколений после удаления: {gc.get_count()}")
# c = gc.collect()
# print(f"Статистика поколений после сбора мусора: {gc.get_count()}")
# print(f"Собрано объектов: {c}")

# дополнительный эксперимент
# gc.disable()
# one = []
# two = []
# one.append(two)
# two.append(one)
#
# three = []
# four = []
# three.append(four)
# four.append(three)
#
# five = []
# six = []
# five.append(six)
# six.append(five)
# del one
# del two
# del three
# del four
# del five
# del six
# print(f"Статистика поколений после удаления: {gc.get_count()}")
# c = gc.collect()
# print(f"Статистика поколений после сбора мусора: {gc.get_count()}")
# print(f"Собрано объектов: {c}")
# gc.enable()

# практическая задача
a = {"name": "a", "neighbors": []}
b = {"name": "b", "neighbors": []}
c = {"name": "c", "neighbors": []}
d = {"name": "d", "neighbors": []}

a["neighbors"].append(b)
b["neighbors"].append(c)
c["neighbors"].append(a)

count1 = gc.collect()
first = gc.get_count()

for i in [a, b, c, d]:
    neighbors = [j["name"] for j in i["neighbors"]]
    print(f"  {i['name']}: соседи - {neighbors}")

del a
del b
del c
count2 = gc.collect()
second = gc.get_count()
print(f"\nd доступен: {d is not None}")

print(f"\nСтатистика до: {first}")
print(f"Собрано до: {count1}")
print(f"\nСтатистика после: {second}")
print(f"Собрано после: {count2}")

