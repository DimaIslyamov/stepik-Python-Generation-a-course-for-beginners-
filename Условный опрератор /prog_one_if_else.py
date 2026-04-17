# This program prompts the user to enter a password twice and checks if both entries match.
password_first_try = input("Enter your password: ")
password_second_try = input("Re-enter your password: ")

if password_first_try == password_second_try:
    print("Пароль принят")
else:
    print("Пароль не принят")



# This program checks if the entered number is even or odd.
user_value = int(input())

if user_value % 2 == 0:
    print("Четное")
else:
    print("Нечетное")



# This program checks if the user is old enough to access certain content.
user_age = int(input())

if user_age >= 18:
    print("Доступ разрешен")
else:
    print("Доступ запрещен")



# This program compares two numbers and prints the larger one.
value_one = int(input())
value_two = int(input())

if value_one > value_two:
    print(value_one)
else:
    print(value_two)



# Напишите программу, которая проверяет, что для заданного четырехзначного числа выполняется следующее соотношение: сумма первой и последней цифр равна разности второй и третьей цифр.
# Формат входных данных
# На вход программе подаётся одно целое положительное четырёхзначное число.
# Формат выходных данных
# Программа должна вывести «ДА» (без кавычек), если соотношение выполняется, или «НЕТ» (без кавычек) в противном случае.

four_digit_number = input()

a = int(four_digit_number[0])
b = int(four_digit_number[1])
c = int(four_digit_number[2])
d = int(four_digit_number[3])

if a + d == b - c:
    print("ДА")
else:
    print("НЕТ")



# Напишите программу, которая считывает три числа и подсчитывает сумму только положительных чисел.
# Формат входных данных
# На вход программе подаются три целых числа, каждое на отдельной строке.
# Формат выходных данных
# Программа должна вывести одно число – сумму положительных чисел.

num1 = int(input())
num2 = int(input())
num3 = int(input()) 

sum_positive = 0

if num1 > 0:
    sum_positive += num1
elif num2 > 0:
    sum_positive += num2
elif num3 > 0:
    sum_positive += num3

print(sum_positive) 


 
# Напишите программу, которая определяет возрастную категорию пользователя по введённому возрасту.
age_group = int(input())

if age_group <= 13:
    print("детство")
elif 14 <= age_group <= 24:
    print("молодость")
elif 25 <= age_group <= 59:
    print("зрелость")
else:
    print("старость")   
