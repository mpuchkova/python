import os
import numpy as np
from random import randint
import deff


print("____Ex 4____")
print("Имя операционной системы: ",os.name)
print("Имя пользователя, вошедшего в терминал: ",os.getlogin())
print("Cписок файлов и директорий в папке: ",os.listdir())

print("____Ex 5____")
print("Массив 3*3: ")
a=np.array([[randint(-10,10) for i in range(3)] for j in range(3)])
print(a)
print("Транспонированный маcсив: ", end='\n')
print(a.transpose())

print("____Ex 6____")
print(deff.Fibonachi_7(8))
print(deff.sum_7(1,2,3))
