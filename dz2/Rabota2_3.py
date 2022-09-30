# Задача 3. Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

import math
num = int(input('Введите число: '))

listN =[]
for i in range(1,num+1):
    listN.append((1+1/i)**i)
    
print(listN)
print(sum(listN))