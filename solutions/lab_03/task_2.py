def linear_search(a, x):
    i = -1
    count = 0
    for j in range(len(a)):
        count += 1
        if a[j] == x:
            i = j
            break
    return i, count

def is_prime(x):
    if x == 1:
        return False
    if x == 2:
        return True
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
    return True


def selection_sort(a):
  n = len(a)
  for i in range(n - 1):
    imin = i
    for j in range(i + 1, n):
      if a[j] < a[imin]:
        imin = j
    if imin != i:
      a[i], a[imin] = a[imin], a[i]
  return a


def binary_search(a, x):
    l = 0
    r = len(a)
    count = 0
    while r - l > 1:
        count += 1
        m = (r + l) // 2
        if a[m] <= x:
            l = m
        else:
            r = m
    if a[l] == x:
        return l, count
    else:
        return -1, count


measurements = [12, 15, 11, 18, 18, 9, 21, 15, 7, 18]
sum = 0
mn = 100
mx = 0
even = 0
count = 0
for i in measurements:
    sum += i
    if i < mn:
        mn = i
    if i > mx:
        mx = i
    if i % 2 == 0:
        even += 1

average = sum / 10
for i in measurements:
    if i > average:
        count += 1

a1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a2 = [i for i in range(1, 101)]
a3 = [i for i in range(1, 1001)]
x1 = 10
x2 = 38
x3 = 711
print(f"Линейный поиск в массиве из 10 элементов: {linear_search(a1, x1)}")
print(f"Бинарный поиск в массиве из 10 элементов: {binary_search(a1, x1)}")
print(f"Линейный поиск в массиве из 100 элементов: {linear_search(a2, x2)}")
print(f"Бинарный поиск в массиве из 100 элементов: {binary_search(a2, x2)}")
print(f"Линейный поиск в массиве из 1000 элементов: {linear_search(a3, x3)}")
print(f"Бинарный поиск в массиве из 1000 элементов: {binary_search(a3, x3)}")
