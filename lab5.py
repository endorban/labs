# база 1
s = input('Введите строку: ')
Up, Low = 0, 0
for i in s:
    if i.isupper():
        Up += 1
    else:
        Low += 1

if Up > Low:
    print(s.upper())
elif Up < Low:
    print(s.lower())
else:
    print(s)

# база 2
s = "объектно-ориентированный"
print(s[:6])
print(s[4:6] + s[7])
print(s[9:17])
print(s[16] + s[12] + s[13] + s[14] + s[19])
print(s[4] + s[7] + s[5])
print(s[1]+ s[7] + s[5])
print(s[6:8] + s[14] + s[19])
print(s[18:15:-1])
print(s[0]+s[4] + s[6] + s[7])

# база 3
num1 = input('Введите первое число: ')
num2 = input('Введите второе число: ')

def Check(x):
    if (x.isdigit()):
        return int(x)
    else:
        new_num = ''
        for i in x:
            if i in '123457890':
                new_num += i
    if not new_num:
        return Check(input('Введите число заного: '))
    return int(new_num)
print(Check(num1) + Check(num2))

# база 4
dictionary = {
    1: 'объект',
    2: 'кто',
    3: 'ориентир',
    4: 'рента',
    5: 'кот',
    6: 'бот',
    7: 'нота',
    8: 'вор',
    9: 'окно',
}

def d(dictionary):
    x = dictionary.items()
    dictionary_new = dict()
    for i in x:
        dictionary_new[i[1]] = i[0]
    return (dictionary_new)

print(d(dictionary))

# база 5
school = {
    '1а' : 30,
    '1б' : 31,
    '1в' : 29,
    '1г' : 30,
    '2а' : 29,
    '2б' : 32,
    '2в' : 33,
    '2г' : 30,
    '11а': 9,
}

def append_students(dictionary):
    School_class = input('Введите класс в котором изменилось кол-во учеников: ')
    School_students = int(input('Сколько теперь учеников в классе? '))
    dictionary[School_class] = School_students
    return dictionary

def append_class(dictionary):
    School_class = input('Введите название нового класса: ')
    School_students = int(input('Введите количество учащихся этого класса: '))
    dictionary[School_class] = School_students
    return dictionary

'''
Не знаю, должны ли ученики распределяться по уровню знаний или нет, 
поэтому в данной школе ученикам расформированного класса не повезло
'''

def delete_class(dictionary):
    School_class = input('Введите класс, который был расформирован: ')
    School_students = dictionary[School_class]
    del dictionary[School_class]
    if School_students % len(dictionary) == 0:
        for i in dictionary.keys():
            dictionary[i] += School_students//len(dictionary)
    else:
        Raspr = School_students % len(dictionary)
        for i in dictionary.keys():
            if Raspr != 0:
                dictionary[i] += 1
                Raspr -= 1
            else:
                break
        for i in dictionary.keys():
            dictionary[i] += School_students//len(dictionary)
    return dictionary

def statistic(dictionary):
    classes = dictionary.keys()
    students = 0
    for i in classes:
        students += dictionary[i]
    return len(classes), students, dictionary

action = input('Выберите букву действия\n"а" Изменилось кол-во учащихся\n"б" Добавился новый класс\n"в" Класс был расформироаван\n'
               '"г" Получить статистику\nПункт: ')

total = statistic(school)
if action == 'а':
    print(append_students())
elif action == 'б':
    print(append_class())
elif action == 'в':
    print(delete_class(school))
elif action == 'г':
    temp = statistic(school)
    print(f'Количество классов в школе: {temp[0]}\nКоличество учеников во всех классах: {temp[1]}')
    print('Распределение учеников по классам:')
    for i in temp[2]:
        print(f'Количество учеников в классе {i} составляет {temp[2][i]}')

else:
    print('Некорректно выбрано действие, попробуйте ещё раз')
    action = input('Выберите букву действия\n"а" Изменилось кол-во учащихся\n"б" Добавился новый класс\n"в" Класс был расформироаван\n'
               '"г" Получить статистику\nПункт: ')

# доп 1
dictionary = {1: 'acc', 2: 'cab', 3: 'ccb'}
def reverse(dictionary):
    temp_dict = {}
    for i in dictionary.items():
        for i1 in i[1]:
            if i1 not in temp_dict:
                temp_dict[i1] = str(i[0])
            else:
                temp_dict[i1] += str(i[0])
    return temp_dict
print(reverse(dictionary))

# доп 3
N = int(input('Введите количество чисел: '))
number_2, number_13, number_26 = 0, 0, 0
NX = 0

for i in range(1, N + 1):
    number = int(input(f'Введите число номер {i}: '))
    if number % 26 == 0:
        number_26 += 1
    elif number % 13 == 0:
        number_13 += 1
    elif number % 2 == 0:
        number_2 += 1

total_pairs = number_26 * (number_26-1) // 2 + number_26 * (N-number_26) + number_2 * number_13

print(f'На 26 делится произведение {total_pairs} пар чисел')

