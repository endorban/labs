# база 1
def HYPERgrasshopper(n):
    GH = [None] + ([0] * max(3, n))
    GH[1] = 1
    GH[2] = 1
    for i in range(3, n + 1):
        GH[i] = GH[i - 1] + GH[i - 2]
        if i % 3 == 0:
            GH[i] += GH[i // 3]
    return GH[n]
print('Количество способов достичь её:',HYPERgrasshopper(int(input('Введите конечную точку: '))))

# база 2
import nympy as np
def maxCommonSequence(first, second):
    commonSequences = []
    i = 0
    while i < len(first) - 1:
        j = 0
        while j < len(second) - 1:
            if first[i] == second[j]:
                if first[i + 1] == second[j + 1]:
                    commonSequences.append(first[i])
                    commonSequences[-1] += first[i + 1]
                    i1 = i + 2
                    j1 = j + 2
                    while (i1 < len(first)) and (j1 < len(second)):
                        if first[i1] == second[j1]:
                            commonSequences[-1] += first[i1]
                        else:
                            break
                        i1 += 1
                        j1 += 1
            j += 1
        i += 1
    if len(commonSequences) == 0:
        return ''
    else:
        mx = 0
        for i in range(1, len(commonSequences)):
            if len(commonSequences[mx]) < len(commonSequences[i]):
                mx = i
        return commonSequences[mx]


def maxCommonSequence_Dynamically(first, second):
    first.insert(0, '1')
    second.insert(0, '2')
    E = np.zeros((len(first) + 1, len(second) + 1))
    H = np.zeros((len(first) + 1, len(second) + 1))
    for j in range(1, len(second) + 1):
        for i in range(1, len(first) + 1):
            if first[i - 1] == second[j - 1]:
                E[i][j] = 1 + E[i - 1][j - 1]
                H[i][j] = -1
            else:
                if E[i - 1][j] >= E[i][j - 1]:
                    E[i][j] = E[i - 1][j]
                    H[i][j] = 2  # l
                else:
                    E[i][j] = E[i][j - 1]
                    H[i][j] = 1  # u

    i = len(first)
    j = len(second)
    commonSequences = []
    commonSequence = ''
    while H[i][j] != 0:
        if H[i][j] == -1:
            commonSequence += first[i - 1]
            i -= 1
            j -= 1
        elif H[i][j] == 1:
            if commonSequence != '':
                commonSequence
                commonSequences.append(commonSequence)
                commonSequence = ''
            j -= 1
        elif H[i][j] == 2:
            if commonSequence != '':
                commonSequences.append(commonSequence)
                commonSequence = ''
            i -= 1
    if len(commonSequences) == 0:
        return
    else:
        mx = 0
        for i in range(1, len(commonSequences)):
            if len(commonSequences[mx]) < len(commonSequences[i]):
                mx = i
        CS = list(commonSequences[mx])
        CS.reverse()
        CS = ''.join(CS)
        return CS


print(maxCommonSequence(list(str(input('Введите первую последовательность: '))),
                        list(str(input('Введите вторую последовательность: ')))))

print(maxCommonSequence_Dynamically(list(str(input('Введите первую последовательность: '))),
                                    list(str(input('Введите вторую последовательность: ')))))

# база 3
def isSecondSequenceASubsequence(first, second):
    l, k = 0, 0
    j = 0
    i = 0
    while i < len(first):
        if first[i] == second[j]:
            k = i
            l += 1
            i += 1
            if j < len(second) - 1:
                j += 1
            elif l < len(second):
                return False
        else:
            i += 1
        if l == len(second):
            return True
    return False

print('Является ли вторая последовательность подпоследовательностью первой? Ответ:', isSecondSequenceASubsequence(str(input('Введите первую последовательность: ')), str(input('Введите вторую последовательность: '))))
# база 4

def ballOnStairs(init, n, step, show = False):
    if init >= n:
        return 0
    if n // 2 ** step < 1:
        return min(n // 16, n - init)
    routes = min(n // 2 ** step, n - init)
    for i in range(init + 1, min(init + n // 2 ** step, n) + 1):
        if show: print(init, '->', i)
        routes += ballOnStairs(i, n, step + 1, show)
    return routes

ballOnStairs(1, 4, 1, show = True)

print(ballOnStairs(1, int(input('Введите n: ')), 1, show = (True if input('Показывать все возможные ходы? (y/n) ') == 'y' else False)))

# доп 1
things = {}
num = int(input())
for i in range(num):
    itemdata = input('Название вес стоимость ').split()
    things.update({itemdata[0]:(int(itemdata[1]),int(itemdata[2]))})
print(things)
lim=int(input('Емкость сумки '))
def lst_weight_cost(items):
    weight=[items[item][0] for item in items]
    cost=[items[item][1] for item in items]
    return weight, cost
def memoisation(things, lim):
    weight, cost=lst_weight_cost(things)
    n=len(things)
    memtable=[[0 for j in range(lim+1)] for i in range(n+1)]
    for i in range(n+1):
        for j in range(lim+1):
            if i==0 or j==0:
                memtable[i][j]=0
            elif weight[i-1]<=j:
                memtable[i][j]=max(cost[i-1]+memtable[i-1][j-weight[i-1]],memtable[i-1][j])
            else:
                memtable[i][j]=memtable[i-1][j]
    return memtable, weight, cost
def itemstaken(things,lim):
    memtable, weight, cost=memoisation(things,lim)
    n=len(things)
    res=memtable[n][lim]
    a=lim
    lst_items=[]
    for i in range(n,0,-1):
        if res<=0:
            break
        if res==memtable[i-1][a]:
            continue
        else:
            lst_items.append((weight[i-1],cost[i-1]))
            res-=cost[i-1]
            a-=weight[i-1]
    picked=[]
    for i in lst_items:
        for key,value in things.items():
            if value==i:
                picked.append(key)
    return picked
bag=itemstaken(things,lim)
print(bag)
# доп 2
from __future__ import annotations
from typing import Dict, List


def tsp_solver(weights: Dict[int, Dict[int, int]]):
    amount_of_cities = len(weights)
    routes: Dict[List[int]] = dict()
    prev: Dict[List[int]] = dict()
    routes[0] = [0]
    prev[0] = [0]
    for length in range(1, amount_of_cities):
        routes[length] = float('inf')
        for j in range(1, amount_of_cities):
            if j in prev:
                continue
            if j not in weights[prev[length - 1]].keys():
                continue
            if routes[length] < routes[length - 1] + weights[prev[length - 1]][j]:
                routes[length] = routes[length - 1] + weights[prev[length - 1]][j]
                prev = j
    return routes[amount_of_cities - 1], prev


print(tsp_solver({0: {1: 3}, 1: {0: 3}}))
