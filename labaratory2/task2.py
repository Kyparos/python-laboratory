"""
Визначити і вивести на екран і цифри цілого числа n.
"""


import Checker as ch
ch.greet(2,'Визначити і вивести на екран і цифри цілого числа n.')
while True:
    n = input('Введіть число')
    n = ch.intCheck(n)
    rasr = 10
    memory = 0
    while True:
        temp = int((n%rasr - memory)/rasr * 10)
        memory += temp * (rasr/10)
        print(temp)
        if memory == n:
            break
        rasr *= 10
    ans=input('Ще раз?(+ якщо так)')
    if ans != '+':
        break
