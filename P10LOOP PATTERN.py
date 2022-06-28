#1.take year as an input from user print the message
#if that year is leap year or not.

a=int(input('chose a year:'))
if a%4==0:
     print(a ,'is a leap year')
else:print(a ,'non leap year')


#2.take unit as input from user and print the bill accordingly
#for first 100 units - no charge,than for each 100 units Rs 5 per unit flat.
#0-100 unit is Rs 0
#100-200 unit is Rs 5
#example:if user gives 102 units,
#than unit should be 5 and bill should Rs 10.


a=int(input('enter the units:'))
d=int(a/100)

if d<1:
    print('1.No charges')
else:
    print('1.Your 1unit = Rs',d*5,'and total bill is ',(a-100)*(d*5))



#3.print the elements in the list using for loop
colors =['red','blue','white','orange']
for color in colors:
       print(color,end="    ")
print()


#4.check if white is in the list,if yes print a message as "found"
#and at what index.(with loop and without loop)
c=['red','blue','white','orange']

# without loop
if 'white' in c:
   print(c.index('white'),' found ')
else:print('white not found')

#with loop
for i in c:
    if i=='white':
       print(c.index('white'),'found')



#pattern
# to print in a straight line 
a=5
for i in range (a):
     for j in range (i,a):
            print('#',end=" ")
print()


# to print in a line below
a=5
for i in range (a):
     for j in range (i,a):
            print('#',end=" ")
            print()

# to print + pattern
a=5
for i in range (a):
    for j in range (a):
         if i==2 or j==2:
           print('#',end=" ")
         else:
          print('  ',end = " ")
    print()



# to print in a right angle trangle
a=5
for i in range(1,a+1):
      for j in range(i,i+1):
           print(""*(a-1)," * "*j)


# alternative to print in a right angle trangle of any size
a=int(input('Enter a number: '))
for i in range(a):
    for j in range(i+1):
        print("#",end=" ")
    print()

