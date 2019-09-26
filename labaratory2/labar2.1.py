import Checker as ch
ch.greet(2 ,'Розрахунок за формулой')
while True:
    print('Введіть n')
    n = ch.iCheck()
    print('Введіть x')
    x = ch.nCheck()
    p = 1
    for i in range(1, n + 1):
        p *= (i + x)
    print('Відповідь:%.4f' % p)
    ans=input('Ще раз?(+ якщо так)')
    if ans != '+':
        break
