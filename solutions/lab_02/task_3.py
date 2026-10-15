import sys
import weakref

# изменение счётчика ссылок
# data = [1, 2, 3]
# print("После создания:", sys.getrefcount(data))
#
# alias = data
# print("После создания alias:", sys.getrefcount(data))
#
# container = [data]
# print("После помещения в контейнер:", sys.getrefcount(data))
#
# del alias
# print("После del alias:", sys.getrefcount(data))
#
# container.clear()
# print("После очистки контейнера:", sys.getrefcount(data))

# слабые ссылки
#
# class Record:
#     pass
#
#
# record = Record()
# weak_record = weakref.ref(record)
#
# print(weak_record())
# del record
# print(weak_record())

# практическая задача


class Record:
    pass


registry = weakref.WeakValueDictionary()
r1 = Record()
r2 = Record()
r3 = Record()
registry[0] = r1
registry[1] = r2
registry[2] = r3
print("Удаление первой сильной ссылки")
del r3
print(list(registry))
print(f"r1: {0 in registry}")
print(f"r2: {1 in registry}")
print(f"r3: {2 in registry}")

print("\nУдаление второй сильной ссылки")
del r1
print(list(registry))
print(f"r1: {0 in registry}")
print(f"r2: {1 in registry}")
print(f"r3: {2 in registry}")