import re


def intValid(num):
    """
    check if it int
    :param num: any
    :return: bool
    """
    if bool(re.fullmatch('\s*\d+\s*', num)):
        return True
    else:
        return False


def floatValid(num):
    """
        check if it float
        :param num: any
        :return: bool
        """
    if bool(re.fullmatch('\s*\d+(\.\d+)?\s*', num)):
        return True
    else:
        return False


def intLitstValid(iList):
    """
    check if it list of int
    :type iList: list
    """
    for inta in iList:
        if intValid(inta):
            continue
        else:
            return False
    return True


def floatCheck(a):
    """
     if a is float return it or force to enter float
    :param a: any
    :return: float
    """
    while True:
        if floatValid(a):
            return float(a)
        else:
            print('введіть тільки цифри та \'-\'')
            a = input()


def intCheck(a):
    """
    if a is int return it or force to enter int
    :param a: any
    :return: int
    """

    while True:
        if intValid(a):
            return int(a)
        else:
            print('Введить тильки цілі числа')
            a = input()


def greet(num, task):
    """
    printing info about laba
    :param num: nuber of laba : int
    :param task: theme : str
    """
    print("""Малахатка Олександр Володимирович
    Лабараторна работа №%d
    Варіант №7
    %s
    """ % (num, task))


def nCheck(num):
    """
    if a is Natural number return it or force to enter Natural number
    :param a: any
    :return: NAtural number
    """
    b = intCheck(num)
    while True:

        if b >= 1:
            return b
        print('введіть занчення ≥ 1')
        b = intCheck()


def oCheck(num):
    """
    if a is Natural+0 number return it or force to enter Natural+0 number
    :param num: any
    :return: NAtural+0 number
    """
    b = intCheck(num)
    while True:
        if b >= 0:
            return b
        print('введіть занчення ≥ 1')
        b = intCheck()


def ofCheck(num):
    """
    if a is float>=0 number return it or force to enter Natural+0 number
    :param num: any
    :return: float>=0 number
    """
    b = floatCheck(num)
    while True:
        if b >= 0:
            return b
        print('введіть занчення ≥ 1')
        b = intCheck()


def intListCheck(iList):
    while True:
        if intLitstValid(iList):
            return iList
        else:
            print('введіть список цілочисленних значень')
            iList = input().split(' ')
