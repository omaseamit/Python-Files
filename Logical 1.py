
'''
n1= ['Done','Good','Great','Nice']
n2=n1
n3=n1[:]

n2[0]='Ahad'
n3[1]='Rohit'

list1=['Done','Good','Great','Nice','Ahad','Good','Great','Nice','Done','Rohit','Great','Nice']

sum=0
for i in (n1,n2,n3):
    print(i)
    if i[0]=='Ahad':
      sum=sum+3
    if i[1]=='Rohit':
      sum=sum+10

print(sum)

# check prime number
n=int(input('enter no'))

if n>1:
    for i in range(2,n):
         if (n%i==0):
              print(n,'is not prime')
              break

            
    else:
        print(n,'is prime no')

else:
    print('not prime')
    
#print prime no

num=int(input('enter any no'))

list1=[]
for i in range(2,num+1):
    
    for j in range (2,i):
        if i%j==0:
            
            break

    else:
        (list1.append(i))

print(list1)






#palendrome
# for word
s=input('enter any word :- ')

a=s[::-1]

if s==a:
    print('word is palandrome')

else:
    print('word is not palandrome')

#for number
i= int(input('enter any number -:'))
x=i
rev=0
while(i>0):
    rev=(rev*10)+i%10
    i=i//10     
if rev==x:
    print('number is palandrome')
else:
    print('number is not palandrome')

#method 2
n=input('enter number')
b=str(n)
c=b[::-1]
if n==c:
    print('number is palindrome')
else:
    print('number is not palindromr')


# lambda having number af afrguments but only one expression
x=lambda a,b : a+b
print(x(5,5))



#ASCII AMERICAN STANDAR CODE FOR INFORMATION INTERCHANGE
x=input('enter letter')
print(ord(x))

y=int(input('enter number'))
print(chr(y))


# fiboncci series 
n= int(input('enter no'))

x=0
y=1
z=0

while z<=n:
    print(z)
    x=y
    y=z
    z=x+y

# right angle print
a=int(input('Enter a number: '))
for i in range(a):
    for j in range(i+1):
        print('#',end=" ")
    print()


#print total no of vovales

word=(input('Enter any word :- '))
a1=word.count('a')
e1=word.count('e')
i1=word.count('i')
o1=word.count('o')
u1=word.count('u')

total=(a1+e1+i1+o1+u1)
print('total no of vovules are:-',total)


word=input('word')
count=0
v=['a','e','i','o','u']
for char in word:
    if char in v:
        count=count+1
        
print(count)

#sum of 1to n numbers
num=int(input('no'))
count=0
for i in range(num+1):
    count=count+i
    
print(count)

# sum of digit of number
num=(input('no'))
count=0
for i in str(num):
    count=count+int(i)
print(count)

#sum of square of all digit
num=(input('no'))
count=0  
for i in str(num):
    count=count+(int(i)**2)
print(count)

#armstrong no (370)
num=(input('no'))
x=len(num)
count=0  
for i in str(num):
    count=count+(int(i)**(x))
a=str(count)
if (num==a):
    print('the no is armstron no')
else:
    print('not armstrong')


# perfect no
num=int(input('no'))
count=0
for i in range(1,num+1):
    if num%i==0:
        count=count+i

        if count==num:
            
            print('no is perfect')
            break
else:
            print('not perfect')
    

# factorial

n=int(input('no'))
facto=1
if n<0:
    print('negative no has no factorial')
elif n==0:
    print('0 has factorial 1')
else:
    
    
    for i in range(1,n+1):
        facto=facto*i
    print(facto)


# factors of givin no

n=int(input('no'))
list1=[]
for i in range(1,n+1):
    if n%int(i)==0:
        list1.append(i)
print(list1)



# sum of even digit multiplication of odd digit of given no
n=int(input('no'))
count=0
mult=1
for i in str(n):
    if int(i)%2==0:
        count=count+int(i)
    elif int(i)%2!=0 :
        mult=mult*int(i)
print(count,mult)

# sum and multi of all element in list
list1=[1,2,3,4,5]
count=0
multi=1
for i in list1:
    count=count+i
    multi=multi*i
print(count,multi)

#square all elenent in list

list1=[1,2,3,4]
for i in list1:
    i=i**2
    list1.append(i)
print(list1)

#random function
import random
a=random.randint(0,5)
print(a)
'''













   























    





























































































