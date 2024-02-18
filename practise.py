print('hello welcome',sep="")
print('hi')
a=1+2j
print(type(a))


l1=['apple','mango','orange']
l2=l1[-1]
print(l2)

list=[1,2,4,5,8]
print(list[0:3])

l5=['kishore','hari','mani','mike']
print(l5[0:2])
number = 17
def check_prime():
    if number >1:
        print('none')
        if number %2 ==0:
            print('true')
    else:
        print('false')
check_prime()

di=['tiger','lion','monkey','deer']
dl=di[-3:3]
print(dl)

a=10
b=14
a,b=b,a
print(a,b)

print(a)

a='kishore'
b='venkat'
a,b=b,a
print(a,b,sep='')

def absolute_number(number):
    if number >=1:
        return number
    else:
        return -number
print(absolute_number(5))
print(absolute_number(-9))    

s="kishore"
def reverse(s):
    result =""
    for i in s:
        result = i + result
    return result  
k = reverse("kishore")
print(k) 

k='venkat'
m="".join(reversed(k))
print(m)

k='monkey'
l=k[::-1]
print(l)

g={"school":'student',"teacher":'parent'}
g["teacher"] = "school"
print(g)

def add_number(a,b):
    return a + b
print(add_number(6,9))

k=add_number(9,3)
print(k)
n=lambda x,y : x +y
print(n(5,9))

### how to swap two numberss

a=12
b= 18
a,b = b,a
print(a)

def swap(num1,num2):
    num1,num2=num2,num1
    return num1,num2
swap(3,8)

### check is prime are not

def check_prime(num):
    if num %2 != 0:
        print("prime")
    else:
        print(' not prime')
check_prime(19)            

#### we have to check natural number

### which only contains 2 factors 11 and itself

num = 19
count = 0

if num >1:
    for i in range(1,num+1):
        if (i % num) ==0:
            count = count+1

    if count == 2:
        print('prime')

    else:
        print('not prime')    
         
### check prime
        
def check_prime(number):
    if number %2 != 0:
        print('prime')
    else:
        print('not prime')
check_prime(19)     

### find the factorial number

def find_factorial(num):
    for i in range(1,num+1):
        num = num * i
    
find_factorial(9)   

num = 5
fact = 1
for i in range(1,num+1):
    fact= fact *i
    print(fact)


### find factorial of 9
    
num = 4
fact = 1
for i in range(1,num+1):
    fact = fact * i
    print(fact)
                       
                                               ### it is natural number

def find_factorial(num):
    if (num == 0 or num ==1):
        return 1
    else:
        return num * find_factorial(num - 1)
print(find_factorial(6))  

def num_of_factorial(number):
    if (number == 0 or number == 1):
        return 1
    else:
        return number * num_of_factorial(number - 1)
print(num_of_factorial(6))    


#arrr = [3,7,9,5]
### output should be [9,49,81,25]

def square_elements(arr):
    squared_arr = [x**2 for x in arr]
    return squared_arr

arr = [3, 5, 7, 9]
output = square_elements(arr)
print(output)


def square_root(arr):
    m=[]
    for i in arr:
        m.append ( i ** 2)
    return m
arr = [3,5,7,9] 
output = square_root(arr)
print(output)    


def whole_square(arr):
    square = [x ** 2 for x in arr]
    return square
arr = [9,8,7,6]
op=whole_square(arr)
print(op)

def is_palindrome(s):
    # Convert the string to lowercase and remove spaces and punctuation
    s = ''.join(char.lower() for char in s if char.isalnum())
    # Check if the string is equal to its reverse
    return s == s[::-1]

# Test cases
print(is_palindrome("racecar"))  # Output: True
print(is_palindrome("hello"))     # Output: False
print(is_palindrome("A man, a plan, a canal, Panama"))  # Output: True

def check_string_is_palidrome(st):
    st = ''.join(x.lower() for x in st if x.isalnum())
    return st == st[::-1]
st = 'racecar'
k=check_string_is_palidrome(st)
print(k)

### check a string is palidrome are not

def check_string(string):
    string = ''.join(x.lower() for x in string if x.isalnum())
    return string == string[::-1]
string='pops'
l=check_string(string)
print(l)

def multiple_of_three(integers):
    k=[]
    for j in in*


