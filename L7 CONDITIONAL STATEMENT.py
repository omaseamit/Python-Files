#7  CONDITIONAL STATEMENT


# conditional statement

num=3
if num > 0:
    print(num,' is positive ')
num = -1
if num > 0:
    print(num,' is positive ')
else:
    print(num,' is negitive ')

# program checks if the no is positive or negitive
# and display an appropriate message

num=5
if num >= 0:
    print(num,' is positive ')
else:
    print(num,' is negitive ')

# check the no is positive , negitive or zero
#num=2
#num=0
num= -3
if num > 0:
    print(num,' is positive ')
elif num== 0:
    print(num,' is zero ')
   
else: print (num,' is negitive ')

# the symbol " % " , in python is called the modulo. it returns reminder
#2%2 = 0
#3%2 =1

# nested if else
n=5
if n>=0:
    if n==0:
        print ('no is zero')
    else:
        print('no is positive')
else:
    print('no is negitive')
   
