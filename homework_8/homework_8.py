class animals():
    def __init__(self,name,weight,country):
        self.name = name
        self.weight = weight
        self.country=country

    def behaviour(self):
        print("Я животное!")


class mammals(animals):
    def __init__(self,name,weight,country,feeding_period):
        super().__init__(name,weight,country)
        self.feeding_period=feeding_period

    def behaviour_m(self):
        print("Я кормлю своих детей молоком!")


class human(mammals):
    def __init__(self,name,weight,country,feeding_period,language):
        super().__init__(name,weight,country,feeding_period)
        self.language=language

    def behaviour_h(self):
        print("Я обладаю прямохождением!")


class cat(mammals):
    def __init__(self,name,weight,country,feeding_period,count_kitten):
        super().__init__(name,weight,country,feeding_period)
        self.count_kitten=count_kitten

    def behaviour_c(self):
        print("Я умею мяукать!")


class dog(mammals):
    def __init__(self,name,weight,country,feeding_period,count_puppy):
        super().__init__(name,weight,country,feeding_period)
        self.count_puppy=count_puppy

    def behaviour_d(self):
        print("Я умею гавкать!")


print("____Ex 1____")
fish=animals("Рыба",0.5,"Россия")
print("Мое название -", fish.name)
fish.behaviour()
print()

elephant=mammals("Слон",4000,"Южная Африка","2 mounth")
print("Мое название -", elephant.name)
elephant.behaviour()
elephant.behaviour_m()
print()

Tom=human("Том",80,"Америка","6 mounth","English")
print("Мое имя -", Tom.name)
Tom.behaviour()
Tom.behaviour_m()
Tom.behaviour_h()
print()

Kaila=cat("Кайла",8,"Великобритания","1 month",5)
print("Мое имя -", Kaila.name)
Kaila.behaviour()
Kaila.behaviour_m()
Kaila.behaviour_c()
print()

Cherry=dog("Черри",12,"Россия","1 month",3)
print("Мое имя -", Cherry.name)
Cherry.behaviour()
Cherry.behaviour_m()
Cherry.behaviour_d()
##везде можно узнать любую другую информацию 

print("____Ex 2____")
class human_ex2():
    def __init__(self,name,weight,height,age):
        self.name = name
        self.weight = weight
        self.height=height
        self.age=age


class student(human_ex2):
    def __init__(self,name,weight,height,age,course,count_of_homework):
        super().__init__(name,weight,height,age)
        self.course=course
        self.count_of_homework=count_of_homework

    def __eq__(self,student) :     
        if student.count_of_homework>self.count_of_homework:
            print(student.name,"выполнила больше домашних работ,чем",self.name)
            return("__Анализ завершен__")
        if student.count_of_homework<self.count_of_homework:
            print(student.name,"выполнила меньше домашних работ,чем",self.name)
            return("__Анализ завершен__")
        else:
            print(student.name,"и",self.name,"выполнили одинаковое кол-во домашних работ")
            return("__Анализ завершен__")
        

Mary=student("Маша",60,168,20,3,26)
Veronika=student("Вероника",50,155,20,3,20)
print(Mary.name,"сделал(а)",Mary.count_of_homework,"домашних работ")
print("____Ex 3____")
print(Mary.__eq__(Veronika))