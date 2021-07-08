def mergeSort(l):
    if len(l) < 2: return l
    result, L, R, i, j = [], mergeSort(l[:len(l) // 2]), mergeSort(l[len(l) // 2:]), 0, 0
    while i < len(L) and j < len(R): result, j, i = result + ([R[j]] if L[i] > R[j] else [L[i]]), j + (L[i] > R[j]), i + (L[i] <= R[j])
    return result + L[i:] + R[j:]
def bubbleSort(l):
    for i in range(len(l)):
        flag = True
        for j in range(len(l) - 1, i, -1):
            if l[j - 1] > l[j]: flag, l[j - 1], l[j] = False, l[j], l[j - 1]
        if flag: return l
def selectionSort(l):
    result = []
    while l:
        min = 0
        for i in range(len(l)):
            if l[i] < l[min]: min = i
        result += [l.pop(min)]
    return result
def bitonicSort(l):
    gap = 2 ** (len(bin(len(l) - 1)) - 2) - len(l)
    l, k = [min(l)] * gap + l, 2
    while k <= len(l):
        j = k // 2
        while j:
            for i in range(len(l)):
                x = i ^ j
                if x > i:
                    if (not(i & k) and l[i] > l[x]) or (i & k and l[i] < l[x]): l[i], l[x] = l[x], l[i]
            j //= 2
        k *= 2
    return l[gap:]
# The next sorting algorithm actually needs some imports
# This is a sorting algorithm in o(n) complexity
# I will run for ints *and* floats (I know count sort is possible but this is for floats too)
# I know it's impossible, but it is
# It is my own invention...
from threading import Thread
from time import sleep
o = []
def threadsort(l):
    global o
    o = []
    max_value = max(l)
    def insert(element):
        global o
        sleep(element / max_value)
        o.append(element)
    for item in l: Thread(target=insert, args=(item,)).start()
    sleep(1)
    return o
