import random


print("____Ex 1____")
d=input("Введите список чисел через пробел ").split(" ")
for i in range(len(d)-1):
	for j in range(len(d)-1):
		if float(d[j]) > float(d[j+1]):
			d[j], d[j+1] = d[j+1], d[j]
print("Отсортированный список ", end=' ')
for i in range(len(d)):
    print(d[i],end =' ')
print()

print("____Ex 2____")
d = dict([('#fff', (255,255,255)), ('#000', (0,0,0)),('#f00',(255, 0, 0)),('#0a0791',(10, 7, 145)),('#1da811',(29, 168, 17)),('#e317cf',(227, 23, 207))])
print(d.keys())
print(d.values())

print("____Ex 3____")
a={random.randint(0,100) for i in range(10)}
b={random.randint(0,100) for i in range(10)}
print(a)
print(b)
print("Входят одновременно в оба множества ",set.intersection(a,b))
print("Входят только в первое множество ",a.difference(b))
print("Входят только во второе множество ",b.difference(a))
print("Входят в 1 или во 2 множество, но не входят одновременно в оба ",a.symmetric_difference(b))

print("____Ex 4____")
inventory=dict([('Молоток', 80), ('Палка', 50), ('Лук', 150)])
i=input("Игровой инвентарь. Добавить предмет-Добавить, Удалить предмет-Удалить  ")
if i=="Добавить":
    item=input("Введите название предмета  ")
    weight=int(input("Введите вес предмета(целое число)  "))
    inventory[item]=weight
elif i=="Удалить":
    item=input("Введите название предмета,который хотите удалить  ")
    del inventory[item]

print(inventory)
