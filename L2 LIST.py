
##List

#1. initializing list
list0=[]
print(list0)

#2. creating a list
list1= [1,2,3,'helo',4,5]
print(list1)

list2=([5,6,'hi',7])
print(list2)

list3=[0,1,2,3,4,5,6]
print(list3)

#3. index function (list[starting index:ending index:skipping value])

list1= [1,2,3,'helo',4,5]

list2=([5,6,'hi',7])

list3=['a',1,2,3,4,5,6]

print(list1[:6])      #to print all list element
print(list1[3])       #to print value of 3rd index
print(list1[0:4])     #to print value fron 0 to 3th index
print(list1[::-2])    #to print reverse order
print(list1[-2:-5:1])
print(list1[0:5:2]) #to print using skiping index
print(list1[3][1])  #to print alphabate of string using index place

#4. append function (for adding element in list

list1=list([1,2,3,'helo',4,5,3])
list1.append(10)  #to add element in list
print(list1)

list1.append([11,12])  #to add two elements as arguments(at one index)
print(list1)

#5. extend function

list1=list([1,2,3,4,5,6,7,8,9,10,11])

list1.extend([16])
print(list1)

list1.extend([14,15])
print(list1)

#6. insert function

list1=list([1,2,3,4,5,'hi',6,7,8,9,10,11])

list1.insert(3,'good')
print(list1)

#7. index function

list1=list([1,2,3,4,5,'hi',6,7,8,9,10,11])

print(list1.index('hi'))

#8. count function

list1=list([1,2,3,4,5,'hi',6,7,8,'hi',9,10,11])

print(list1.count('hi'))

#9. length of function

list1=list([1,2,3,4,5,'hi',6,7,8,'hi',9,10,11])

print(len(list1))


#10. reverse function

list1=list([1,2,3,4,5,'hi',6,7,8,'hi',9,10,11])

list1.reverse()
print(list1)

#11. sort function

list4 = [6,2,8,1,10,4,7,3,0,5,9]

list4.sort()      #change list by sort in accending order
print(list4)
#or
print(sorted(list4)) #only print accending order



list4.sort(reverse=True) # sort in decending order
print(list4)
#or
print(sorted(list4,reverse=True))



#12. copy function

list5=list4.copy()
print('list5 is',list5)
#or
print(list4.copy())


#13. pop function (use index)

a=(list4.pop(2))
print(a)
print(list4)

#14. remove function  for removing in the list (use value)

list4.remove(7)
print(list4)

#15. del function ,for deleting an element in the list ( use index)

del(list4[2])
print(list4)

#16. clear function , for clearing list

list4.clear()
print(list4)

#17. replace an element in list

list5=[6,2,8,1,10,4,7,3,0,5,9]

list5[-2]='5 is replaced'
list5[3]=35
print(list5)






































