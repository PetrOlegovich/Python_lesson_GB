# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается
# сделать один разлом по прямой между дольками то есть разломить шоколадку на два прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no
#
# a = int(input("какая ширина  шоколаднки  :   "))
# b = int(input('какая длинна шоколадки  :  '))
# c = int(input("сколько хочешь отломить за раз ? : "))
# if c % a == 0 or c % b == 0:
#     print("у тебя все получится !!! ")
# else:
#     print("Не сегодня, найди другую шоколадку.")


# Задача 2: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)
#
# a = input('введите трехзначное число:  ')
# b = int(a)
# if b > 99 and b < 1000:
#     a1 = int(a[0])
#     a2 = int(a[1])
#     a3 = int(a[2])
#     sum = a1 + a2 + a3
#     print(sum)
# else:
#     print('Вы ввели не трехзначное число')


# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,  где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no
#
# a = input('Введите номер билета из 6 цифр: ')
# b = int(a)
# if b > 99999 and b < 1000000:
#     sum1 = int(a[0]) + int(a[1]) + int(a[2])
#     sum2 = int(a[3]) + int(a[4]) + int(a[5])
#     if sum1 == sum2:
#         print('это счастливый билет!!! Съешь его !!!')
#     else:
#         print('Это не счасливый билет =( ')
# else:
#     print("Ты ввел число не из 6 цифр!  ")



# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов.Вместе они сделали S журавликов.
#  Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
#  а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# 6 -> 1 4 1
# 24 -> 4 16 4
# 60 -> 10 40 10
#
# a = int(input('всего журавликов сделано : '))
# p = a / 3 / 2
# s = p
# k = (p + s) * 2
# print(p, k, s)


# 10 /     перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2
# 2

# n = int(input('Введите кол-во монеток :  '))
# eagle = 0
# tails = 0
# for i in range(n):
#     money = int(input("Введите 0 или 1. где 0 это решка, а 1 это орел:  "))
#     if money == 1:
#         eagle += 1
#     else:
#         tails += 1
# if eagle > tails:
#     print(f'надо перевернуть монетку с решкой , их меньше ,а именно :  {tails}')
# elif tails > eagle:
#     print(f'надо перевернуть монетку с орлом, их меньше ,а именно :  {eagle}')
# else:
#     print(f'их одинаковое количество , переверни что хочешь ! ')




# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3
#
# s = int(input("Сумма чисел: "))
# p = int(input("Произведение чисел: "))
# for y in range(0, 1001):
#     for x in range(0, 1001):
#         if x + y == s and x * y == p:
#             print(",".join((str(x), str(y))))
#
# НИЖЕ ПРЕДСТАВЛЕНО РЕШЕНИЕ В 2 СТРОКИ!!!!
# s, p = int(input("Сумма чисел: ")), int(input("Произведение чисел: "))
# print(*[",".join((str(x), str(y))) for y in range(0, 1001) for x in range(0, 1001) if x + y == s and x * y == p])



# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8
#
# n = int(input("Введите число : "))
# res = i = 0
# x = 2
# while res < n:
#     res = x ** i
#     i += 1
#     if res < n:
#         print(res)




# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
#  Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
#  В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
# n = 5
# 1 2 3 4 5
# x = 3

# -> 1

# import random
#
# array = []
# n = int(input("Введите величину случайнозаполняемого  массива : "))
# k = int(input("Введите число которое вы хотите тут найти (от 1 до 10): "))
# j = 0
# count = 0
# for i in range(0, n):
#     array.append(random.randrange(1, 11, 1))
# print(f'Ваш массив : \n {array}')
# while j < n:
#     if array[j] == k:
#         count += 1
#     j += 1
# print(f'Ответ : {count}. \nСтолько раз встречается эта цифра ')




# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих строках записаны
#  N целых чисел Ai. Последняя строка содержит число X

# n = 5
# 1 2 3 4 5
# x = 6
# -> 5

#
# import random
# array = []
# n = int(input("Введите величину случайно-заполняемого  массива : "))
# j =  0
# count = 0
# for i in range(0, n):
#     array.append(random.randrange(1, 11, 1))
# print(f'Ваш массив : \n {array}')
# k = int(input("Введите число которое вы хотите тут найти (от 1 до 10): "))
# while j < n:
#     if array[j] == k:
#         if j == 0:
#             print(f'ближайшее число : {array[array.index(array[j+1])]}')
#             count += 1
#         else:
#             print(f'ближайшее число : {array[array.index(array[j-1])]}')
#             count += 1
#     j += 1
# if count == 0:
#     print("Число в масиве не встретилось, попробуй в другой раз. ")
# print("  КОНЕЦ  ")




# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
#  В случае с английским алфавитом очки распределяются так:
# A,E,I,O,U,L,N,S,T,R – 1 очко;
# D,G – 2 очка;
# B,C,M,P – 3 очка;
# F,H,V,W,Y – 4 очка;
# K – 5 очков;
# J,X – 8 очков;
# Q,Z – 10 очков.
# А русские буквы оцениваются так:
# А,В,Е,И,Н,О,Р,С,Т – 1 очко;
# Д,К,Л,М,П,У – 2 очка;
# Б,Г,Ё,Ь,Я – 3 очка;
# Й,Ы – 4 очка;
# Ж,З,Х,Ц,Ч – 5 очков;
# Ш,Э,Ю – 8 очков;
# Ф,Щ,Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово,
# которое содержит либо только английские, либо только русские буквы.

# Ввод:
# ноутбук
# Вывод:
# 12

#
# s = input("Введите слово : ").lower()
# count = 0
# sum = 0
# d = {
#     'а':1, 'в':1, 'е':1, 'и':1, 'н':1, 'о':1, 'р':1, 'с':1, 'т':1,
#     'д':2, 'к':2, 'л':2, 'м':2, 'п':2, 'у':2,
#     'б':3, 'г':3, 'ё':3, 'ь':3, 'я':3,
#     'й':4, 'ы':4,
#     'ж':5, 'з':5, 'х':5, 'ц':5, 'ч':5,
#     'ш':8, 'э':8, 'ю':8,
#     'ф':10, 'щ':10, 'ъ':10,
#     'a':1, 'e':1, 'i':1, 'o':1, 'u':1, 'l':1, 'n':1, 's':1, 't':1, 'r':1,
#     'd':2, 'g':2,
#     'b':3, 'c':3, 'm':3, 'p':3,
#     'f':4, 'h':4, 'v':4, 'w':4, 'y':4,
#     'k':5,
#     'j':8, 'x':8,
#     'q':10, 'z':10
#     }
# for i in s:
#     if i in d:
#         count = d.get(i)
#         sum = sum + count
#     else:
#         count += 0
# print(f'Это слово стоит :  {sum} очков ')


# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены
# только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов. Эти
# кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте
# выросло ai ягод. В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из
# управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед
# некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать
# за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.


# gardenBed = int(input("number of bushes :  "))
# berryBush = []
# i = 0
# for i in range(gardenBed):
#     berryBush.append(int(input("berry : ")))
# print(berryBush)
# # Создал массив. заполним массив . и все . далее(что ниже ) вообще не понял. надо разобраться !!!!
#
# berryCount = list()
# for i in range(len(berryBush) - 1 ):
#     berryCount.append(berryBush[i-1] + berryBush[i] + berryBush[i+1])
# berryCount.append(berryBush[-2] + berryBush[-1] + berryBush[0])
# print(max(berryCount))



# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке
# возрастания все те числа, которые встречаются в обоих наборах. Пользователь вводит 2 числа. n - кол-во элементов
# первого множества. m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.


# n = int(input("Введите размер множества N : "))
# m = int(input("введите размер множества M : "))
# firstNumbers = set()
# doubleNumbers = set()                               #создал пустые множества
# for i in range(n):
#     firstNumbers.add(int(input("числа  N : ")))
# заполняю пустое множество с клавиатуры и сразу перевожу в инт ( для вывода по порядку)
# for i in range(m):
#     doubleNumbers.add(int(input("числа  M  : ")))
# unique = firstNumbers.union(doubleNumbers)          # обьеденяю множества в 1 целое
# print(unique)


# Задача 26: Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.

# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

# a = int(input("введите число А : "))
# a1 = a
# b = int(input("введите число В : "))
# count = 1
#
#
# def st(x, y, z, w):
#     if z == y:
#         return x
#     z += 1
#     return st(x * w, y, z, w)
#
# print(f' Итог = {st(a, b, count, a1)}')



# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# 2 2
# 4

# n = int(input("введите первое число  : "))
# p = int(input("введите второе число  : "))
#
# def sum(x, y):
#     if x == 0:
#         return y
#     return sum(x-1, y+1)
#
# print(f' итог: {sum(n, p)}')



# Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не
# настолько просто, насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть,
# если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять
#  из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами.
#  Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом
#  все в порядке и “Пам парам”, если с ритмом все не в порядке

# Ввод:
# пара-ра-рам рам-пам-папам па-ра-па-дам

# Вывод:
# Парам пам-пам

# def kolvo_a(x):
#     count = 0
#     for i in x:
#         if i == 'а' or i == 'е' or i == 'у' or i == 'о' or i == 'э'or i == 'я' or i == 'и' or i == 'ю' or i == 'ё':
#             count +=1
#         else:
#             count += 0
#     return count
#
# a1 = input(" первая строка : ")
# b1 = a1.split()
# c1 = '-'.join(b1)
#
# a2 = input(" вторая стока : ")
# b2 = a2.split()
# c2 = '-'.join(b2)
#
# a3 = input(" Третья строка : ")
# b3 = a3.split()
# c3 = '-'.join(b3)
#
#
# if kolvo_a(c1.lower()) == kolvo_a(c2.lower()) == kolvo_a(c3.lower()):
#     print(f'\n{c1}\n{c2}\n{c3}\nПарам пам-пам \n    ритм есть')
# else:
#     print(f'\n{c1}\n{c2}\n{c3}\n Пам парам \n    ритма нет(')



# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),которая принимает в качестве
# аргумента функцию, вычисляющую элемент по номеру строки и столбца. Аргументы num_rows и num_columns указывают число
# строк и столбцов таблицы, которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
# почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента,
# как, например, у операции умножения.

# Ввод:
# print_operation_table(lambda x, y: x * y)

# Вывод:
# 1 2 3 4 5 6
# 2 4 6 8 10 12
# 3 6 9 12 15 18
# 4 8 12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36


# def operation_table(x, y):
#     res = list()
#     for i in range(x):
#         for j in range(y):
#             res.append((i+1)*(j+1))
#         print(res)
#         res = []
#
# a = 6
# b = 6
# print(operation_table(a,b))
