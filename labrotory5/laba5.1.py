import Checker as ch
import re


def pars(lis, separ='0'):
    mainTemp = []
    temp = []
    for i in range(len(lis)):
        if lis[i] != separ: temp.append(lis[i])
        else:
            mainTemp.append(temp)
            temp = []
    mainTemp.append(temp)
    return mainTemp


while True:
    ch.greet(5, 'Перетворити однорівневий список у список із вкладеними списками, згідно з визначеними умовами. ')
    rawList = input('Введіть елемнти списку через пробіл з родільником "0" ').split(' ')
    newList = pars(rawList)
    print(newList)
    if input('Бажаєте продовжити(+)') != '+':
        break
