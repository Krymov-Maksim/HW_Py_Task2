# На столе лежат n монеток. Некоторые из монеток лежат вверх решкой, а некоторые – гербом. Ваша задача - 
# определить минимальное количество монеток, которые нужно перевернуть, чтобы все монетки лежали одной 
# и той же стороной вверх.
# Входные данные:
# На вход программе подается список coins, где coins[i] равно 0, если i-я монетка лежит гербом вверх, 
# и равно 1, если i-я монетка лежит решкой вверх. Размер списка не превышает 1000 элементов.
# Выходные данные:
# Программа должна вывести одно целое число - миdнимальное количество монеток, которые нужно перевернуть.
# Пример использования На входе:
    # coins = [0, 0, 0, 0, 0]
    # 3

# orel = 0
# reshka = 0

# for i in coins:
#     if i == 0:
#         orel = orel + 1
#     if i == 1:
#         reshka = reshka + 1
# print(min(orel, reshka))

# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.
# Примечание: числа S и P задавать не нужно, они будут передаваться в тестах. 
# В результате вы должны вывести все возможные пары чисел X и Y через пробел, такие что X <= Y.
    # Пример
    # На входе:
    # s = 12
    # p = 27
    # 3 9

# s = 20      # сумма
# p = 100      # произведение
# x = 1
# y = int 
# i = 1

# for x in range (1, int(s/2)+1):
#     y = s - x
#     if x * y == p:
#         print(x, y)
#     i = i + 1


# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числаN.
# Пример

# n=512


# #Вывод
# 1
# 2
# 4
# 8
# 16

# for i in range (0, n):
#     if n >= 2**i: print(2**i)