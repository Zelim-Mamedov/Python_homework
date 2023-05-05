# 4.1[22]: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах. 
# Если таких чисел нет - выдать внятное диагностическое сообщение
# Наборы (списки) чисел можно считать заданными и не вводить с клавиатуры

# Примеры/Тесты:
# Input1: 2 4 6 8 10 12 10 8 6 4 2
# Input2: 3 6 9 12 15 18
# Output: 6 12     Обратите внимание: Без скобочек, в одну строку

# Input1: 2 4 6 8 10 10 8 6 4 2
# Input2: 3 9 12 15 18
# Output: Повторяющихся чисел нет

# задаем два неупорядоченных набора целых чисел
first_set = [2, 4, 6, 8, 10, 12, 10, 8, 6, 4, 2]
second_set = [3, 6, 9, 12, 15, 18]
# first_set = [2, 4, 6, 8, 10, 10, 8, 6, 4, 2]
# second_set = [3, 9, 12, 15, 18]

# инициализируем пустой список для хранения общих элементов
common = []

# проходим по всем элементам из первого набора
for num in first_set:
    # проверяем, есть ли такое число во втором наборе
    if num in second_set and num not in common:
        # если есть, то добавляем его в список общих элементов
        common.append(num)

# проверяем, были ли найдены общие элементы
if len(common) > 0:
    # если да, то сортируем и выводим их
    common.sort()
    print(f'Input1: {first_set}')
    print(f'Input2: {second_set}')
    print("Повторяющиеся числа:", common)
else:
    # если нет, выводим сообщение
    print(f'Input1: {first_set}')
    print(f'Input2: {second_set}')
    print("Повторяющихся чисел нет")