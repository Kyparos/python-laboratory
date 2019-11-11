"""
Підрахувати кількість негативних серед чисел а, b, с (ввести з клавіатури).

"""

import Checker as ch

ch.greet(1, "Підрахувати кількість негативних серед чисел а, b, с (ввести з клавіатури).")


def check():
    """
    ask to enter number,return 1 for negative othewise 0
    :return: 0 or 1
    """

    a = input('Введите число ')
    a = ch.floatCheck(a)
    print(a)
    if a < 0:
        return 1
    else:
        return 0


count = 0

for i in range(3):
    count += check()
print('Усього %d від`ємних чісел' % count)
