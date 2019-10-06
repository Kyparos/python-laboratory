import logging, Checker
logging.basicConfig(level=logging.WARN)
Checker.greet(3,'Замінити перші 3 символи слів, що мають обрану довжину, на символ')
while True:
    words = []
    while True:
        words.append(input('Введить слово'))
        if input('Бажаєте продовжити(+)') != '+':
            break
    logging.debug(words)
    for i in range(len(words)):
        words[i] = '***'+words[i][3:]
    print(words)
    if input('Бажаєте продовжити(+)') != '+':
            break