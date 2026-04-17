# ввывод имени и фамилии пользователя
name = input()
sur_name = input()

print(f"Hello {name} {sur_name}! You have just delved into Python")


# вывод длины названия футбольной команды
football_team = input()
print(f"Футбольная команда {football_team} имеет длину {len(football_team)} символов")



# Три города 
city1 = input()
city2 = input()
city3 = input()

shortest = min(city1, city2, city3, key=len)
longest = max(city1, city2, city3, key=len)

print(shortest)
print(longest)



# Арифметические строки
s1 = input()
s2 = input()
s3 = input()

a = len(s1)
b = len(s2)
c = len(s3)

lengths = sorted([a, b, c])

if lengths[1] - lengths[0] == lengths[2] - lengths[1]:
    print("YES")
else:
    print("NO")



# Цвет настроения синий
color = input()

if color in "синий":
    print("YES")
else:
    print("NO")



# Отдыхаем ли?
user_str = input()

if "суббота" in user_str or "воскресенье" in user_str:
    print("YES")
else:
    print("NO")



# Корректный email 
user_email = input()

if "@" in user_email and "." in user_email:
    print("YES")
else:
    print("NO")