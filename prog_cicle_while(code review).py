# ревью кода - 1
# Напишите программу, которая принимает на вход натуральное число и выводит произведение его цифр.
n = int(input())
product = 1

while n > 0:
    digit = n % 10
    product *= digit
    n //= 10
    
print(product)



# ревью кода - 2
# Напишите программу, которая принимает на вход натуральное число и выводит его первую (старшую) цифру.
n = int(input())

while n >= 10:
    n //= 10
    
print(n)



# ревью кода - 3
s = 0

for i in range(7):
    n = int(input())

    if n % 2 == 0:
        s = s + n

print(s)



# ревью кода - 4
count = 0
p = 1

for i in range(10):
    x = int(input())
    
    if x >= 0:
        p = p * x
        count = count + 1
        
if count > 0:
    print(count)
    print(p)
else:
    print('NO')



# ревью кода - 5
n = int(input())

if n == 0:
    print(0)
else:
    max_digit = -1
    
    while n > 0:
        digit = n % 10
        
        if digit % 3 == 0:

            if digit > max_digit:
                max_digit = digit
                
        n //= 10
    
    if max_digit == -1:
        print("NO")
    else:
        print(max_digit)



# ревью кода - 6  (Очень странные никнеймы)
nik_name = input()

while len(nik_name) < 10:

    if len(nik_name) % 4 == 0:
        nik_name += 'x'

    elif len(nik_name) % 5 == 0:
        nik_name += 'y'

    else:
        nik_name = 'z' + nik_name
        
nik_name = '@' + nik_name
print(nik_name)



# ревью кода - 7 (Цифровые сообщения)
longer_then_seven = 0
count_sms = 0

while True:
    num = int(input())
    
    count_sms += 1
    
    if len(str(num)) > 7:
        longer_then_seven += 1
    
    if num % 100 == 11:
        break

print(longer_then_seven, '/', count_sms, sep='')



# Ревью кода - 6
mx = -10**6 - 1
s = 0

for i in range(10):
    x = int(input())
    
    if x < 0:
        s += x
        
    if x < 0 and x > mx:
        mx = x

if mx == -10**6 - 1:
    print("NO")
else:
    print(s)
    print(mx)