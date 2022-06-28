## operators

#arithmetic progression
a=10
b=2
print('Addition:',a+b)
print('Subtraction:',a-b)
print('Multyiplication:',a*b)
print('Division:',a/b)
print('Rmainder:',a%b)
print('Exponential:',a**b)

# assignment operators
print()
print('assignment operators')
a=5
add,sub,mul,div,rem,expo=0,0,0,1,1,1

add = add + a
add += a
print('1.',add)
sub -= a
print('2.',sub)
mul *= a
print('3.',mul)
div /= a
print('4.',div)
rem %= a
print('5.',rem)
expo **= a
print('6.',expo)

# comparission operators
print()
print('comparission operators')
a=5
b=10
#true if equal
print('1.',a==b)

#true if not equal
print('2.',a!=b)

#true if a is greater than b
print('3.',a>b)

#true if b is greater than a
print('4.',a<b)

#true if a is greater than or equal to b
print('5.',a>=b)

#true if b is greater than or equal to a
print('6.',a>=b)

# logical operators
print()
print('logical operators')

#if value = 0 its always false
#if 1 or greater than 1 then true
a=5
b=10

#true if b is greater than or equal to a
print('5.',a<=b)

 #IF value=0 its always false
#if 1 or greater than 1 then true
a=5
b=0
print('1.',a and b)

#true if either 1 is true
print('2.',a or b)
#return opposites of value
print('2.',not a)
print('4.',not b)


#identity operator
print()
print('identity operator')

a=[1,2,3]
b=[2,3,4]
#true if a and b are equal
print('5.',a is b)

#true if a and b are not equal

print('6.',a is not b)

#true if 2 is in b
print('7.',2 in a)

#true if 2 is not in b
print('8.',2 not in b)
