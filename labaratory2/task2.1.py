"""
Розрахунок за формулой

"""

import Checker as ch
ch.greet(2 ,'Розрахунок за формулой')
while True:
    n = input('Введіть n')
    n = ch.nCheck(n)
    x = input('Введіть x')
    x = ch.floatCheck(x)
    p = 1
    for i in range(1, n + 1):
        p *= (i + x)
    print('Відповідь:%.4f' % p)
    ans=input('Ще раз?(+ якщо так)')
    if ans != '+':
        break
