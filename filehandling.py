### file handling in read process
import os
file=open("c:/Users/reddy/OneDrive/Desktop/filehandlings.txt" ,   "r")
print(file.read())
file.close()

### file handling in condition process
##(e.g= 8)

import os
file=open("c:/Users/reddy/OneDrive/Desktop/filehandlings.txt" ,   "r")
print(file.read(8))
file.close()

### in this process file read line by line process

import os
file=open("c:/Users/reddy/OneDrive/Desktop/filehandlings.txt" ,   "r")
print(file.readline())
file.close()

## in  this step file reads by line by line process 
## it gives an array type  with \\n 

import os
file=open("c:/Users/reddy/OneDrive/Desktop/filehandlings.txt" ,   "r")
print(file.readlines())
file.close()

## write process

import os
file=open("c:/Users/reddy/OneDrive/Desktop/filehandlings.txt" ,   "w")
print(file.write('nse talent sprint'))
print(file.write('wel'))

file.close()

### creatings a new files
#

### to remove entire process

#


## to check if possible deleted or saved

import os

if os.path.exists("c:/Users/reddy/OneDrive/Desktop/filehandlings1.txt"):
    os.remove("c:/Users/reddy/OneDrive/Desktop/filehandlings1.txt")
else:
    print('file is not exist with name filehandlng1')    

## to print in line by line
    
### practise
    
## to create a file
    
#


file.close()

import os
file = open("c:/Users/reddy/OneDrive/Desktop/filehandlings20.txt","r")
print(file.read())
file.close()
#
 
import os
file=open("c:/Users/reddy/OneDrive/Desktop/filehandlings50 .txt","a")
print(file.write(" hello mike how are yoy"))
file.close()

import os
file = open("c:/Users/reddy/OneDrive/Desktop/filehandlings50.txt","r")
print(file.read())

import os 
file = open ("c:/Users/reddy/OneDrive/Desktop/filehandlings55.txt","r")
print(file.read())


l=[1,2,3]
l.append[4,5]
print(len(l))