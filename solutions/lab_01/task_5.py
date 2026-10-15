# Программа по введённым данным вычисляет результаты и выводит на экран

name = input("Имя исследователя: ")
exp = input("Название эксперимента: ")
runs = int(input("Количество запусков: "))
dur = float(input("Длительность запуска: "))
real = float(input("Действительная часть коэффициента: "))
imag = float(input("Мнимая часть коэффициента: "))

time_s = runs * dur
time_m = time_s / 60
comp = complex(real, imag)
sq = real ** 2 + imag ** 2
has_runs = bool(runs)

print("\n========================================")
print("ЭКСПЕРИМЕНТ:", exp)
print("Исследователь:", name)
print("Запуски:", runs)
print(f"Общее время: {time_s:.2f} с ({time_m:.2f} мин)")
print("Коэффициент:", comp)
print(f"Квадрат модуля: {sq:.2f}")
print("Есть выполненные запуски:", has_runs)
print("========================================")

print("\nstr, str, int, float, float, float")
