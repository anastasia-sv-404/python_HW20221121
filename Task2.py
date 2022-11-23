# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

print('Введите значения предикат')
x = int(input('Введите значение Х: '))
y = int(input('Введите значение Y: '))
z = int(input('Введите значение Z: '))

first_statement = not (x or y or z)
second_statement = not x and not y and not z

if (x == 0 or x == 1) and (y == 0 or y == 1) and (z == 0 or z == 1):
    print(first_statement == second_statement)
else:
    print('Введенные значения предикат должны быть либо 0, либо 1!')
