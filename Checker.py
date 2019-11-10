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


def floatCheck(a):
    """
    if a is float return it or force to enter float
    :param a: any
    :return: float
    """
    a = input()
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
    a = input()
    while True:
        if intValid(a):
            return int(a)
        else:
            print('Введить тильки цілі числа')
            a = input()


def greet(a, b):
    """
    printing info about laba
    :param a: nuber of laba : int
    :param b: theme : str
    """
    print("""Малахатка Олександр Володимирович
    Лабараторна работа №%d
    Варіант №7
    %s
    """ % (a, b))


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
    :param a: any
    :return: NAtural+0 number
    """
    b = intCheck(num)
    while True:
        if b >= 0:
            return b
        print('введіть занчення ≥ 1')
        b = intCheck()
