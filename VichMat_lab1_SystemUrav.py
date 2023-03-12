
#Метод Гаусса с выбором главного элемента по столбцу
import numpy as np
from math import fabs

#поиск максимального элемента в n-ном столбце матрицы
def Max(a,j):
    max = fabs(a[j][j])
    index = j
    i =j
    for i in range(j,len(a)):
        if (fabs(a[i][j]) > max):
            max = a[i][j]
            index = i
    return index


def change_a(a, index, k):
    for i in range(len(a)):
        if i == index :
            for j in range(len(a[i])):
                temp = a[k][j] 
                a[k][j] = a[index][j]
                a[index][j] = temp
            break
    return a

def change_b(b,index, k):
    for i in range(len(b)):
            temp = b[k] 
            b[k] = b[index]
            b[index] = temp
            break
    return b

def gaussElimin(a,b):
    n = len(b)
    # Прямой ход
    for k in range(0,n-1):
        index= Max(a,k)
        a = change_a(a,index,k)
        b = change_b(b,index,k)
        print ("Замена \n", a)
        print (b)
        for i in range(k+1,n):
            if a[i,k] != 0.0:
                lam = a[i,k]/a[k,k]
                a[i,k+1:n] = a[i,k+1:n] - lam*a[k,k+1:n]
                b[i] = b[i] - lam*b[k]
    # Обратный ход
    for k in range(n-1,-1,-1):
        b[k] = (b[k] - np.dot(a[k,k+1:n],b[k+1:n]))/a[k,k]
    return b

# Главная программа
n_unknowns = int(input('Введите число неизвестных: '))

print('Введите коэффициенты при неизвестных:')
a = np.zeros((n_unknowns,n_unknowns), dtype="float32")
for i in range(n_unknowns):
    for j in range(n_unknowns):
        a[i,j] = float(input())

print('Введите свободные коэффициенты:')
b = np.zeros(n_unknowns, dtype="float32")
for i in range(n_unknowns):
    b[i] = float(input())

print('Значения коэффициентов:')
for i in range(n_unknowns):
    for j in range(n_unknowns):
        print('{0:+.3f}'.format(a[i,j]), end = ' ')
    print(' | {0:+.3f}'.format(b[i]), end = '\n')


print('Значения неизвестных:')
x = gaussElimin(a,b)
for i in range(n_unknowns):
    print('{0:+.3f}'.format(x[i]), end = ' ')

print()