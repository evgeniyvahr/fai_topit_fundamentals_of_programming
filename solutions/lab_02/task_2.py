import copy

original = [
    ["Python", 5],
    ["Algorithms", 4],
]

alias = original
shallow = original.copy()
deep = copy.deepcopy(original)

# изменение 1
# print("Изменение 1")
# original.append(["Databases", 5])
# print(f"original: {original}")
# print(f"alias: {alias}")
# print(f"shallow: {shallow}")
# print(f"deep: {deep}")
# print("\nИдентификаторы")
# print("Внешние списки:")
# print(f"id(original): {id(original)}")
# print(f"id(alias): {id(alias)}")
# print(f"id(shallow): {id(shallow)}")
# print(f"id(deep): {id(deep)}")
# print("Первые вложенные списки:")
# print(f"id(original[0]): {id(original[0])}")
# print(f"id(alias[0]): {id(alias[0])}")
# print(f"id(shallow[0]): {id(shallow[0])}")
# print(f"id(deep[0]): {id(deep[0])}")
# print("Объект, содержащий первую оценку:")
# print(f"id(original[0][1]): {id(original[0][1])}")
# print(f"id(alias[0][1]): {id(alias[0][1])}")
# print(f"id(shallow[0][1]): {id(shallow[0][1])}")
# print(f"id(deep[0][1]): {id(deep[0][1])}")

# изменение 2
# print("\nИзменение 2")
# original[0][1] = 3
# original.append(["Databases", 5])
# print(f"original: {original}")
# print(f"alias: {alias}")
# print(f"shallow: {shallow}")
# print(f"deep: {deep}")
# print("\nИдентификаторы")
# print("Внешние списки:")
# print(f"id(original): {id(original)}")
# print(f"id(alias): {id(alias)}")
# print(f"id(shallow): {id(shallow)}")
# print(f"id(deep): {id(deep)}")
# print("Первые вложенные списки:")
# print(f"id(original[0]): {id(original[0])}")
# print(f"id(alias[0]): {id(alias[0])}")
# print(f"id(shallow[0]): {id(shallow[0])}")
# print(f"id(deep[0]): {id(deep[0])}")
# print("Объект, содержащий первую оценку:")
# print(f"id(original[0][1]): {id(original[0][1])}")
# print(f"id(alias[0][1]): {id(alias[0][1])}")
# print(f"id(shallow[0][1]): {id(shallow[0][1])}")
# print(f"id(deep[0][1]): {id(deep[0][1])}")

# ошибочное создание матрицы
print("Ошибочное создание:")
wrong_matrix = [[0] * 3] * 3
print(f"Матрица до изменения: {wrong_matrix}")
wrong_matrix[0][0] = 1
print(f"Матрица после изменения: {wrong_matrix}")

# корректное создание матрицы
print("\nКорректное создание:")
correct_matrix = [[0] * 3 for _ in range(3)]
print(f"Матрица до изменения: {correct_matrix}")
correct_matrix[0][0] = 1
print(f"Матрица после изменения: {correct_matrix}")

