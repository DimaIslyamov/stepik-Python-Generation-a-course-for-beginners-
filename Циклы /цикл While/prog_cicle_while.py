# До КОНЦА 1
some_text = input()

while "КОНЕЦ" not in some_text:
    print(some_text)
    some_text = input()



# До КОНЦА 2
some_text = input()

while some_text != "КОНЕЦ" and some_text != "конец":
    print(some_text)
    some_text = input()



# Количество членов
some_text = input()
stop_words = ["стоп", "хватит", "достаточно"]
counter = 0

while some_text not in stop_words:
    counter += 1
    some_text = input()

print(counter)



# Пока делимся
while True:
    num = int(input())
    if num % 7 != 0:
        break
    print(num)



# Сумма чисел
total = 0

while True:
    num = int(input())
    if num < 0:
        break
    total += num

print(total)



# Количество пятёрок 
count = 0

while True:
    num = int(input())
    if num <= 0 or num > 5:
        break
    elif num == 5:
        count += 1

print(count)



# Первый никнейм
while True:
    user_name = input()

    if "_" not in user_name:
        print(user_name)
        break
    


# Количество имён после Александры
found_alexandra = False
count = 0

while True:
    name = input()
    
    if name == "Александра":
        found_alexandra = True
        continue
    
    elif name == "Левон":
        break

    elif found_alexandra:
        count += 1


print(count)



# Ведьмаку заплатите чеканной монетой
price = int(input())
coins = [25, 10, 5, 1]

count = 0
i = 0

while price > 0:

    if coins[i] <= price:
        price -= coins[i]
        count += 1
    else:
        i += 1

print(count)



# Временной промежуток 
h1 = int(input())
m1 = int(input())
h2 = int(input())
m2 = int(input())

start = h1 * 60 + m1
end = h2 * 60 + m2

for minute in range(start, end + 1):
    h = minute // 60
    m = minute % 60
    print(f"{h:02}:{m:02}")

# Решение без перевода в минуты
h1 = int(input())
m1 = int(input())
h2 = int(input())
m2 = int(input())

while True:
    print(f"{h1:02}:{m1:02}")
    
    if h1 == h2 and m1 == m2:
        break
    
    m1 += 1
    
    if m1 == 60:
        m1 = 0
        h1 += 1





