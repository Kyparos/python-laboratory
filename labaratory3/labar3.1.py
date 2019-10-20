import Checker


Checker.greet(3, 'Замінити перші 3 символи слів, що мають обрану довжину, на символ')
while True:
    words = input('Введить речення ')
    print('Введить задану довжину:', end='')
    leng = Checker.iCheck()
    newWords = str('')
    for word in words.split(' '):
        if len(word) == leng:
            newWords += '*'+word[3:]+' '
        else:
            newWords = newWords + (word + ' ')

    print(newWords)
    if input('Бажаєте продовжити(+)') != '+':
        break
