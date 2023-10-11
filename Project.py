print('Введите массу тела')
m = float(input())
print('Введите ваш рост')
h = float(input())
print('Введите свой возраст')
v = int(input())
imt = m / ((h/100) ** 2)
print('Ваше значение ИМТ:', round(imt,2))
if v < 65:
    if imt < 18.4:
        print('Недостаточный вес')
    elif 18.5 <= imt <= 24.9:
        print('Нормальный вес')
    elif 25 <= imt <= 29.9:
        print('Избыточный вес')
    else:
        print('Ожирение')
if 65 <= v < 75:
    if imt < 22:
        print('Недостаточный вес')
    elif 22 <= imt <= 26.9:
        print('Нормальный вес')
    elif 27 <= imt <= 29.9:
        print('Избыточный вес')
    else:
        print('Ожирение')
if v >= 75:
    if imt < 23:
        print('Недостаточный вес')
    elif 23.1 <= imt <= 27.9:
        print('Нормальный вес')
    elif 28 <= imt <= 29.9:
        print('Избыточный вес')
    else:
        print('Ожирение')

















