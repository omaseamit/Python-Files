#loop
'''
#simple for loop
list1=[1,2,3,'a','b','c','d']
for i in list1:
       print(i)

colors = ['red','green','pink']
for color in colors:
       print(color,end=" ")


       
#add all elements in list
d=0
list1=[]
numbers=[1,2,3,4]
for i in numbers:
       d=d+i #d+=i (shortcut)
       list1.append(d)
print(list1)


#using range function
print("by using range function")

for i in range(10):
       print('1.',i)      

for i in range(2,9):
        print('2.',i)

for i in range(0,20,3):
        print('3.',i)

'''
##nested for loop

#a=[1,2,3,4,]
#b=['a','b','c','d']
for i in range (5):
    for j in range (5):
        if j==0 or j==4:
         print(i,j,end=" ")
        else:
          print(' ',end=" ")
    print()

### right angle triangle

for i in range (5):
    for j in range (5):
        if i==0 or j==0 or i==4 or j==4:
         print('#',end=" ")
        else:
          print(' ',end=" ")
    print()

### triangle

for i in range (5):
    for j in range (i+1):
         print('#',end=" ")
        else:
          print(' ',end=" ")
    print()
### diagonal
    


### method 2
 
a=int(input('Enter a number: ')) 
for i in range(a):
     for j in range(i+1):
        print("#",end=" ")
     print()


### upper triangle

a=int(input('Enter a number: ')) 
for i in range(a):
     for j in range(i-1):
        print("#",end=" ")
     print()













    

