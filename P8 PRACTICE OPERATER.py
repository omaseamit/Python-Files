##Practice Operation

#1.take two int inputs from the user, print greatest among them

num1=int(input('Enter 1st no:'))
num2 = int(input('Enter 2nd no:'))
if num1 >= num2:
    print(num1 ,'is greater ')
else:
   print(num2 ,'is greater ')

 #2.ask the user their Marks and grade accordingly
#Below 25 - F
#25 to 45 - E
#45 to 50 - D
#50 to 60 - C
#60 to 80 - B
#Above 80 - A

MARKS=int(input('marks?:'))
num=MARKS
if MARKS <25:
    print(num,' Grade F ')
elif MARKS<45:
    print(num,' Grade E ')
elif MARKS<50:
    print(num,' Grade D ')
elif MARKS<60:
    print(num,' Grade C ')
elif MARKS<80:
    print(num,' Grade B ')
else: print (num,' Grade A')

#3.take age as input from 3 users check who is oldest among them
a=int(input('Enter your age?:'))
b=int(input('Enter your age?:'))
c=int(input('Enter your age?:'))

if a>b and a>c:
    print(a ,'is  senior ')
elif c>a and c>b:
    print(c ,'is senior ')
elif b>a and b>c:
    print(b ,'is senior ')    
else:print()


    

a=int(input('a enter age1 '))
b=int(input('b enter age2 '))
c=int(input('c enter age3 '))

if a>b and a>c:
    print(a ,'is  senior ')
elif c>a and c>b:
    print(c ,'is senior ')
elif b>a and b>c:
    print(b ,'is senior ')    
else:print()


#4.take age as input from 3 users check who is youngest among them


a=int(input('a enter age1 '))
b=int(input('b enter age2 '))
c=int(input('c enter age3 '))

if a<b and a<c:  
 print(a,'is younger')
elif b<a and b<c:
 print(b,'is younger')
elif c<a and c<b:
 print(c,'is younger')
else:print()


#5.take salary and no of service in a company as input from the user
#company decided to give bonus of 5% to employee, 
#if his/her year of service is more than 5 years
#print total amount and bonus amount.

salery=int(input('salery?:'))
exp=int(input('exp?:'))
if exp>5:
    print('new salery is ',salery*5/100+salery,'bonus is',salery*5/100)
else: print ('Your service is less than 5 yrs hence you are not applicable for bonus')



#6.Ask user for quantity of a product he purchased,
#A shop will give discount of 10% 
#if the cost of purchased quantity is more than 1000
#Suppose, one unit will cost 100.
#Judge and print discount for user and total cost.

user=int(input('total quantity ?:'))
if user>10:
    print('your discount is', user*100*0.1, ' :-so total cost is ', user*100-user*100*0.1)
else: print ('not applicable for discount')




#7.take Number of classes held and Number of classes attended and medical
#fitness as input from user, Allow him to attend exam if percentage 75. 

a=int(input('total no of classes held ?:'))
b=int(input('total no of classes attended ?:'))
c=int(input('medical fitness ?:'))
if ((b/a*100)+(c))/2 >=75:
    print('your are allowed to attend the exam')
else: print ('not allowed to sit for exam')


#8.take input as month from user(take only first six month)
#output should be no. of days in that month

a=input("Enter Month :-")
month1=['jan','mar','may']
month2=['apr','june']

if a in month1:
    print(a, " has 31 Days")
elif a in month2:
    print(a, " has 30 Days")
else :print(a, " has 28 days in a non Leap year and 29 Days in a Leap year")


#9.take 10 inputs from the user, print greatest among them.
a=int(input('enter your age:'))
b=int(input('enter your age'))
c=int(input('enter your age:'))
d=int(input('enter your age:'))
e=int(input('enter your age:'))
f=int(input('enter your age:'))
g=int(input('enter your age:'))
h=int(input('enter your age:'))
i=int(input('enter your age:'))
j=int(input('enter your age:'))

set1 = {a,b,c,d,e,f,g,h,i,j}
print('maximum value is',max(set1))


