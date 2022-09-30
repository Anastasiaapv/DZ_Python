# Задача 4. Реализуйте алгоритм перемешивания списка.
# import random
# listA = [1,2,3,4,5,6]  
# listB = [1,2,3,4,5,6] 

import random
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_length = len(list)
for i in range(list_length):
        index = random.randint(0, list_length - 1)
        temp = list[i]
        list[i] = list[index]
        list[index] = temp
print("Перемешанный список: ")
print(list)
