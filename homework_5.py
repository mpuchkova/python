
def password():
    str=input("Введите строку-пароль  ")
    count=0
    if (len(str)>=6):
        try:
            int(str)
            return("False")
        except:
            str=str.lower()
            if "password" in str:
                return("False") 
            else:
                for i in range(len(str)):
                    try:
                        int(str[i])
                        return("True")
                        break
                    except:
                        count+=1
                if count==len(str):
                    return("False")
    else:
        return("False")


def sum(*args):
    rez=0
    for i in args:
        rez+=i
    return(rez)
    

def Fibonachi(x):
    x=int(x)
    if x in (1, 2):
        return 1
    else:
        return Fibonachi(x - 1) + Fibonachi(x - 2)

print("____Ex 1____")
print(password())


print("____Ex 2____")
print(sum())
print("2+2=",sum(2,2))
print("2,5+2,5=",sum(2.5,2.5))
print("-7+8+9-5=",sum(-7,8,9,-5))
print("10+30.1=",sum(10,30.1))


print("____Ex 3____")
print("Первое число Фибоначчи",Fibonachi(1))
print("Пятое число Фибоначчи",Fibonachi(5))
print("Восьмое число Фибоначчи",Fibonachi(8))