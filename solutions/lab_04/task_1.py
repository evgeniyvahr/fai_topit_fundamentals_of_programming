values = [10, 20, 30]
iterator = iter(values)

print(iterator is values)
print(iter(iterator) is iterator)
print(next(iterator))
print(next(iterator))
print(next(iterator))
# print(next(iterator))


def consume(iterable) -> list:
    result = []
    it = iter(iterable)
    while True:
        try:
            result.append(next(it))
        except StopIteration:
            break
    return result


def my_enumerate(iterable, start=0):
    it = iter(iterable)
    index = start
    while True:
        try:
            value = next(it)
        except StopIteration:
            return
        yield index, value
        index += 1


def my_zip(first, second):
    it1 = iter(first)
    it2 = iter(second)
    while True:
        try:
            a = next(it1)
        except StopIteration:
            return
        try:
            b = next(it2)
        except StopIteration:
            return
        yield a, b


'''генератор для проверки'''


def squares(n: int):
    i = 0
    while i < n:
        yield i * i
        i += 1


if __name__ == "__main__":
    print("=== Проверка функции consume() ===")
    print(f"consume([10, 20, 30]) -> {consume([10, 20, 30])}")
    print(f"consume((10, 20, 30)) -> {consume((10, 20, 30))}")
    print(f"consume('hello') -> {consume('hello')}")
    print(f"consume(range(5)) -> {consume(range(5))}")
    print("\nЧастично использованный итератор:")
    it = iter([10, 20, 30, 40])
    print(f"next(it) -> {next(it)}")
    print(f"next(it) -> {next(it)}")
    print(f"consume(it) -> {consume(it)}")

    print(f"\n=== Повторный обход списка vs итератор ===")
    arr = [10, 20, 30]
    print("Список:")
    print(f"1-й проход: {consume(arr)}")
    print(f"2-й проход: {consume(arr)}")
    it = iter(arr)
    print("Итератор:")
    print(f"1-й проход: {consume(it)}")
    print(f"2-й проход: {consume(it)}")

    print(f"\n=== my_enumerate ===")
    print(f"Список: {consume(my_enumerate([10, 20, 30]))}")
    print(f"Строка: {consume(my_enumerate('hello', start=1))}")
    print(f"Генератор: {consume(my_enumerate(squares(4)))}")

    print("\n=== my_zip ===")
    print(f"Список + список: {consume(my_zip([10, 20, 30], [40, 50]))}")
    print(f"Строка + список: {consume(my_zip('hello', [10, 20, 30]))}")
    print(f"Генератор + range: {consume(my_zip(squares(4), range(3)))}")

    from task_2 import StepRange
    print("\n=== Проверка на StepRange ===")
    sr = StepRange(0, 10, 2)
    print(f"StepRange(0, 10, 2) -> {consume(sr)}")
    print(f"my_enumerate(StepRange) -> {consume(my_enumerate(sr))}")
    print(f"my_zip(StepRange, 'hello') -> {consume(my_zip(sr, 'hello'))}")
    print(f"my_zip(StepRange, squares(3)) -> {consume(my_zip(sr, squares(3)))}")
