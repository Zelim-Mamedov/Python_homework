# 1.3[6]. Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.
# 	Примеры/Тесты:
# 	385916 >>> yes
# 	123456 >>> no
# ```(*)``` **Усложнение.** Вывод результат на экран сделайте одной строкой(только один print), 
# для этого используйте тернарный оператор

six_digit_number = int(input('Введите шестизначное число: '))
first_number = six_digit_number // 100000
second_number = (six_digit_number // 10000) % 10
third_number = (six_digit_number // 1000) % 10
fourth_number = (six_digit_number // 100) % 10  
fifth_number = (six_digit_number // 10) % 10
sixth_number = six_digit_number % 10
condition1 = first_number + second_number + third_number
condition2 = fourth_number + fifth_number + sixth_number
answer = (f'yes' if {condition1} == {condition2} else 'no')
print(f'{six_digit_number} >>> {answer}')