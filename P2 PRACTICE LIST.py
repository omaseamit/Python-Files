# Practice list



###Q1 print welcome python1
list11 = ['welcome',1,2,3,'python1',6,5,13,'python2','python3',10.5]

#method 1
print(list11[0:5:4])

#method 2
a=(list11[0])
b=(list11[4])
print(a,b)

#method 3
print(list11[-11:-6:4])

###Q2
list12 =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

#print table of 2
print(list12[1:20:2])
#print table of 3
print(list12[2:20:3])

#type "end" at place of 4
list11.insert(4,'end')
print(list11)

#type end at last
list11.extend(['end'])
print(list11)

list11.append('end')
print(list11)

###Q3 reverse list 'new'
new = [10,29,1,2,3,7,9,0,4,55]

#method 1
print(new[::-1])
#method 2
new.reverse()
print(new)

###Q4 only print sorted list in ascending and descending order
new = [10,29,1,2,3,7,9,0,4,55]

#accending
new.sort()      
print(sorted(new)) 

#descending
new.sort(reverse=True) 
print(sorted(new,reverse=True))

###Q5 changing the list to sort descending order





###Q6 deleting 3 from list 'new' (use index)
new = [10,29,1,2,3,7,9,0,4,55]

del(new[3])
print(new)


###Q7 remove 29 from list 'new' (use values)
new = [10,29,1,2,3,7,9,0,4,55]

new.remove(29)
print(new)

###Q8 pop 9 from list 'new' (uses index and returns the value)
new = [10,29,1,2,3,7,9,0,4,55]

a=(new.pop(6))
print(a)
print(new)

###Q9 copy new list
new = [10,29,1,2,3,7,9,0,4,55]

new1=new.copy()
print(new1)


###10 count '2' in list a
a=[1,2,12,2,2,2,3,3,4,4,5,5,6,6,7,7,8,9,9,5,6,5,7,6,7,6,3,4,5]


print(a.count(2))


###11 clear list
new = [10,29,1,2,3,7,9,0,4,55]

new.clear()
print(new)

###12 append "cup" in list11
list11 = ['welcome',1,2,3,'python1',6,5,13,'python2','python3',10.5]

list11.append('cup')  
print(list11)


###13 extend "tea" in list12
list12 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

list12.extend(['tea'])
print(list12)


###14 add 32,41,55 in list 'new'
new = [10,29,1,2,3,7,9,0,4,55]

new.extend([32,41,55])
print(new)


###15 add 22,32,42 as one index in list'new'
new = [10,29,1,2,3,7,9,0,4,55]

new.append([22,32,42])  
print(new)

###16 replace '29' by 'done' in list 'new'
new = [10,29,1,2,3,7,9,0,4,55]

new[1]='done'
print(new)









###

new = [10,29,1,2,3,7,9,0,4,55]
##3.1 reverse list 'new'
##4.only print sorted list in ascending and descending order
##5.changing the list to sort descending order
##6.deleting 3 from list 'new' (use index)
##7.remove 29 from list 'new' (use values)

##8.pop 9 from list 'new' (uses index and returns the value)
##9.copy new list
##10. count '2' in list a
#a=[1,2,12,2,2,2,3,3,4,4,5,5,6,6,7,7,8,9,9,5,6,5,7,6,7,6,3,4,5]
##11.clear list 
##12.append "cup" in list11
##13.extend "tea" in list12
##14.add 32,41,55 in list 'new'
###15.add 22,32,42 as one index in list'new'
##16.replace '29' by 'done' in list 'new'






