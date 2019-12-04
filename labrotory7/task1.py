import Checker as ch
import os

ch.greet(7, 'Є файл, в кожному рядку якого записано ціле число. \nВизначити:\nсуму всіх чисел;\nсереднє арифметичне '
            'всіх чисел;\nсуму чисел, записаних на 2-й, 4-й, 6-й, ... рядках;\nкількість парних чисел.\nСписки не '
            'використовувати.')

while True:
    fName = input('ведить им\'я вводного файлу')
    while not os.path.exists(fName):
        fName = input("введіть коректне ім'я файлу")
    rFile = open(fName, 'r')
    summ = 0
    sumEv = 0
    evQu = 0
    i = 1
    while True:
        temp = rFile.readline()
        if temp == '':
            break
        else:
            temp = int(temp)
        summ += temp
        if i % 2 == 0:
            sumEv += temp
        if temp % 2 == 0:
            evQu += 1
        i += 1
    ofName = input('ведить им\'я виводного файлу')
    wFile = open(ofName, 'w')
    wFile.write((str(summ)+'\n'))
    mid = summ / i
    wFile.write((str(mid)+'\n'))
    wFile.write((str(sumEv)+'\n'))
    wFile.write((str(evQu)+'\n'))
    rFile.close()
    wFile.close()
    if input('Бажаєте продовжити(+)') != '+':
        break
