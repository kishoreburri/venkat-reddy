import re

pattern = '^b...s$'
testing_string='baths'

result = re.match(pattern,testing_string)

if result:
    print('search succesful')
else:
    print(' search unsuccesfull')

import re
a = '^m....y$'
b='monkeey'

result = re.match(a,b)

if result:
    print('matches')
else:
    print('ummatch') 

## square matches

a="kishmore mike"
s=re.match(r'[mal]',a)
if s:
    print('match')
else:
    print('unmatch')  

a=16
while a>18:
    print('true')
else:
    print('false')                     

a= 'hello mike howare you'
c=re.search(r'[bbk]',a)
if c:
    print('search succesful')
else:
    print('unsuccesfull')    


## in this example it search before space  only

a='hello mike'
s=re.match(r'[hel]',a)
if s:
    print('match')
else:
    print('unmatch')      

### in thos example it seach entire string
## search() function use
a='hello kishore how are you'
r=re.search(r'[zzu]',a)
if r:
    print('match')
else:
    print('unmatch')         
###
a='hello kishore how are you'
r=re.findall(r'[zzu]',a)
print(r)      

### in this example it shows search characters in the output
### findall() function use
a='hello mike i am usa'
r=re.findall(r'[hica]',a)
print(r) 

## .period function

a='abc'
r=re.findall(r'..',a)
print(r)

## ^ -caret
### search the first letter

a='kishore'
b=re.search(r'^k',a)
if b:
    print('fetch succesfull')
else:

   print('unsuccesful')    

## $ use for search last charcter is matches or not

a='leg'
b=re.findall(r'kig$ ',a)
if a:
    print(' l search') 
else:
    print('l not found')         

### * is follows the before number

a='mian'
b=re.search(r'ma*n',a )
if b:
    print('t')
else:
    print('f')            