#1 print 1,2, from list 'a' using index
a=[1,2,3,4,5]

print(a[0:3])



#2.print 1,2,3 from 'a' using for loop
a=[1,2,3,4,5]
for i in a :
    if i==4:
        break
    else:print(i,end="  ")
print()

#3.print multiplication of all the numbers in list using for loop 
a=[1,2,3,4,5]
mul=1
for i in a:
    mul=mul*i
print(mul)


#4.print table of 2 using range

for i in range(2,21,2):
    print(i)

#5.print squares of all elements of list 'a', in the list
a=[1,2,3,4,5]
for i in a:
    print(i*i,end=' ')
print()


#6.take an int input from user,print the factorial of that number.
#(the product of an integer and all the integers below it)


n=int(input('no=: '))
fact=1
for i in range (n):
            fact=fact*(i+1)
print('factorial of given no is: ',fact)


#7.Print 1 to 30,for multiple of, 
# 3 print "three"  
# 5 print "five"  
# 15 print "fifteen" 

for i in range(1,31):
    if i%15==0:
     print(i,'fifteen')
    elif  i%5==0:
     print(i,'five')
    elif  i%3==0:
     print(i,'three')
    else:
         print(i)


#8.print prime numbers till 50


for i in range(1,51):
    for j in range(2,i):
        if i%j==0:
             break
    else:
        print(i)



