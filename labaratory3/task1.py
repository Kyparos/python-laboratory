import Checker
sep= ' '

Checker.greet(3, 'Замінити перші 3 символи слів, що мають обрану довжину, на символ')
while True:
    words = input('Введить речення ')
    print('Введить задану довжину:', end='')
    leng = Checker.nCheck()
    newWords = str('')
    for word in words.split(sep):
        if len(word) == leng:
            newWords += '*'+word[3:]+sep
        else:
            newWords = newWords + (word + sep)

    print(newWords)
    if input('Бажаєте продовжити(+)') != '+':
        break
