import Checker as ch
import re

border = 2
boredr_check = re.compile('^\s{%d}' % border)


def left(s, len_border=1):
    border = len_border+1
    while bool(boredr_check.match(s)):
        s = s[1:]
    if s[0] != ' ':
        s = ' '*len_border + s
    return s


ch.greet(4, '7) Функція - Left(s,l). Призначення - вирівнювання рядка s по лівому краю до довжини l.')
while True:
    text = input('Введіть текст: ')
    print('Введіть довжинну відступпу:',end=' ')
    len = ch.nCheck()
    text = left(text,len)
    print(text)
    if input('Бажаєте продовжити(+)') != '+':
        break
