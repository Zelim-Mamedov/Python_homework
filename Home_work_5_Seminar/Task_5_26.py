# 5.1[26]: Напишите рекурсивную функцию для возведения числа a в степень b.
# Разрешается использовать только операцию умножения. Циклы использовать нельзя
# Примеры/Тесты:
# <function_name>(2,0) -> 1
# <function_name>(2,1) -> 2
# <function_name>(2,3) -> 8
# <function_name>(2,4) -> 16

num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
def degree(num1, num2):
    # случай, когда степень равна нулю
    if num2 == 0:
        return 1
    # случай, когда степень положительная и четная
    elif num2 % 2 == 0:
        return degree(num1 * num1, num2 // 2)
    # случай, когда степень положительная и нечетная
    elif num2 % 2 == 1:
        return num1 * degree(num1, num2 - 1)
    # случай, когда степень отрицательная
    elif num2 < 0:
        return 1 / degree(num1, -num2)
print(f'<degree>({num1},{num2}) -> {degree(num1, num2)}')