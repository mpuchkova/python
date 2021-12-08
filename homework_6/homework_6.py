def Code(input_str):
    """return encoding str"""
    for i in range(len(input_str)):
        output.append(bytes((" ".join(input_str[i])),encoding = 'utf-8'))
    return(output)


def unCode(output):
    """return the decoded str"""
    for i in range(len(output)):
        input1.append(str(((output[i])), encoding ='utf-8'))
    return(input1)


print("____Ex 1____")
input_str=['Hello','world','.','Thank you!']
input1=[]
output=[]

print(Code(input_str))
print(unCode(output))

print("____Ex 2____")
f=open('homework_6/Input.txt')
g=open('homework_6/Output.txt','w')
try:
    c=int((f.readline().split())[1])
    h=int((f.readline().split())[1])
    o=int((f.readline().split())[1])
except:
    g.write('Проверьте правильность входного файла')
    exit()

rez="Максимально возможное число молекул спирта " + str(min(c//2,h//6,o))
g.write(rez)
g.close()
f.close()


print("____Ex 3____")
f=open('homework_6/Input_xor.txt')
g=open('homework_6/Output_xor.txt','w')
input_str=f.read()
key=input("Введите ключ шифрования(строка)  ")   ##ключ = 11100011
if len(input_str)==len(key):
    for i in range(len(input_str)):
        try:
            if int(input_str[i])==int(key[i]):  
                g.write('0')
            else:
                g.write('1')
        except:
            g.write("Проверьте правильность вводимых данных")
            break
    g.close()
    f.close()
else:
    g.write("Проверьте правильность вводимых данных")
    g.close()
    f.close()

##декодировка
z=open('homework_6/Input_xor_new.txt','w')
w=open('homework_6/Output_xor.txt')
output_str=w.read()
if len(output_str)==len(key):
    for i in range(len(output_str)):
        try:
            if int(output_str[i])==int(key[i]):  
                z.write('0')
            else:
                z.write('1')
        except:
            z.write("Проверьте правильность вводимых данных")
            break
    z.close()
    w.close()
else:
    z.write("Проверьте правильность вводимых данных")
    z.close()
    w.close()