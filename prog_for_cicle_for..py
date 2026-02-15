# Популяция 🦠
m = int(input()) # стартовое количество организмов
p = int(input()) # среднесуточное увеличение в процентах
n = int(input()) # количество дней, в течение которых наблюдается рост популяции

population = float(m)

for day in range(1, n + 1):
    print(day, population)
    population *= (1 + p / 100)



# Таблица умножения
n = int(input())

for i in range(1, 10 + 1):
    print(f"{n} x {i} = {n * i}")
    


# Последовательность чисел 2
m = int(input())
n = int(input())

for i in range(m, n + 1):
    if i % 17 == 0:     # кратные 17
        print(i)
    elif i % 10 == 9:   # заканчивающиеся на 9
        print(i)
    elif i % 3 == 0 and i % 5 == 0:     # кратные 3 и 5
        print(i)



# Последовательность чисел 3
m = int(input())
n = int(input())

for i in range(m, n -1, -1):
    if i % 2 != 0:
        print(i)



# Последовательность чисел 4
m = int(input())
n = int(input())

if m <= n:
    for i in range(m, n + 1):
        print(i)
else:
    for i in range(m, n - 1, -1):
        print(i)



#### ЧАСТЫЕ СЦЕНАРИИ ####
# Количество чисел
a = int(input())
b = int(input())

counter = 0

for i in range(a, b + 1):
    cube = i**3

    if cube % 10 == 4 or cube % 10 == 9:
        counter += 1


print(counter)



# Сумма чисел
n = int(input())

total = 0

for i in range(n):
    number = int(input())
    total += number

print(total)



# Асимптотическое приближение 
from math import log

n = int(input())
total = 0

for i in range(1, n + 1):
    total += 1 / i

result = total - log(n)

print(result)



# Сумма чисел 2
n = int(input())
total = 0

for i in range(1, n + 1):
    square = i**2
    last_digit = square % 10

    if last_digit in [2, 5, 8]:
        total += i


print(total)



# Факториал
n = int(input())

factorial = 1

for i in range(1, n + 1):
    factorial *= i

print(factorial)



# Без нулей 
total = 1

for i in range(10):
    number = int(input())
    if number != 0:
        total *= number

print(total)



# Сумма делителей
n = int(input())
total = 0

for i in range(1, n + 1):
    if n % i == 0:
        total += i

print(total)



# Only even numbers
# Способ 1 — через флаг (самый понятный)
for i in range(10):
    number = int(input())
    if number % 2 != 0:
        print("NO")
        break
else:
    print("YES")

# Способ 2 — через ранний выход (более “питоновский”)
for i in range(10):
    number = int(input())
    if number % 2 != 0:
        print("NO")
        break
else:
    print("YES")



# Знакочередующаяся сумма
n = int(input())
total = 0

for i in range(1, n + 1):
    if i % 2 != 0:
        total += i
    else:
        total -= i

print(total)



# Наибольшие числа 
n = int(input())

first = int(input())
second = int(input())

if first > second:
    max1 = first
    max2 = second
else:
    max1 = second
    max2 = first

for i in range(n - 2):
    number = int(input())

    if number > max1:
        max2 = max1
        max1 = number
    elif number > max2:
        max2 = number

print(max1)
print(max2)



# Последовательность Фибоначчи
n = int(input())

a = 1
b = 1

if n == 1:
    print(1)
else:
    print(a, b, end=" ")

    for i in range(3, n + 1):
        c = a + b
        print(c, end=" ")
        a = b
        b = c


