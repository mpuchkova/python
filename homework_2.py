import math

print("____Ex 1____",'\n',"Введите первое число")
number1=input()
print(" Введите второе число")
number2=input()
try:
    number1=int(number1)
    number2=int(number2)
except:
    number1=float(number1)
    number2=float(number2)
print(" Результаты")
print(number1,"+",number2,"=",number1+number2)
print(number1,"-",number2,"=",number1-number2)
print(number1,"*",number2,"=",number1*number2)
print(number1,"^",number2,"=",number1**number2)
if number2!=0.0:
    print(number1,"/",number2,"=",number1/number2)
    print(number1,"%",number2,"=",number1%number2)
    print(number1,"//",number2,"=",number1//number2)
else:
    print("Деление на 0 невозможно!")

print("____Ex 2____",'\n',"Введите ваше имя")
name=input()
print("Здравствуйте,",name,"!")

print("____Ex 3____",'\n',"Введите строку")
str=input()[::-1]
print(str[:2])

print("____Ex 4____",'\n',"Введите радиус круга")
r=input()
try:
    r=int(r)
except:
    r=float(r)
print(math.pi*r*r)