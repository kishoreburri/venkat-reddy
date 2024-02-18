#import calendar
#


class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        return self
    hello=display(f'my self.name = kishor self.age  = 88 ');
    print(hello)    

class Car:

    def __init__(self,model,price,color):
        self .model = model
        self.price = price
        self.color = color

    def display(self):
        print('my "+self.model+" is red')

    def write(self):
        print('my  "+ self.price+" is white')

car_1=Car('ford',888899,'red')
car_2=Car('bmw',8888999,'black')

#print(car_1)  
print(car_2.model)
#print(car_1.price)  
#print(car_1.color)


car_2.write()
car_2.display()


### oops basic syntax

class Student:

    def __init__(self,name,age,number):
        self.name=name
        self.age=age
        self.number=number
    def display(self):
        print("my name is :",self.name)

    def greetings(self):
        print('wel come to python  totorial and phone number is :',self.number)

    def age(self):
        print('my age is:',self.age)    

Sir=Student('kishore',25  ,8309801856)            
print(Sir.name)
print(Sir.age)
print(Sir.number)
              
Sir.display()
Sir.greetings()

class Dog:

    def one_add(self,x,y):
        return x + y
    
f=Dog()
print(f.one_add(6,9))

class Car:
    def __init__(self,brand,price,color):
        self.brand = brand
        self.price=price
        self.color = color

    def display(self):
        print("my new  brand is:", self.brand)
        pass

    def show(self):
        print('my car color is:', self.color)

Car_1=Car('BMW',8888878,'red')
print(Car_1.brand)
print(Car_1.price)
print(car_1.color)

Car_1.display()
Car_1.show()


###  

class Student:

    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade

    def get_grade( self):
        return self.grade
    
class Course:

    def __init__(self,name,max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_students(self,student  ):
        if len(self.students) < self.max_students:
          self.students.append(student)  
          return True
        
        return False  
    
    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()

        return value /  len(self.students)
s1=Student('tom',45,78)
s2=Student('line',3,67)
s3=Student('mine',44,99)

course = Course('science',23)
course.add_students(s1)
course.add_students(s2)
print(course.get_average_grade())
    
### inheritance

class Pet:
    def __init__(self,name,age ):
        self.name =name
        self.age = age   
    def display(self):
        print(f"i am {self.name} and i am {self.age } years old")

class Dog(Pet): 
    def speak(self):
        print('bark')

class Cat(Pet):
    def speak(self):
        print('meow')

p=Pet('mile',16)
print(p.name)
p.display()  
c = Dog('nike',66)
c.speak()
d=Cat('take',55)
d.speak()





class Student:

    def __init__(self,name,age,number):
        self.name = name
        self.age = age
        self.number = number

    def display(self):
        print(f" my name is {self.name} and my age {self.age} is  and my phone numner is {self.number}"); 
    
class Course:
    def __init__(self,name,price):
        self.name=name
        self.price=price

sir=Student('kishore',88,9849265124)
print(sir.name)
print(sir.age)
print(sir.number)
sir.display()    
madam=Course('science',9999)


class Bikes:

    def __init__(self,brandname,year):
        self.brandname = brandname
        self.year=year

    def topspeed(self,topspeed):
        return "{} topspeed is {}".format(self.brandname,self.topspeed)
    def type(self):
        return "{} is geared bike".format(self.brandname)    

bmw = Bikes('bmw',220) 


### inheritance

class Animal:
    def Sound(self ):
        print('meow')

class Cat(Animal):
    def meow(self):
        print('cat meows')

class Dog(Cat):
    def Bow(self):
 
     print("barks")     
     
d=Cat()
#d.Sound()
d.meow()

f=Dog()
#f.Sound()
f.meow()


## multilebvel inheritance

class Animal:
    def Cat(self):
        print('it makes sound meows')

class Hen(Animal): 
    def Pot(self):
        print("it makes sound beck beck")

class Man(Hen):
    def Speak(self):
        print('man speak loudly')

m=Man()
m.Speak()
m.Cat()
m.Pot()

### polymorphism



class Parrot:
    def fly(self):
        print('parrot it can fly')

    def swim(self):
        print("parrot can't swim")

class Peguin:
    def fly(self):
        print("piguin can't fly")        

    def swim (self):
        print( "pegiun can swim") 

def flying_test(bird):
    bird.swim()       

blue = Parrot()
black=Peguin()


flying_test(blue)
flying_test(black)


class Dog:
    def dog(self):
        print('dogs make sound loudly ')

    def pig(self):
        print('pig make sound slowely')  

class Hen:
    def dog(self):
        print('hen makes beck beck')

    def pig(self):
        print('it makes sound slowely')

def test(Animal):
    Animal.pig()

d=Dog()
h=Hen()

test(d)
test(h)

class Sir:
    def Son(self):
        print("son listen Sir words carefully")

    def Student(self):
        print('student never listen sir words carefully')  

class Father:
    def Son(self):
        print('son listen father words carefully')

    def Student(self):
        print('student doesnot listen words carefully')

def testing(good):
    good.Student()

s=Sir()
f=Father()

testing(s)
testing(f)

### encapulsulation

class Car:
    def __init__(self):
         self. __maxprice = 1000000
         self.__minprice = 600000

    def Sell(self):
        print("selling price:{} minimum price :{}".format(self.__maxprice,self.__minprice))

    def SetMaxPrice(self,price,minprice):
        self.__maxprice = price
        self.__minprice=minprice

c = Car()
#c.Sell()
c.SetMaxPrice(500000,400000)
c.Sell()


### absraction 






                       
  
    


