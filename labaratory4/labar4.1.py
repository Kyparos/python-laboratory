import Checker as ch
import re, math

valid_form = re.compile('(\d+\s){19}\d+\s*')


def form_validate(tex_ex):
    return bool(valid_form.match(tex_ex))



def length_of(dot_srt,dot_end):
    x= (dot_end[0]-dot_srt[0])**2
    print(x)
    y=(dot_end[1]-dot_srt[1])**2
    print(y)
    return math.sqrt(x+y)



ch.greet(4,'7) Ввести дійсні числа х1, у1, х2, у2, ..., х10, у10. Знайти периметр десятикутника, вершини якого мають відповідно координати (х1, у1), (х2, у2), ..., (х10, у10). Написати функцію обчислення відстані між двома точками, заданими своїми координатами, які передаються при виклику функції.')
text = input('Введіть масив чисел:')
while  not form_validate(text):
    text = input('Введіть масив чисел:')
numbers = text.split(' ')
print(len(numbers))
for i in range(20, len(numbers)):
    numbers.pop(20)
print(numbers)
dots = []
for i in range(0 ,len(numbers),2):
    dots.append([int(numbers[i]),int(numbers[i+1])])
print(dots)
suma=int()
for i in range(0,len(numbers)):
    if i != len(numbers)-1:
        suma += length_of(dots[i],dots[i+1])
    else:
        suma += length_of(dots[i],dots[0])
print(suma)