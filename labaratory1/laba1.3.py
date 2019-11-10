import Checker as ch

ch.greet(1,"""Обчислення конкретної функції, в залежності від введеного значення х
x>3 or x<0 F(x)=4
0≤x≤3 F(x)=x^2
""")
x = input('x=')
x = ch.floatCheck(x)
if 0 <= x <= 3:
    print('F(x)=%.4f' % x ** 2)
else:
    print('F(x)=4')
