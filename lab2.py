# база 1
a = input()
a = '0'*(4 - len(a)) + a
if a[:2] == a[:1:-1]:
    print('base')
else:
    print('0')
    
# база 2
year = int(input("Введите год: "))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("Год високосный")
else:
    print("Не високосный")

# база 3
a = int(input('Введите число: '))

if 4 < a % 100 < 21 or a % 10 == 0 or 4 < a % 10 < 10:
    print(f'На лугу пасётся {a} коров')
else:
    if a % 10 == 1:
        print(f'На лугу пасётся {a} корова')
    if 1 < a % 10 < 5:
        print(f'На лугу пасётся {a} коровы')

# база 4
a = int(input('Введите число: '))
print('\nцикл for')
for i in range(2, int(num ** 0.5) + 1):
    if a % i == 0:
        print('Наименьший натуральный делитель: ', i)
        break
else:
    print(a)

print('\nцикл while')
i = 1
while i <= int(a**0.5) + 1:
    i += 1
    if a % i == 0:
        print('Наименьший натуральный делитель: ', i)
        break
else:
    print(a)
    
# база 5
a = int(input("Введите число: "))
maximum, minimum, proizv, summa, n, ch = temp, temp, 1, 0, 0, 0
while a != 0:
    summa += a
    n += 1
    proizv *= a
    if a % 2 == 0:
        ch += 1
    if a > maximum:
        maximum = temp
    if a < minimum:
        minimum = temp
    a = int(input("Введите число: "))
if n:
    print(f'1) Сумма = {summa}\n2) Произведение = {proizv}\n3) Среднее значение = {summa/n}\n4) Максимальное число = {maximum}\n5) Минимальное число = {minimum}\n6) Количество чётных чисед = {ch}, нечётных чисел = {n-ch}')
else:
    print(False)
    
# доп 1
a, b = int(input('Введите первое число: ')), int(input('Введите второе число: '))

print(f'Максимальное из двух чисел равно {int((a + b + abs(a - b)) / 2)}.')

# доп 2
k = int(input('Введите количество котлет: '))
min = int(input('Введите время приготовления одной стороны: '))
v = int(input('Вместимость сковороды: '))
if k < v:
    print(min * 2)
elif (k * 2) % v == 0:
    print(((k * 2) // v) * min)
else:
    print((((k * 2) // v) + 1) * min)

# доп 3
print('Загадайте число от Base до N')
right = int(input('Введите число N: '))
left = 1
question = ''
while question.title() != 'Угадал':
    mid = (right + left)//2
    print('Ваше число =', mid)
    question = input('Выберите утверждение: "Больше/Меньше/Угадал": ')
    if question.title() == 'Больше':
        left = mid
    elif question.title() == 'Меньше':
        right = mid
    if question.title() not in ['Больше', 'Меньше', 'Угадал']:
        question = input('Утверждение введено неверно - "Больше/Меньше/Угадал": ')
else:
    print('end')
