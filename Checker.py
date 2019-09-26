def nCheck():
    while True:
        a = input()
        try:
            a = float(a)
            return a
        except ValueError:
            print('введіть тільки цифри та \'-\'')


def iCheck():
    while True:
        b = intCheck()
        if b >= 1:
            return b
        print('введіть занчення ≥ 1')


def intCheck():
    while True:
        a = input()
        try:
            a = int(a)
            return a
        except:
            print('Введить тильки цілі числа')


def greet(a ,b):
    print("""Малахатка Олександр Володимирович
    Лабараторна работа №%d
    Варіант №7
    %s
    """ % (a,b))
