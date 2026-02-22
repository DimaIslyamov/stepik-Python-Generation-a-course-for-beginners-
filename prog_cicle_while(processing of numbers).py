# Обратный порядок 1
num = int(input())

while num != 0:
    last_digit = num % 10
    print(last_digit)
    num = num // 10    



# Обратный порядок 2
num = int(input())
while num != 0:
    last_digit = num % 10
    print(last_digit, end="")
    num = num // 10



# Макс и мин цифры
num = int(input())

min_digit = 9
max_digit = 0

while num > 0:
    digit = num % 10

    if digit > max_digit:
        max_digit = digit

    if digit < min_digit:
        min_digit = digit

    num = num // 10


print(f"Максимальная цифра равна {max_digit}")
print(f"Минимальная цифра равна {min_digit}")



# Все вместе
n = int(input())

original = n

sum_digits = 0
count = 0
product = 1
last_digit = n % 10

while n > 0:
    digit = n % 10
    sum_digits += digit
    product *= digit
    count += 1
    n //= 10

first_digit = original
while first_digit >= 10:
    first_digit //= 10

print(sum_digits)
print(count)
print(product)
print(sum_digits / count)
print(first_digit)
print(first_digit + last_digit)



# Вторая цифра
num = int(input())

while num >= 100:
    num //= 10

second_digit = num % 10

print(second_digit)



# Одинаковые цифры
num = int(input())

last_digit = num % 10
num //= 10

while num > 0:
    digit = num % 10

    if digit != last_digit:
        print("NO")
        break
    num //= 10
else:    
    print("YES")



# Цифры в порядке неубывания
n = int(input())

prev = n % 10
n //= 10

while n > 0:
    digit = n % 10
    
    if digit < prev:
        print("NO")
        break
        
    prev = digit
    n //= 10
else:
    print("YES")



# Количество четных цифр
n = input()

i = 0
count = 0

while i < len(n):
    digit = int(n[i])
    
    if digit % 2 == 0:
        count += 1
        print(f"{count}-я четная цифра равна {digit}")
    
    i += 1

if count == 0:
    print("Четных цифр в числе нет")