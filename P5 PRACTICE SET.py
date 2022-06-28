#practice set

#1.creat an empty set
set1=()
print(set1)
print(type(set1))

#2.create a set with multiple values,repetitions and all possible data type, print the set
set2={1,2.35,2,'hi',(5,6,8),7,11,-22,33,'hi'}
print(set2)
print(type(set2))

#3.add 100 in the set
set2.add(100)
print(set2)
print(set2)
print(set2)

#4.add 23,'little',[11,'done',33],('a','b',10),{'d','f'},{71:'one',72:'two'},set1
set1={1,2,3,4}

set1.update('little',[11,'done',33],('a','b',10),{'d','f'},{71:'one',72:'two'},set1)
print(set1)

#5. delete tuple and 50 from set
set21={1.56,'hello in set',(1,2,2,3,3,3),-6,-6,50}
set21.remove(50)
set21.remove((1,2,2,3,3,3))

#6.delete first element from set
a=set1.pop()
print(set1)

set1 = {1,2,3,4,7,9}  
set2 = {1,4,5,6,11,3}
#7.print the all elements of these sets

#method1
print('1.',set1.union(set2))
#method2
print('1.',set2|set1)

#8.print the common elements of these sets
#method1
print('2.',set2.intersection(set1))
#method1
print('2.',set1&set2)

#9.print the uncommon elements of both set1 and set2
print('3',set1.symmetric_difference(set2))
print('3',set1^set2)

#10.print difference of set2 and set1
print('4.',set2.difference(set1))
print('4.',set2-set1)


s1 = {1,3,4,11}
s2 = {3,2,4,5,6}
s3 = {2,3,4,5,6,8,9,1,10,11,12,20}
#11.check if 4 is present in s1
print('5. if 4 is in s1',4 in s1)
print('6. if 4 is not in s1',4 not in s1)

#12.check if s1 and s2 are same
print('7. if s1 and s2 not summetric ?',s1 == s2)

#13.check if s1 is subset of s3
print('8 if s1 is subset of s3 ?',s1 <=s3)

#14.check if s2 is proper set of s3
print('9. if s2 is proper subset of s3 ?',s2 < s3)



