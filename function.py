def greeting():
    print('hello marry')
    print('how are you')
greeting()
greeting()
greeting()

def my_name():
    print('my name is :',"kishore")
my_name()     

def addition(x,y,z):
    return x+y+z
a=addition(2,4,5)
print(a)

### write a function states that a list is sends to argents while functing calling

def my_list(new_list):
    for old_list in new_list:
        print(old_list)
my_list([2,4,6,88,8])        

def dunction(*a):
    return a
b=dunction(7,9,10)
print(b)

def function(**a):
    return a
c=function(name="kishore",age=21,height=5.11)
print(c)


def hello(**dict):
    return dict
d=hello(name="kishore",age="21")
print(d ,sep ="----- ")

