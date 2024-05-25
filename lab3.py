# база 1
def task1(x):
    return (((99 < x < 1000) and (x % 10 == 0)) or (x % 2 == 0) and ((x % 3 == 0) and (x % 5 == 0)) or (2 <= x <= 6) or
            ((99 < x < 1000) and (str(x).count(str(x)[0]) == 3)))

print(task1(int(input('Введите число: '))))

# база 2
def t(x):
    return (abs(x) + 5 > 3)
def f(x):
    return (abs(x) + 5 < 3)

num = int(input("Введите число: "))
print(t(num))
print(f(num))

# база 3
def a(x, y):
    return (x > 4 and y > 3) or ((y < -1 * x) and (x < 4 and y < 3))

def b(x, y):
    return ((x**2 + y**2 > 9) and (-3 < x < 3) and  (-3 < y < 3))

def c(x, y):
    return ((x-5)**2 + (y-3)**2 > 9) and (y < 3) and (x < 5)

x, y = int(input('Введите число x: ')), int(input('Введите число y: '))
print(f'а) {a(x,y)}\nб) {b(x, y)}\nв) {c(x, y)}')

# база 4
def f():
    x = int(input("Введите число: "))
    if x >= 0:
        print(positive(x))
    else:
        print(negative(x))

def positive(x):
    return 'Положительное'

def negative(x):
    return 'Отрицательное'

f()

# база 5
def getInput():
    return input("Введите строку: ")

def testInput(x):
    try:
        int(x)
        return True
    except:
        return False

def strToInt(x):
    return int(x)

def printInt(x):
    print(x)

x = getInput()
if testInput(x):
    printInt(strToInt(x))

# доп 1
def check_multiplication_knowledge():
    count_true = 0
    count_false = 0
    combo_true = 0
    combo_false = 0

    while count_true < 5:
        num1 = int(input("Введите первое число: "))
        num2 = int(input("Введите второе число: "))
        correct_answer = num1 * num2
        user_answer = int(input(f"Результат умножения {num1} на {num2}: "))

        if user_answer == correct_answer:
            print("Правильно\n")
            count_true += 1
            combo_true += 1
            combo_false = 0
        else:
            print("Неправильно")
            print(f"Правильный ответ: {correct_answer}\n")
            count_false += 1
            combo_false += 1
            consecutive_correct = 0

        if combo_true == 3 and user_answer == correct_answer:
            print("lvl rockstar, g nexxt\n")
        elif combo_false == 3 and user_answer != correct_answer:
            print("go cry.\n")

    print('Получено 5 верных ответов, программа завершена.')


check_multiplication_knowledge()

# доп 2
str = input('Введите строку: ')
def clean(x):
    a = ''
    for i in x:
        if i not in a and i != ' ':
            a += i
    return a

print('Результат удаления одинаковых символов:', clean(str))
