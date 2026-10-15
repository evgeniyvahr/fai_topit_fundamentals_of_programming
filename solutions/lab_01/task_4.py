student = "Анна Смирнова"
course = "Основы программирования на Python"
completed = 7
total = 10
print(student[0], student[3])
print(student[0:4], student[5:])
print(student.upper(), student.lower())
print(student[0] + "." + student[5] + ".")
print(course[::-1])

x = 70
result1 = "%s - %s: %d/%d (%d%%)" % (student, course, completed, total, x)
result2 = "{} - {}: {}/{} ({}%)".format(student, course, completed, total, x)
result3 = f"{student} - {course}: {completed}/{total} ({x}%)"
print(result1)
print(result2)
print(result3)

symbol = "Я"
print(symbol)
print(ord(symbol))
print(chr(ord(symbol)))
print(symbol.encode("utf-8"))
print(len(symbol.encode("utf-8")))

# student[0] = "t"
