# Площадь треугольника 📐
# Напишите программу, которая считывает длины двух катетов в прямоугольном треугольнике и выводит его площадь.
# Формула для вычисления площади треугольника: (1/2) * основание * высота

a = float(input())
b = float(input())

area = 0.5 * a * b
print(area)




# Две старушки 👵
# Две старушки идут навстречу друг другу с постоянными скоростями V1 и V2 км/ч.
# Определите, через какое время старушки встретятся, если расстояние между ними равно S км.

s = float(input())
v1 = float(input())
v2 = float(input())

time = s / (v1 + v2)
print(time)




# Обратное число 🙃
num = float(input())

if num != 0:
    reciprocal = 1 / num
    print(reciprocal)
else:
    print("Обратного числа не существует")




# 451 градус по Фаренгейту 🌡️
temp_far = float(input())
temp_cel = 5/9 * (temp_far - 32)
print(temp_cel)




# Dog age 🐶
dog_years = int(input())

if dog_years <= 2:
    human_years = dog_years * 10.5
else:
    human_years = 21 + (dog_years - 2) * 4

print(human_years)



# Первая цифра после точки
num = float(input())
first_decimal_digit = int((num * 10) % 10)
print(first_decimal_digit)



# Дробная часть
num = float(input())
fractional_part = num - int(num)
print(fractional_part)



# Наибольшее и наименьшее
vl_onem, vl_two, vl_three, vl_four, vl_five = int(input()), int(input()), int(input()), int(input()), int(input())

total_volume = vl_onem + vl_two + vl_three + vl_four + vl_five

print(f"Наименьшее число = {min(vl_onem, vl_two, vl_three, vl_four, vl_five)}")
print(f"Наибольшее число = {max(vl_onem, vl_two, vl_three, vl_four, vl_five)}")



# Абсолютная сумма
a1 = float(input())
a2 = float(input())
a3 = float(input())
a4 = float(input())
a5 = float(input())

result = abs(a1) + abs(a2) + abs(a3) + abs(a4) + abs(a5)
print(result)



# Интересное число 🤔
n = int(input())

a = n // 100
b = (n // 10) % 10
c = n % 10

mn = min(a, b, c)
mx = max(a, b, c)
mid = a + b + c - mn - mx

if mx - mn == mid:
    print("Число интересное")
else:
    print("Число неинтересное")



# Сортировка трёх чисел 🔢
a = int(input())
b = int(input())
c = int(input())

min_val = min(a, b, c)
max_val = max(a, b, c)
mid_val = a + b + c - min_val - max_val

print(min_val)
print(mid_val)
print(max_val)



# Манхэттенское расстояние 🗽
p1 = int(input())
p2 = int(input())
q1 = int(input())
q2 = int(input())

manhattan_distance = abs(p1 - q1) + abs(p2 - q2)

print(manhattan_distance)