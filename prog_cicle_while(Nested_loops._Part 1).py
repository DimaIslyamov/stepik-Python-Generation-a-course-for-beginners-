# Таблица - 1
# Напишите программу, которая принимает на вход натуральное число n и выводит таблицу из n строк и 3 столбцов, заполненную числом n.
n = int(input())

for i in range(n):
    for j in range(3):
        print(n, end=' ')

    print()



# Таблица - 2
# Напишите программу, которая принимает на вход натуральное число n и выводит таблицу из n строк и 5 столбцов, заполненную числами от 1 до n.
n = int(input())

for i in range(n):
    for j in range(5):
        print(i + 1, end=' ')

    print()



# Таблица - 3
# Напишите программу, которая принимает на вход натуральное число n и выводит таблицу сложения от 1 до n.
n = int(input())

for i in range(1, n + 1):
    for j in range(1, 10):
        print(f"{i} + {j} = {i + j}")
    print()



# Таблица - 4
n = int(input())

for i in range(1, n + 1):
    for j in range(i):
        print(i, end='')
    print()



# Звёздный треугольник
# Дано нечётное натуральное число n. Напишите программу, которая печатает равнобедренный звёздный треугольник с основанием, равным n.
n = int(input())

peak = n // 2 + 1

# рост
for i in range(1, peak + 1):
    for j in range(i):
        print('*', end='')
    print()

# спад
for i in range(peak - 1, 0, -1):
    for j in range(i):
        print('*', end='')
    print()

# Более компактный вариант
n = int(input())

peak = n // 2 + 1

for i in range(1, n + 1):
    if i <= peak:
        stars = i
    else:
        stars = n - i + 1
    
    for j in range(stars):
        print('*', end='')
    print()
