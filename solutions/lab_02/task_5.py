import sys
import tracemalloc

# часть 1
# empty_list = []
# list_of_ten = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# cortege = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# string_of_ten = "1234567890"
# number = 67
# none_object = None
# print(f"Пустой список: {sys.getsizeof(empty_list)} байт")
# print(f"Список из десяти элементов: {sys.getsizeof(list_of_ten)} байт")
# print(f"Кортеж из десяти элементов: {sys.getsizeof(cortege)} байт")
# print(f"Строка из десяти символов: {sys.getsizeof(string_of_ten)} байт")
# print(f"Целое число: {sys.getsizeof(number)} байт")
# print(f"Объект None: {sys.getsizeof(none_object)} байт")

# часть 2
# a = []
# c = sys.getsizeof(a)
# for i in range(1, 101):
#     a.append(i)
#     x = sys.getsizeof(a)
#     if x != c:
#         c = x
#         print(f"Длина: {len(a)}")
#         print(f"Размер: {c} байт")

# часть 3
print("Вариант 1:")
tracemalloc.start()

numbers = list(range(100_000))
current, peak = tracemalloc.get_traced_memory()

tracemalloc.stop()
print(f"Текущая память: {current / 1024:.2f} КБ")
print(f"Пиковая память: {peak / 1024:.2f} КБ")

print("\nВариант 2")
tracemalloc.start()

numbers = range(100_000)
current, peak = tracemalloc.get_traced_memory()

tracemalloc.stop()
print(f"Текущая память: {current / 1024:.2f} КБ")
print(f"Пиковая память: {peak / 1024:.2f} КБ")
