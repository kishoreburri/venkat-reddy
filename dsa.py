li=[3,8,9,10]
k = li[1:-1]
print(k)

k="kishore"
m=k[1::-1]
print(m)

l=['kishore','hari','karma']
m=l[1::-1]
print(m)

l=['kishore','hari','karma']
n=l[2]
print(n)

l=['kishore','hari','karma']
l.append([2,'mari'])
print(l)

l=['kishore','hari','karma']
l.extend([2,4,'d'])
print(l)

l=['kishore','hari','karma']
l.insert(-1,'venkat')
print(l)
m= ['kishore', 'hari', 'venkat', 'karma']
#del m[2]
m.insert(2,'venkat')
print(m)

m = ['kishore', 'hari', 'venkat', 'venkat', 'karma']
del  m[2]
print(m)

b =['kishore', 'hari', 'venkat', 'venkat', 'karma']
b.insert(3,'kishore')
print(b)

print(b)

del b[3]
print(b)

c=b.pop(-2)
print(c)
print(b)

b.remove('kishore')
print(b)

print(b)



z= ['kishore', 'hari', 'mangamma', 'kankamma', 'yashammma', 'karma']
z[1:4:2]
print(z)



squares = [x**2 for x in range(10)]
print(squares)

### error handling in pythonns

a=10
b='kishore'
try:
    print(a + b)
except:
    print('a string and integer cannot add')
else:
    print('ohh god')    

for i in range(10):
    if i == 7:
        continue
    print('break',i)  

dict = {'name':'kishore','age':24,'gender': 'male'}
dict['corse'] = 'python'
print(dict)

n=[1,2,44,55,66,12,77,13,88]
n.sort()
print(n)

#### slicing

li=[2,3,5,6,7,8,9,10,3,]
k=set(li)
print(k)

li=[2,3,5,6,7,8,9,10,3,]
m=li[0:10]
print(m)

l=[23,29,30,34,38,42]
g=l[1:5]
print(g)

l=[23,29,30,34,38,42]
g=l[1:-1:3]
print(g)


l=[23,29,30,34,38,42,18,15,19]
l.sort(reverse=True)
### sorted function
print(l)
k = sorted(l)
print(k)

### how to find the index of particular element in index
l=[23,29,30,34,38,42,30,34]
k = l.index(38)
print(k)

### how to use count menthod in list duplicate

r=l.count(30)
print(r)
#### to count the number of elements in list
p=len(l)
print(p)

t=(8,9,10)
m=t.index(10)
print(m)
    
a="kishore"
b="reddy"
print("my name is",a ,"and my surname is" ,b ,sep=" ")