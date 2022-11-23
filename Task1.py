# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# 6 -> да
# 7 -> да
# 1 -> нет

day_of_week = int(input('Введите номер дня недели: '))
if day_of_week <= 0 or day_of_week > 7:
    print('Введенное число должно находиться в диапазоне от 1 до 7 включительно')
elif day_of_week == 6 or day_of_week == 7:
    print(f'Введенное число {day_of_week} обозначает выходной день')
else:
    print(f'Введенное число {day_of_week} обозначает будний день')