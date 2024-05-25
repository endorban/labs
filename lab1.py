# база 1

x = 2
print(x, type(x))
x += 3
print(x, type(x))
x = 0.5 * (x+1)
print(x, type(x))
x += 0.5
print(x, type(x))
x = x < 5
print(x, type(x))
x = str(x)
print(x, type(x))

# база 2
x = 0
for i in range(1, 6):
    x += i
sr = x/5
print(f"Среднее значение данных 5 чисел равно: {format(sr, '.5f')}")

# база 3

a = 1
x = 15
c = 5
while a != 0:
    sr = x/c
    print(f"Среднее значение данных {c} чисел равно: {format(sr, '.5f')}")
    print(f"Введите число, которое желаете добавить")
    print(f"Если хотите остановиться, введите 0")
    a = float(input())
    x += a
    c += 1

# доп 1

from math import sin, acos, cos
import pylab

pi = 3.14159
g = 9.80665

def x_t(v0, a, t):
    return v0 * cos(a) * t

def y_t(v0, a, t):
    return (v0 * sin(a) * t) - (0.5 * g * (t ** 2))


v0 = input('Введите начальную скорость (по умолчанию - 5 м/с):')
if v0 == '':
    v0 = 5
v0 = float(v0)

alpha = input('Введите угол прыжка (по умолчанию - 40 градусов к горизонту):')
if alpha == '':
    alpha = 40
alpha = float(alpha)

alpha = alpha * pi / 180

h_max = (v0 * (sin(alpha) ** 2)) / (2 * g)
l_max = ((v0 ** 2) * sin(alpha * 2)) / g

print('Максимальная высота прыжка равна {} м, а максимальная длина - {} м'.format(h_max, l_max))

cornersForLength = []
for a in range(91):
    cornersForLength.append(v0 ** 2 * sin(2 * a * pi / 180) / g)
print('Начальный угол для максимальной дальности прыжка равен: {}°'
      .format(cornersForLength.index(max(cornersForLength))))


cornersForHeight = []
for a in range(91):
    cornersForHeight.append(v0 ** 2 * sin(a * pi / 180) / g)
print('Начальный угол для максимальной дальности прыжка равен: {}°'
      .format(cornersForHeight.index(max(cornersForHeight))))


x = input('Введите x (по умолчанию - 2 м):')
if x == '':
    x = 2
x = float(x)

y = input('Введите y (по умолчанию - 3 м):')
if y == '':
    y = 3
y = float(y)

t = input('Введите t (по умолчанию - 1 c):')
if t == '':
    t = 1
t = float(t)

v0 = ((y + 0.5 * g * (t ** 2)) ** 2 + x ** 2 / (t ** 2)) ** 0.5
print('Скорость равна {:.5f} м/с.'.format(v0))

alpha = acos(x / (v0 * t))
print('Угол равен {:.5f} радиан, что в градусах равняется {:.5f}.'.format(alpha, alpha * 180 / pi))

t_sh = input('Введите шаг точности построения (по умолчанию - 0.1 c):')
if t_sh == '':
    t_sh = 0.1
t_sh = float(t_sh)

print('По последним известиям график представлен ниже:')

xList, yList = list(), list()
t0 = 0

while t0 < t:
    xList.append(x_t(v0, alpha, t0))
    yList.append(y_t(v0, alpha, t0))
    t0 += t_sh

pylab.plot(xList, yList)
pylab.show()

# доп 2

print(f'Введите число')
a = int(input())
print(f'Вы ввели {a}')
x = 0
while True:
    while a >= 10:
        x += a % 10
        a = a // 10
    if a > 0:
        x += a
        print(x)
        a = x
        x = 0
    if a < 10:
        break

#Дополнительное Задание 3

print('Введите первые два числа')
a = float(input())
x = float(input())
if a >= x:
    max_ = a
    min_ = x
else:
    max_ = x
    min_ = a
while a:
    print('Введите числа, чтобы мы узнали какое из них больше, а какое меньше.')
    if a > max_:
        max_ = a
    if a < min_:
        min_ = a
    print(f'На данный момент max:{max_}, min{min_}')
    a = float(input())

