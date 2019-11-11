"""
Користувач уводить суму вкладу в банк і річний відсоток.
Знайти суму вкладу через 5 років (розглянути два способи нарахування відсотків)
(REGex  у Сhecker.py)
"""



import Checker as ch

ch.greet(1, """Користувач уводить суму вкладу в банк і річний відсоток.
Знайти суму вкладу через 5 років (розглянути два способи нарахування відсотків)
""")
print('Введіть суму вкладу')
m2 = 'Введіть 1 або 2'
m1 = 'Введіть чісло >0'
summ = 0
ans = 0
pro = 0
summ = input(m1)
summ = ch.ofCheck(summ)
print('введіть річні проценти')
pro = input(m1)
pro = ch.ofCheck(pro)
print("""Оберіть тип капіталізаціі
 1) Без капіталізаціі 
 2) Шорічна капіталізаціі """)
ans = input()
while True:
    ans = ch.floatCheck(ans)
    if ans == 1 or ans == 2:
        break
    else:
        print(m2)
if ans == 1:
    summ = (5 * pro * summ) + summ
else:
    summ = (((pro + 1) ** 5) * summ)
print("Ваш вклад через 5 років:%.2f" % (summ))
input()
