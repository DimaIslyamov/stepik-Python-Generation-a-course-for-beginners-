# Площадь и длина
import math 

R = float(input())

S = math.pi * R ** 2
C = 2 * math.pi * R

print(S)
print(C)



# Пол и потолок
X = float(input())
specified_expression = math.floor(X) + math.ceil(X)
print(specified_expression)



# Евклидово расстояние
from math import sqrt

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

P = sqrt((x1 - x2)**2 + (y1 - y2)**2)

print(P)



# Тригонометрическое выражение
from math import radians, cos, sin, tan

X = float(input())
x_rad = radians(X)

value_of_a_trigonometric_expression = sin(x_rad) + cos(x_rad) + tan(x_rad)**2

print(value_of_a_trigonometric_expression)



# Правильный многоугольник
from math import pi, tan

n = int(input())
a = float(input())

S = (n * a ** 2) / (4 * tan(pi / n))

print(S)



# Средние значения
from math import sqrt

a = float(input())
b = float(input())

arithmetic_mean = (a + b) / 2
geometric_mean = sqrt(a * b)
harmonic_numbers = 2 * a * b / (a + b)
quadratic_numbers = sqrt((a**2 + b**2) / 2)

print(arithmetic_mean)
print(geometric_mean)
print(harmonic_numbers)
print(quadratic_numbers)



# Квадратное уравнение
import math

a = float(input())
b = float(input())
c = float(input())

D = b * b - 4 * a * c

if D < 0:
    print("Нет корней")
elif D == 0:
    x = -b / (2 * a)
    print(x)
else:
    sqrt_D = math.sqrt(D)
    x1 = (-b - sqrt_D) / (2 * a)
    x2 = (-b + sqrt_D) / (2 * a)
    print(min(x1, x2))
    print(max(x1, x2))