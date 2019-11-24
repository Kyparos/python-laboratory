import Checker as ch

def deleter(n,k,itero):
    if not itero == n:
        raw.pop(k)
        itero += 1
        deleter(n,k,itero)

ch.greet(6, '7) Дан одновимірний масив числових значень, що нараховує n елементів. Виключити з нього m елементів, починаючи з позиції k.')
while True:
    raw = input('Введіть список цілих чисел').split(' ')
    raw = ch.intListCheck(raw)
    iter = 0
    kk = input('введіть k: ')
    kk = ch.intCheck(kk)
    nn = input('введіть n: ')
    nn = ch.intCheck(nn)
    deleter(nn,kk,iter)
    print(raw)
    if input('Бажаєте продовжити(+)') != '+':
        break
