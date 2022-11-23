# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

number_of_quarter = int(input('Введите номер четверти: '))
if number_of_quarter <= 0 or number_of_quarter > 4:
    print('Введенный номер четверти должен быть числом от 1 до 4 включительно!')
elif number_of_quarter == 1:
    print(f'Четверти {number_of_quarter} принадлежат значения координат из диапазона Х > 0 и Y > 0')
elif number_of_quarter == 2:
    print(f'Четверти {number_of_quarter} принадлежат значения координат из диапазона Х < 0 и Y > 0')
elif number_of_quarter == 3:
    print(f'Четверти {number_of_quarter} принадлежат значения координат из диапазона Х < 0 и Y < 0')
else:
    print(f'Четверти {number_of_quarter} принадлежат значения координат из диапазона Х > 0 и Y < 0')
