import logging
logging.basicConfig(level=logging.WARN)
words = []
while True:
    words.append(input('Введить слово'))
    if input('Бажаєте продовжити(+)') != '+':
        break
logging.debug(words)
for i in range(len(words)):
    words[i] = '***'+words[i][3:]
print(words)