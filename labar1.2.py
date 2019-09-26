count = 0
def nCheck(a):
    try:
        float(a)
        return True
    except ValueError:
        print('Помилка: хибне значення')
        return False
def check():
    while True:
        a = (input('Введите число '))
        if nCheck(a):
            a= float(a)
            break
    print(a)
    if a < 0:
        return 1
    else: return 0
print("""Малахатка Олександр Володимирович
Лабараторна работа №1
Варіант №7
Підрахувати кількість негативних серед чисел а, b, с (ввести з клавіатури).
""")
for i in range(3):
    count += check()
print('Усього %d від`ємних чісел'% count)


