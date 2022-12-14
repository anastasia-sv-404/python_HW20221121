# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка
# (или на какой оси она находится).
# Пример:
# x=34; y=-30 -> 4
# x=2; y=4 -> 1
# x=-34; y=-30 -> 3

x = int(input('Введите координату на оси Х: '))
y = int(input('Введите координату на оси Y: '))

# if x == 0 or y == 0:
#     print('Ни одно из введенных значений координат не должно равняться 0!')  # по условию указано, что X ≠ 0 и Y ≠ 0
# elif x > 0:
#     if y > 0:
#         print(f'Координаты точки ({x};{y}) принадлежат 1 четверти')
#     else:
#         print(f'Координаты точки ({x};{y}) принадлежат 4 четверти')
# elif x < 0:
#     if y > 0:
#         print(f'Координаты точки ({x};{y}) принадлежат 2 четверти')
#     else:
#         print(f'Координаты точки ({x};{y}) принадлежат 3 четверти')


# Второй вариант решения
if x != 0 and y != 0:
    if x > 0:
        if y > 0:
            print(f'Координаты точки ({x};{y}) принадлежат 1 четверти')
        else:
            print(f'Координаты точки ({x};{y}) принадлежат 4 четверти')
    else:
        if y > 0:
            print(f'Координаты точки ({x};{y}) принадлежат 2 четверти')
        else:
            print(f'Координаты точки ({x};{y}) принадлежат 3 четверти')
else:
    print('Введены неверные значения!')
