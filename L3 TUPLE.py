
##tuple

#tuple is same as list but they are not mutable
#in tuple we use "()" brackets

#1 initializing tuple
mytuple=()
mytuple1=tuple()
print(mytuple)
print(mytuple1)

#2 creating a tuple
tuple1=(1,2,3)
tuple2=tuple(('helo','welcome',3))
print(type(tuple2))
print(tuple1)
print(tuple2)

tuple3='example',6
print(tuple3)
print(type(tuple3))

#3 print tuple 1
tuple1=(1,2,3)
print(tuple1)

#4 print 'helo','all'
tuple1=('helo','all')
print(tuple1)
tuple2=tuple(('helo','welcome','all','here'))
print(tuple2[0:3:2])

#or
a=(tuple2[0])
b=(tuple2[2])
print(a,b)

#5 print '1' from tuple 3
tuple3=(1,2,3,['new','string','1'])
print(tuple3[0])

#6 print tuple 2
tuple2=tuple(('helo','welcome','all','here'))
print(tuple2[:])

#7 print 'string' from tuple3
tuple3=(1,2,3,['start','done','string','end'])
print(tuple3[3][2])

#8 replace 'start' with  'change'
tuple3=(1,2,3,['start','done','string','end'])
tuple3[3][0]='change'
print(tuple3)

#9 count 5 in tuple 4
tuple4=(1,2,3,('new','string',9,9,9),1,1,5,5)
print(tuple4.count(5))

#10 find index of list in tuple 4
tuple4=(1,2,3,['new','string',9,9,9],1,1,5,5)
print(tuple4.index(['new','string',9,9,9]))











