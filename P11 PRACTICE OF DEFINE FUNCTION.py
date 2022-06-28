#1.define a function to subtract 2 numbers

def sub(x,y):
    a=x-y
    print(a)  
sub(3,6)


#2.define a function to divide 2 numbers
def divide(x,y):
    a=x/y
    print(a)   
divide(3,6)


#3.define a function to multiply 3 numbers
def multiply(x,y,z):
    a=x*y*z
    print(a)  
multiply(3,6,2)


#4.define a function to add and sub two different numbers.
def add_sub(x,y):
    c=x+y
    d=x-y
    return c,d
f1,f2= add_sub(10,2)
print(f1,f2)

#or

def add_sub(x,y):
    c=x+y
    d=x-y
    print(c,d)
add_sub(5,4)

#5.fruits = ["apple", "banana", "cherry"] write a function name it 'code1',
#to return apple otherwise print not found,
#use code1 on nuts = ["mongo", "banana", "cherry","apple"]

fruits = ["apple", "banana", "cherry"]
nuts = ["mongo", "banana", "cherry","apple"]
def code1(name):
      if 'apple' in name:
          print('apple is found')
      else:
         print('not found')
code1(nuts)


#6.fruits = ["apple", "banana", "cherry"] write a function to return
#apple and banana otherwise print not found. use this function on
#greatfruits = ["pineapple","apple","greenbanana", "banana", "cherry"]

fruits = ["banana","cherry"]
#greatfruits = ["pineapple","apple","greenbanana", "cherry"]
#new= ["apple"]
def code1(name):
    
    if "apple" and "banana" in name:
       print('apple and banana') 
    elif "apple" in name:
       print('not found')
    elif "banana" in name:
       print('not found')

    else: 
       print("not found")
code1(fruits)


#code1(greatfruits)

#code1(new)


#7.print square of a number by user, define function for it
n=int(input('Enter a number: '))
def square(n):
    a=n*n
    print('The square of ',n,' is ',a)

square(n)

#8. sort this list and define function for it
list1 = [589.36, 237.81, 230.87, 463.98, 453.42]
def sort_code(name):
    sorted_list=[]
    for i in range (len(name)):
        a=min(name)
        sorted_list.append(a)
        name.remove(a)
    print(sorted_list)
    list1.extend(sorted_list)
sort_code(list1)


#9.define a function which returns the number multiplied by 5

def multi(n):
    a=n*5
    return a
f1=multi(5)
print(f1)


#10.add new month to the list

month = ['Jan', 'Feb', 'Mar']
months = ['January', 'February', 'March']


def usb(m):
    m=input('type month which you add in list')
    months.append(m)
    print(months)
usb(month)       


#11.write a function to return square of list
list1=[2,3,6,8]


def squ(list1):
    a=list1[0]*list1[0]
    b=list1[1]*list1[1]
    c=list1[2]*list1[2]
    d=list1[3]*list1[3]
    print(a,b,c,d)

squ(list1)

#12.define a function to return second largest from the list
a=[55,23,78,13,21,29,8]

def second_largest_no(a):
    a.sort()
    
    print('second largest number in list a is',a[-2],)

    
second_largest_no(a)  


#13. print hello and user defined name

def welcom(name):
    print('hello',name)
    
welcom('amit')

#14.revese list and funtion for it
a=[55,23,78,13,21,29,8]

def reverse_list(a):
    a.reverse()
    print('reverse list',a)
    
reverse_list(a)
    
#15.write a function to print table of 2
    

def table_of_2_is(a):
    print('Table of 2 is:')
    
    for i in range(2,22,2):
        print(i)

table_of_2_is(a)

































