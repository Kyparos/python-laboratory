import Checker as ch

ch.greet(1, """Користувач уводить суму вкладу в банк і річний відсоток.
Знайти суму вкладу через 5 років (розглянути два способи нарахування відсотків)
""")
print('Введіть суму вкладу')
m1 = 'Введіть сумму >0'
m2 = 'Введіть 1 або 2'
m3 = 'Введіть чісло >0'
summ = 0
ans = 0
pro = 0
while True:
    summ = ch.floatCheck()
    if summ > 0:
        break
    else:
        print(m1)
print('введіть річні проценти')
while True:
    pro = ch.floatCheck()
    if pro > 0:
        pro = pro * 0.01
        break
    else:
        print(m3)

print("""Оберіть тип капіталізаціі
 1) Без капіталізаціі 
 2) Шорічна капіталізаціі """)
while True:
    ans = ch.floatCheck()
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
