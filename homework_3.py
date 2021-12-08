import math
import cmath 

print("____Ex 1____")
x=0
y=0
step=-1
print("  Начальное положение (0,0)")
direction=input("Введите нужное направление(вправо,влево,вниз,вверх)  ")
while ((direction!="вправо") and (direction!="влево") 
        and (direction!="вверх") and (direction!="вниз")):
    print("Вы некорректно ввели направление,попробуйте снова. ")
    direction=input("Введите нужное направление(вправо,влево,вниз,вверх)  ")

while step==-1:
    try:
        step=int(input("Введите количество шагов(целое чиcло)  "))
    except:
        continue

if direction=="влево":
    x-=step
elif (direction=="вправо"):
    x+=step
elif (direction=="вверх"):
    y+=step
else :
    y-=step

print("  Текущее положение (",x,",",y,")")

print("____Ex 2____")
x=0
y=0
step=""
print("  Начальное положение (0,0). Стоп-слово 'stop'")
while True:
    direction=input("Введите нужное направление(вправо,влево,вниз,вверх)  ")
    if direction=="stop":
        break
    while ((direction!="вправо") and (direction!="влево") and (direction!="вверх")
            and (direction!="вниз")) and ((direction!="stop")):
        print("Вы некорректно ввели направление,попробуйте снова. ")
        direction=input("Введите нужное направление(вправо,влево,вниз,вверх)  ")
    if direction=="stop":
        break    

    while step=="":
        step=input("Введите количество шагов(целое чиcло)  ")
        try:
            step=int(step)
        except:
            if step!="stop":
                step=""
            continue

    if step=="stop":
        break

    if direction=="влево":
        x-=step
        step=""
    elif (direction=="вправо"):
        x+=step
        step=""
    elif (direction=="вверх"):
        y+=step
        step=""
    else :
        y-=step
        step=""

    print("  Текущее положение (",x,",",y,")")


print("____Ex 3____")
a=float(input("Введите коэфициент при х^2  "))
b=float(input("Введите коэфициент при х  "))
c=float(input("Введите последний коэффициент  "))
D=b**2-(4*a*c)
if D>0:
    x1=(-b+math.sqrt(D))/(2*a)
    x2=(-b-math.sqrt(D))/(2*a)
    print("Корни уравнения:",x1,x2)
elif D==0:
    x=(-b)/(2*a)
    print("Корень уравнения",x)
else:
    print("Корней нет")

print("____Ex 4____")
print("  Квадратное уровнение _x^2+_x+_=0")
ask=input("Будут комплексные коэфициенты?(Да\Нет)  ")
if ask=="Да":
    a=complex(input("Введите коэфициент при х^2  "))
    b=complex(input("Введите коэфициент при х  "))
    c=complex(input("Введите последний коэффициент  "))
    D=b**2-(4*a*c)
    x1=(-b+cmath.sqrt(D))/(2*a)
    x2=(-b-cmath.sqrt(D))/(2*a)
    print("  Корни уравнения:",x1,x2)
else:
    a=float(input("Введите коэфициент при х^2  "))
    b=float(input("Введите коэфициент при х  "))
    c=float(input("Введите последний коэффициент  "))
    D=b**2-(4*a*c)
    if D>0:
        x1=(-b+math.sqrt(D))/(2*a)
        x2=(-b-math.sqrt(D))/(2*a)
        print("Корни уравнения:",x1,x2)
    elif D==0:
        x=(-b)/(2*a)
        print("Корень уравнения",x)
    else:
        x1=(-b+cmath.sqrt(D))/(2*a)
        x2=(-b-cmath.sqrt(D))/(2*a)
        print("  Корни уравнения:",x1,x2)
