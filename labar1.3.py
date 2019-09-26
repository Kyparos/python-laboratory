def nCheck(a):
    try:
        float(a)
        return True
    except ValueError:
        print('Введіть чісло')
        return False
print("""Малахатка Олександр Володимирович
Лабараторна работа №1
Варіант №7
Обчислення конкретної функції, в залежності від введеного значення х
x>3 or x<0 F(x)=4
0≤x≤3 F(x)=x^2
""")
while True:
    z = input('x=')
    if nCheck(z):
        x=float(z)
        break
if x >= 0 and x <= 3:
    print('F(x)=%.4f'% x**2)
else:
    print('F(x)=4')
