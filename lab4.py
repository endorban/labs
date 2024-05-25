# база 1
def Check(x1, x2):
    try:
        return int(x1) + int(x2)
    except:
        return str(x1) + str(x2)
print(Check(input('Введите первое значение: '), input('Введите второе значение: ')))

# база 2
from math import ceil
n = int(input())
def Tort(n):
    razr = 0
    while n > 1:
        n = ceil(n / 2)
        razr += 1
    return razr

print(f'Что бы каждому досталось по куску: {Tort(n)}')
print(f'Что бы минимум половине досталось по 2 куска: {Tort(n + ceil(n/2))}')
print(f'Каждому по куску и осталось минимум 10: {Tort(n+10)}')

# база 3
def fibonachi(n):
    a, b = 0, 1
    for i in range(1, n):
        a, b = b, a+b
    return b

def formulaFib(n):
    sqrt_5 = 5 ** 0.5
    return ((((1 + sqrt_5) / 2) ** n - ((1 - sqrt_5) / 2) ** n) / sqrt_5)

i = 0
while True:
    i += 1
    if abs(formulaFib(i) - fibonachi(i)) > 0.001:
        print('Отличие более чем на 0.001 начинается с n =', i)
        print('При этом отличие составляет:', formulaFib(i) - fibonachi(i))
        break
      
# база 4
n = int(input('Введите число игроков: '))
m = int(input('Введите количество кубиков: '))
def game(n, m):
    now_n = 1
    now_m = 1
    while True:
        if m >= 0 and (m - now_m) > 0:
            m -= now_m
        else:
            print('Проиграл игрок номер', now_n)
            break
        if now_m * 2 < 25:
            now_m *= 2
        else:
            now_m = (now_m * 2) - 25
        now_n = (now_n % n) + 1


game(n, m)

# база 5
n = int(input('Введите количество дисков: '))                             

# рекурсия
def tower(n, start, finish, temp):
    if n > 0:
        tower(n-1, start, temp, finish)
        print("Диск ", n, " : ", start, " =====> ", finish)
        tower(n-1, temp, finish, start)

tower(n, '1', '3', '2')


# цикл

a = []
def f(k, n):
    if n % 2 == 0 and k % 2 == 0 or n % 2 != 0 and k % 2 != 0:
        x, y, z = 1, 2, 3
    else:
        x, y, z = 1, 3, 2

    for i in range(2**k - 1, 2**n - 1, 2**(k + 1)):
        a[i].append(k + 1)
        a[i].append(x)
        a[i].append(y)
        x, y, z = y, z, x

for i in range(2**n - 1):
    a.append([])

for i in range(n):
    f(i, n)

for i in range(len(a)):
    print('Диск ', a[i][0], ' : ' , a[i][1], ' =====> ', a[i][2])

# доп 1
def convert_base_R(num, to_base=10, from_base=10):
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if isinstance(num, str):
        n = int(num, from_base)
    else:
        n = int(num)
    if n < to_base:
        return alphabet[n]
    else:
        return convert_base_R(n // to_base, to_base) + alphabet[n % to_base]
try:
    print('Выберите операцию:\n1) сложение\n2) умножение\n3) вычитание\n4) деление (только целочисленное)\nВаш выбор: ', end = '')
    task = int(input())
    a, b = input('Введите два числа в произвольных ' +
                 'системах счисления через пробел: ').split()
    a_base, b_base = map(int, input('Введите системы счисления ' +
                                    'чисел через пробел: ').split())
    a_10 = int(convert_base_R(a, from_base = a_base))
    b_10 = int(convert_base_R(b, from_base = b_base))
    if b_10 == 0 and task == 4:
        raise ZeroDivisionError
    c_base = int(input('Введите систему счисления результата: '))
    if task == 1:
        print('Результат:', convert_base_R(a_10 + b_10, to_base = c_base))
    elif task == 2:
        print('Результат:', convert_base_R(a_10 * b_10, to_base = c_base))
    elif task == 3:
        print('Результат:', convert_base_R(a_10 - b_10, to_base = c_base))
    elif task == 4:
        print('Результат:', convert_base_R(a_10 // b_10, to_base = c_base))
except ValueError:
    print('Ошибка введенных данных.')
except ZeroDivisionError:
    print('Ошибка деления на ноль.')
except IndexError:
    print('Ошибка индекса.')

# доп 2
 kar():
    spis = []
    x = input('Введите первое число: ')
    spis.append(x)
    y = input('Введите второе число: ')
    spis.append(y)
    if len(x) <= 10 and len(y) <= 10:
        return (int(x)) * (int(y))
    else:
        a = len(x)
        if a % 2 == 0:
            mid = a / 2
            xs, ys = str(x), str(y)

            x_list, y_list = [i for i in xs], [i for i in ys]

            first_halfX, second_halfX = x_list[: a // 2], x_list[a // 2:]
            first_halfY, second_halfY = y_list[: a // 2], y_list[a // 2:]

            xq, xw = ''.join(first_halfX), ''.join(second_halfX)
            x1, x2 = int(xq), int(xw)
            yq, yw = ''.join(first_halfY), ''.join(second_halfY)
            y1, y2 = int(yq), int(yw)
        elif a % 2 == 1:
            mid = (a + 1) / 2
            xs, ys = str(x), str(y)
            x_list, y_list = [i for i in xs], [i for i in ys]

            x_list.append(0)
            y_list.append(0)

            first_halfX, second_halfX = x_list[: a // 2], x_list[a // 2:]
            first_halfY, second_halfY = y_list[: a // 2], y_list[a // 2:]

            second_halfX.pop()
            second_halfY.pop()
            xq, xw = ''.join(first_halfX), ''.join(second_halfX)
            x1, x2 = int(xq), int(xw)
            yq, yw = ''.join(first_halfY), ''.join(second_halfY)
            y1, y2 = int(yq), int(yw)
    mult = x2 * y2 + ((x1 + x2) * (y1 + y2) - y1 * x1 - y2 * x2) * 10 ** mid + y1 * x1 * 10 ** (2 * mid)
    spis.append(mult)
    print(spis)
kar()
