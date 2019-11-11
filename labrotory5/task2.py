import itertools
import Checker as ch
while True:
    a = {'1','2','ee','ww','a','d'}
    b = {'1','d', "tt", '4', '3'}
    u = {'1','2','3','4','a','b','c','d','ee','tt','ww'}
    ch.greet(5,'')
    c= a.union(b)
    print('Обєднаяння: ',c)
    c= a&b
    print('Перетин: ',c)
    c = a-b
    print('a-b : ',c)
    c = b-a
    print('b-a : ',c)
    c =  a^b
    print('сіметрична різниця: ',c)
    c = []
    for element in itertools.product(a,b):
        c.append(element)
    print('aхb: ',c)
    c = []
    for element in itertools.product(b,a):
        c.append(element)
    print('bxa: ',c)
    c = u-a
    print("'a: ",c)
    c = u - b
    print("'b: ",c)
    if input('Бажаєте продовжити(+)') != '+':
        break



