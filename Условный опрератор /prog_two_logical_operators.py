# Программа запрашивает у пользователя угол в градусах
# и определяет его тип: острый, прямой, тупой, развёрнутый, выпуклый или нулевой.
# Используются логические операторы для проверки условий

angle = int(input())

if angle % 90 == 0:
    if angle == 0:
        print('Нулевой')
    elif angle == 90:
        print('Прямой')
    elif angle == 180:
        print('Развёрнутый')
else:
    if 0 < angle < 90:
        print('Острый')
    elif 90 < angle < 180:
        print('Тупой')
    elif 180 < angle < 270:
        print('Выпуклый')
    else:
        print('Ни острый, ни тупой, ни выпуклый')



# ЭКЗАМЕН / ТЕСТ КОД /

# Начало столетия
year = int(input())

if year % 100 == 0:
    print("YES")
else:
    print("NO")



#  Шахматная доска
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if (x1 + y1) % 2 == (x2 + y2) % 2:
    print("YES")
else:
    print("NO")


# Girls only 👧
student_age = int(input())
student_gender = input()
if (student_age >= 10 and student_age <= 15) and (student_gender == 'f'):
    print('YES')
else:
    print('NO')


# Римские цифры до 10, если больше то "ошибка"
num = int(input())

if 1 <= num <= 10:
    if num == 1:
        print('I')
    elif num == 2:
        print('II')
    elif num == 3:
        print('III')
    elif num == 4:
        print('IV')
    elif num == 5:
        print('V')
    elif num == 6:
        print('VI')
    elif num == 7:
        print('VII')
    elif num == 8:
        print('VIII')
    elif num == 9:
        print('IX')
    elif num == 10:
        print('X')
else:
    print('ошибка')


# YES or NO – вот в чём вопрос ❓
num = int(input())
if num % 2 != 0:
    print("YES")
elif num % 2 == 0 and 2 <= num <= 5:
    print("NO")
elif num % 2 == 0 and 6 <= num <= 20:
    print("YES")
elif num % 2 == 0 and num > 20:
    print("NO")


# Ход слона
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if abs(x1 - x2) == abs(y1 - y2):
    print("YES")
else:
    print("NO")


# Ход коня 
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if (abs(x1 - x2) == 2 and abs(y1 - y2) == 1) or (abs(x1 - x2) == 1 and abs(y1 - y2) == 2):
    print("YES")
else:
    print("NO")


# Ход ферзя
x1 = int(input())
y1 = int(input())
x2 = int(input())   
y2 = int(input())

if (x1 == x2) or (y1 == y2) or (abs(x1 - x2) == abs(y1 - y2)):
    print("YES")
else:
    print("NO")