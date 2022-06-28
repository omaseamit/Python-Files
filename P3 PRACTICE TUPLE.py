
### Practice
##1. initialize empty tuple
##2. create a tuple of few integer values (dont use tuple function)
##3. create a tuple of few string values.
#new1=(1,2,3,4,'welcome')
#new12=tuple((1,2,2,3,4,[2,2,2,5,6,7]))
##4. print 'welcome'
##5. create a tuple of few integer values using tuple function
##6. create  a tuple as tuple11, with list,string,tuple,45.21 and integer datat ypes.
#new2 = tuple(('hello','welcome','all','here','python','end'))
##7. print hello , all , python
##8. print all the elements from the tuple
##9. print last element from the tuple
##10. print 'all' from new2
##11. print index of 'end'
#tuple1 = ("Orange",2, [10, 20, 30], ['a','b','c'],(5, 15, 25))
#12. print index of first list
#13. print 1st list from the tuple1
#14. change '20' to 'start'
#15. replace '15' to '9' in tuple1
#16. print second list from tuple1
#17. print tuple from tuple1
#18. change 10 to 'start2'
#19. print 45.21 from tuple11(code should run for all students)
#20. print the number of elements in first list in tuple1.
#21. print the count of 'b' in second list in tuple1.


##1. initialize empty tuple
tuple1=()
print(tuple1)

tuple2=tuple()
print(tuple2)

tuple2=()
print(tuple2[:])


##2. create a tuple of few integer values (dont use tuple function)
tuple3=1,2,3,4,5
print(tuple3)


##3. create a tuple of few string values.
tuple2=('helo','welcome','all','here')
print(tuple2)

tuple2=tuple(('helo','welcome','all','here'))
print(tuple2)


##4. print 'welcome'
tuple1=(1,2,3,4,'welcome')
print(tuple1[4])

tuple1=(1,2,3,4,'welcome')
print(tuple1[4:5])


##5. create a tuple of few integer values using tuple function

tuple1=(1,2,3,4)
tuple2=tuple((1,2,2,3,4,[2,2,2,5,6,7]))
print(tuple1)
print(tuple2)


##6. create  a tuple as tuple11, with list,string,tuple,45.21 and integer data types.
tuple11=([1,2,3],'string',(6,4,5),45.21,99)
print(type(tuple11))


##7. print hello , all , python
tuple13=tuple(('hello','welcome','all','here','python','end'))
print(tuple13[0:6:2])


##8. print all the elements from the tuple
tuple13=tuple(('hello','welcome','all','here','29.32','python','end'))
print(tuple13[:])

tuple13=tuple(('hello','welcome','all','here','29.32','python','end'))
print(tuple13)

tuple13=tuple(('hello','welcome','all','here','29.32','python','end'))
print(tuple13[0:7])


##9. print last element from the tuple
tuple13=tuple(('hello','welcome','all','here','29.32','python','end'))
a=(tuple13.index('end'))
print(tuple13[a])

tuple13=tuple(('hello','welcome','all','here','29.32','python','end'))
print(tuple13[-1])

tuple13=tuple(('hello','welcome','all','here','29.32','python','end'))
print(tuple13[6:7])


##10. print 'all' from tuple2
tuple2 = tuple(('hello','welcome','all','here',29.32,'python','end'))
print(tuple2[2])

tuple2 = tuple(('hello','welcome','all','here',29.32,'python','end'))
print(tuple2[-5])

tuple2 = tuple(('hello','welcome','all','here',29.32,'python','end'))
print(tuple2[2:9:5])


##11. print index of 'end'
tuple2 = tuple(('hello','welcome','all','here',29.32,'python','end'))
print(tuple2.index('end'))


#12. print index of first list
tuple1 = ("Orange",2, [10, 20, 30], ['a','b','c'],(5, 15, 25))
print(tuple1.index([10, 20, 30]))


#13. print 1st list from the tuple1
tuple1 = ("Orange",2, [10, 20, 30], ['a','b','c'],(5, 15, 25))
print(tuple1[2])

#14. change '20' to 'start'
tuple1 = ("Orange",2, [10, 20, 30], ['a','b','c'],(5, 15, 25))
tuple1[2][1]='change'
print(tuple1)


#15. replace '15' to '9' in tuple1
#tuple1 = ("Orange",2, [10, 20, 30], ['a','b','c'],(5, 15, 25))
#tuple1[4][1]=9
#print(tuple1)




#16. print second list from tuple1
tuple1 = ("Orange",2, [10, 20, 30], ['a','b','c'],(5, 15, 25))
print(tuple1[3])


#17. print tuple from tuple1
tuple1 = ("Orange",2, [10, 20, 30], ['a','b','c'],(5, 15, 25))
print(tuple1[4])


#18. change 10 to 'start2'
tuple1 = ("Orange",2, [10, 20, 30], ['a','b','c'],(5, 15, 25))
tuple1[2][0]='start2'
print(tuple1)


#19. print 45.21 from tuple11(code should run for all students)
tuple11 = tuple(('hello','welcome','all','here','45.21','python','end'))
print(tuple11[4])

print(tuple11[-3])


tuple11 = ('hello','welcome','all','here','45.21','python','end')
print(tuple11[-3])

tuple11 = ('hello','welcome','all','here',45.21,'python','end')
print(tuple11[4:7:3])


#20. print the number of elements in first list in tuple1.
tuple1 = ("Orange",2, [10, 20, 30], ['a','b','c'],(5, 15, 25))
print(len(tuple1[2]))


#21. print the count of 'b' in second list in tuple1.
tuple1 = ("Orange",2, [10, 20, 30], ['a','b','b','c'],(5, 15, 25),['a','b','c'])
print(tuple1[3].count('b'))

