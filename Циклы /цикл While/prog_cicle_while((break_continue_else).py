# Запомни навсегда
# У while есть 3 обязательные части:
#   1. начальное значение
#   2. условие продолжения
#   3. изменение переменной
# Если нет пункта 3 → бесконечный цикл.


# Наименьший делитель
n = int(input())

d = 2
while d * d <= n:
    if n % d == 0:
        print(d)
        break
    d += 1
else:
    print(n)



# Следуй правилам
n = int(input())
i = 1

while i <= n:
    
    if 5 <= i <=9 or 17 <= i <=37 or 78 <= i <= 87: # нижняя_граница <= переменная <= верхняя_граница
        i += 1
        continue

    print(i)
    i += 1



# Простое или составное
num = int(input())
flag = True

for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
        flag = False
        break

if num == 1:
    print('Число равно 1')
elif flag == True:
    print('Число простое')
else:
    print('Число составное')