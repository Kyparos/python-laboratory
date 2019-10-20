import Checker as ch
import re
border = 2
boredr_check = re.compile('^\s{%d}'%border)
def left(s,len_border=2):
    border = len_border
    while bool(boredr_check.match(s)):
        print('1')
        s = s[1:]
    return s

ch.greet(4,'7) Функція - Left(s,l). Призначення - вирівнювання рядка s по лівому краю до довжини l.')
while True:
    text = input('Введіть текст: ')
    text = left(text)
    print(text)
    if input('Бажаєте продовжити(+)') != '+':
        break
