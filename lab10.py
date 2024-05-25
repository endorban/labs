# база 1
f = open("pi-10million.txt")
fs = f.readline()
def six_a(numbers, find):
    for i in range(10 ** 7 - 5):
        if fs[i] == find and fs[i + 1] == find and fs[i + 2] == find and fs[i + 3] == find and fs[i + 4] == find and fs[i + 5] == find:
            return (i, i + 5)

def six_b(numbers):
    for i in range(1, 10 ** 7 - 5):
        if fs[i] == '1' and fs[i + 1] == '4' and fs[i + 2] == '1' and fs[i+3] == '5' and fs[i + 4] == '9' and fs[i + 5] == '2':
            return (i, i + 5)

def phone(numbers):
    for i in range(0, 10 ** 7 - 5):
        if fs[i] == '8' and fs[i + 1] == '9' and fs[i + 2] == '9' and fs[i + 3] == '3' and fs[i + 4] == '9' and fs[i + 5] == '2' and fs[i + 6] == '7':
            return (i, i + 5)
print(six_a(fs, '9'))
print(six_a(fs, '8'))
print(six_a(fs, '0'))
print(six_b(fs))
print(phone(fs))

# база 2
from math import floor
from timeit import default_timer
import time
f = open("pi-10million.txt")
fs = f.readline(100)
LS = sorted([int(i) for i in range(1, 10000000)])
def Bin_search(numbers, num):
    left = 0
    right = len(numbers)
    while left < right:
        mid = (left + right) // 2
        if num == numbers[mid]:
            return mid
        elif num < numbers[mid]:
            right = mid
        else:
            left = mid


def goldenCutSearch(num, key):
    phi = 0.5 * (1 + 5 ** 0.5)
    a = 0
    b = len(num) - 1
    while b - a >= 1:
        x1 = int(b - (b - a)//phi)
        x2 = int(a + (b - a)//phi)
        A = num[a:x2 + 1]
        B = num[x1:b + 1]
        if key in A:
            b = x2
        elif key in B:
            a = x1
        else:
            print('goldenCutSearch: not found')
            return
    return a

def interpolating_search(arr, x):
    l = 0
    u = len(arr) - 1

    while l <= u:
        i = l + ((u - l) * (x - arr[l]) // (arr[u] - arr[l]))

        if x == arr[i]:
            return i
        elif x < arr[i]:
            u = i - 1
        else:
            l = i + 1

t = default_timer()
print(Bin_search(LS, 9999999))
print('{:.10f}'.format(default_timer() - t))

t = default_timer()
print(goldenCutSearch(LS, 9999999))
print('{:.10f}'.format(default_timer() - t))

t = default_timer()
print(interpolating_search(LS, 9999999))
print('{:.10f}'.format(default_timer() - t))

# база 3
from math import floor
from timeit import default_timer
import time
f = open("pi-10million.txt")
fs = f.readline(100)
LS = sorted([int(i) for i in range(1, 10000000)])
def Bin_search(numbers, num):
    left = 0
    right = len(numbers)
    while left < right:
        mid = (left + right) // 2
        if num == numbers[mid]:
            return mid
        elif num < numbers[mid]:
            right = mid
        else:
            left = mid


def goldenCutSearch(num, key):
    phi = 0.5*(1 + 5 ** 0.5)
    a = 0
    b = len(num) - 1
    while b - a >= 1:
        x1 = int(b - (b - a)//phi)
        x2 = int(a + (b - a)//phi)
        A = num[a : x2 + 1]
        B = num[x1 : b + 1]
        if key in A:
            b = x2
        elif key in B:
            a = x1
        else:
            print('goldenCutSearch: not found')
            return
    return a

def interpolating_search(arr, x):
    l = 0
    u = len(arr) - 1

    while l <= u:
        i = l + ((u - l) * (x - arr[l]) // (arr[u] - arr[l]))

        if x == arr[i]:
            return i
        elif x < arr[i]:
            u = i - 1
        else:
            l = i + 1

print('бинпоиск')
t = default_timer()
print(Bin_search(LS, 9999999))
print('{:.10f}'.format(default_timer() - t))

print('золотое сечение')
t = default_timer()
print(goldenCutSearch(LS, 9999999))
print('{:.10f}'.format(default_timer() - t))

print('интерпол')
t = default_timer()
print(interpolating_search(LS, 9999999))
print('{:.10f}'.format(default_timer() - t))

print('интерпол. поиск - самый эффективный')

# доп 1
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l


    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)


    for i in range(n, -1, -1):
        heapify(arr, n, i)


    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


arr = [5, 8 , 4, 2, 1, 3]
heapSort(arr)
n = len(arr)
print ('отсортированный список:')
for i in range(n):
    print ('%d' %arr[i])
