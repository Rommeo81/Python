'''
Задача 10:
На столе лежат n монеток. Некоторые из них лежат вверх решкой,
а некоторые – гербом. Определите минимальное число монеток,
которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
Выведите минимальное количество монет, которые нужно перевернуть.
'''

# В этом решении мы определяем количество монеток с решкой вверх,
# и затем сравниваем его с количеством монеток с гербом вверх.
# Минимальное количество переворотов, необходимых для того,
# чтобы все монетки были повернуты вверх одной и той же стороной,
# равно минимуму из этих двух значений.

# Решение данной задачи с использованием цикла while:

print(" *** Задача №10 *** ")

n = int(input("Введите количество монеток: "))
coins = input("Введите состояние монеток (0/1): ")

count_zeros = coins.count("0")  # количество монеток, лежащих вверх гербом
count_ones = n - count_zeros  # количество монеток, лежащих вверх решкой

flips_to_all_ones = count_zeros  # минимальное количество переворотов для превращения всех монеток в решки
flips_to_all_zeros = count_ones  # минимальное количество переворотов для превращения всех монеток в гербы

min_flips = min(flips_to_all_ones, flips_to_all_zeros)  # инициализация минимального количества переворотов

while count_zeros != n and count_ones != n:
    if coins[0] == "0":
        count_zeros += 1
        count_ones -= 1
    else:
        count_ones += 1
        count_zeros -= 1
    flips_to_all_ones += 1
    flips_to_all_zeros += 1
    min_flips = min(min_flips, flips_to_all_ones, flips_to_all_zeros)
    coins = coins[1:] + coins[0]

print("Минимальное количество монеток, которые нужно перевернуть:", min_flips)
print("========= Конец зачачи №10 ========== \n")




'''
Задача 11:
На столе лежат n монеток. Некоторые из них лежат вверх решкой,
а некоторые – гербом. Определите минимальное число монеток,
которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
Выведите минимальное количество монет, которые нужно перевернуть.

Пример: 4 4 -> 2 2   или   5 6 -> 2 3
'''

# Решение данной задачи с использованием цикла for:
# Для решения этой задачи мы можем перебирать все возможные пары чисел X и Y,
# проверять равенство их суммы S и произведения P заданным значениям
# и выводить первую найденную пару:

print(" *** Задача №11 *** ")

s, p = map(int, input('Введите сумму и произведение двух натуральных числел через пробел: ').split())

for x in range(1, 1001):
    for y in range(1, 1001):
        if x + y == s and x * y == p:
            print(f'Петя загадал числа {x} и {y}')
            break
    else:
        continue
    break

print("========= Конец зачачи №11 ========== \n")



'''
Задача 12:
Требуется вывести все целые степени двойки (т.е. числа вида 2**k ), не превосходящие числа N.

Пример:
10 -> 1 2 4 8
'''

# Решение:
# Здесь мы считываем значение N и инициализируем переменную power_of_two единицей.
# Затем мы запускаем цикл while, который будет выполняться,
# пока текущее значение power_of_two  не превысит заданное число N.
# Внутри цикла мы выводим значение power_of_two  на экран,
# добавляя после него пробел с помощью параметра end=' ' ,
# чтобы значения выводились в одну строку.
# Затем мы умножаем power_of_two на 2,чтобы перейти к следующей степени двойки.

print(" *** Задача №12 *** ")

n = int(input("Введите число N для расчета количества всех целых степеней числа 2 до достижения числа N: "))
power_of_two = 1

while power_of_two <= n:
    print(power_of_two, end=' ')
    power_of_two *= 2

print("\n========= Конец зачачи №12 ==========")