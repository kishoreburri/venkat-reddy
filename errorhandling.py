try:
    a=19
    b=0
    c=a/b
except:
    print('it cannot divisible')    

try:
    a=int(input('enter the number:'))
    b=int(input('enter the number:'))   
    c=a/b
except:
    print('not a problem')    

a=80
b=0
try:
    print(a/b)
    print("new line")
except ZeroDivisionError:
    print('it cannot divisible')
print("completed ")        


a=10
b=11

try:
    c= a + b
    print(c)
except:
    print('not a problem')    
    
print('string and integer donot concatate')   

a=99
b="kishore"
try:
    print(a + b)
    print('leave it')
except:
    print('take series')    


a=10
b=12
try:
    print(a + b)  
except:
    print('not a problem')    

a=["kishore","hello"]
b=a.append(['mike'])  
print(b)    

l1=["hello",'kishore']
l1.append('mike')
print(l1)