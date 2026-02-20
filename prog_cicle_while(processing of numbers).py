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