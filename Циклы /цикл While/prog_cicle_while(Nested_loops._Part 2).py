# Делители-1
# На вход программе подаётся натуральное число n. 
# Напишите программу, выводящую графическое изображение делимости чисел от 1 до n включительно. 
# В каждой строке надо напечатать очередное число и столько символов +, сколько делителей у этого числа
n = int(input())

for i in range(1, n + 1):
    count = 0
    
    for j in range(1, i + 1):
        if i % j == 0:
            count += 1
    
    print(i, "+" * count, sep="")



# Численный треугольник 2
# Дано натуральное число n.
#  Напишите программу, которая печатает численный треугольник с высотой, равной n
n = int(input())

num = 1

for i in range(1, n + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()



# Простые числа
# На вход программе подается два натуральных числа a и b(a<b). Напишите программу, которая находит все простые числа от a до b включительно.
a = int(input())
b = int(input())

for x in range(a, b + 1):
    if x < 2:
        continue
    
    for y in range(2, int(x ** 0.5) + 1):
        if x % y == 0:
            break
    else:
        print(x)



# Сумма факториалов
# Дано натуральное число n. Напишите программу, которая выводит значение суммы 1! + 2! + 3! + ... + n!
n = int(input())

total = 0
factorial = 1

for i in range(1, n + 1):
    factorial *= i
    total += factorial

print(total)

# с вложенными циклам 
n = int(input())

total = 0

for i in range(1, n + 1):
    factorial = 1
    
    for j in range(1, i + 1):
        factorial *= j
    
    total += factorial

print(total)



# Подставь и узнаешь
#  На вход программе подаются натуральные числа n и m. 
# Под эмодзи 🍌, 💎, 🦌 спрятаны целые числа от 1 до n (не включительно)
n = int(input())
m = int(input())

found = False

for banana in range(1, n):
    for diamond in range(1, n):
        for camel in range(1, n):
            
            if banana + 3 * diamond + 2 * camel == m:
                print(f"{banana} + 3x{diamond} + 2x{camel} = {m}")
                found = True

if not found:
    print("При заданных n и m решений не существует.")



# Делители-2
# На вход программе подаются два натуральных числа a и b (a< b). 
# Напишите программу, которая находит натуральное число из отрезка [a;b] (от a до b включительно) с максимальной суммой делителей. 
# Если чисел с максимальной суммой делителей несколько, то искомым числом является наибольшее из них
a = int(input())
b = int(input())

count_sum = 0
max_count = 0

for i in range(a, b+1):
    count = 0

    for j in range(1, i+1):
        if i % j == 0:
            count += j

        if count >= count_sum:
            count_sum = count
            max_count = i

print(max_count, count_sum)



# Численный треугольник 3
# Дано натуральное число n. Напишите программу, которая печатает численный треугольник с высотой, равной n
n = int(input())

for i in range(1, n + 1):
    
    # возрастающая часть
    for j in range(1, i + 1):
        print(j, end="")
    
    # убывающая часть
    for j in range(i - 1, 0, -1):
        print(j, end="")
    
    print()



