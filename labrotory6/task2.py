import Checker as ch
import numpy as np


def putter(i, j):
    return input('Введить елемент')


ch.greet(6, 'Виконати обробку елементів прямокутної матриці A, що має n рядків і m стовпців. Знайти суму елементів '
            'всієї матриці. Визначити, яку частку в цій сумі становить сума елементів кожного рядка. Результат '
            'оформити у вигляді матриці з n рядків і m+1 стовпців.')
while True:
    n = input('введить n: ')
    n = ch.intCheck(n)
    m = input('введить m: ')
    m = ch.intCheck(m)
    matrix = np.empty((n, m))
    for i in range(n):
        for j in range(m):
            temp = input('введить елемент: ')
            matrix[i][j] = ch.intCheck(temp)
    suma = sum(sum(matrix))
    matrixPt = np.empty((n, 1))
    for i in range(n):
        tSum = 0
        for j in range(m):
            te = int(matrix[i][j])
            tSum += te

        tSum = tSum / suma
        matrixPt[i][0] = tSum
    matrix = np.append(matrix, matrixPt, axis=1)
    print(matrix)
    if input('Бажаєте продовжити(+)') != '+':
        break