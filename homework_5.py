
def password():
    str=input("Введите строку-пароль  ")
    count=0
    if (len(str)>=6):
        try:
            int(str)
            print("False")
        except:
            str=str.lower()
            if "password" in str:
                print("False") 
            else:
                for i in range(len(str)):
                    try:
                        int(str[i])
                        print("True")
                        break
                    except:
                        count+=1
                if count==len(str):
                    print("False")
    else:
        print("False")

def sum():
    a=input("Введите числа через пробел, сумму которых хотите узнать  ").split()
    rez=0
    try:
        for i in range(len(a)):
            a[i]=float(a[i])
            rez+=a[i]
        print(rez)
    except:
        print("Неверно введены числа")
    

def Fibbonachi():
    c=[]
    b=input("Введите целое число для нахождения числа Фиббоначи  ")
    try:
        n=int(b)
    except:
        print("Неверно введено число")
        exit()
    if n==0:
        print(0)
        exit()
    for i in range(n+1):
        c.append(0)
    c[1]=1
    for i in range (2,n+1):
        c[i]=c[i-1]+c[i-2]
    return(c[n])

print("____Ex 1____")
password()

print("____Ex 2____")
sum()

print("____Ex 3____")
print(Fibbonachi())