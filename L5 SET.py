
##set

#-set is mutable and has only unique immutable elements.
#-A set is created by placing all the items (elements) inside curly
#braces {},separated by comma, or by using the built-in set()function.
#-It can have any number of items and they may be of different
#types (integer, float, tuple, string etc.)
#-But a set cannot have mutable elements like lists, sets or
#dictionaries as its elements.

#1. initializing set
my_set1=set()
print(type(my_set1))
print('1.',my_set1)

#2. initializing element in set
my_set2={1.3,'hello',(1,2,3),6,6}
print('2.',type(my_set2))
print('3.',len(my_set2))
print('4.',my_set2)

#3. adding element to set
set9={1,2,3}
print(set9)
set9.add('x')
print(set9)

#4. update sets
set1={2,3,4,5}
set2={4,5,6,7}
set1.update(set2,{33,44,55},'b')
print(set1)

#5. remove an element
set1={1,2,3}
set1.remove(3)
print('after remove',set1)

#6. discard an element
set1.discard('a')
print(set1)

#7. pop element
set1={2,3,4,5}
a=set1.pop()
print(set1)

#8. max , min, sum
set1={2,3,4,5}
print('maximum value is')
print(max(set1))

print('minimum value is')
print(min(set1))

print('sum of values is')
print(sum(set1))


#9. empty the set
set1.clear()
print(set1)

#10. other method in set
set1={2,3,4,5}
set2={4,5,6,7}
print('1.',set1)
print('2.',set2)

##11. union|(it is aal items of both sets)
print('3.',set1.union(set2))
print('3.',set2|set1)

#12. intersection & function (it is comman of both set)
print('4.',set2.intersection(set1))
print('4.',set1&set2)

#13. difference set2-set1
print('5.',set2.difference(set1))
print('5.',set2-set1)

#set1-set2
print('6.',set1.difference(set2))
print('6.',set1-set2)


#14. symmetric difference (it is uncommon elements)
print('7.',set1.symmetric_difference(set2))
print('7.',set1^set2)

#15. Boolean operators for sets
superset={0,1,2,3,4,4,5,6,7,8,9,}
s1={2,3,4,5}
s2={4,5,6,7}
print('x8. superset is ',superset)
print('x9. s1 is',s1)
print('x10.s2 is' ,s2)

# find an element in set
print('11. if 6 is in s1',6 in s1)
print('11. if 6 is not in s1',6 not in s1)

# if symmetric 
print('12. if s1 and s2 summetric ?',s1 == s2)

# if not symmetric 
print('13. if s1 and s2 not summetric ?',s1 != s2)

# if s1 is a subset of supeset try by using issubset()
print('14. if s1 is a subset of superset ?',s1 <= superset)

# if s1 is a proper subset of superset
print('15. if s1 is a proper set of superset ?',s1 < superset)

# if s2 subset of s1
print('16. if s2 is subset of s1 ?',s2 <=s1)

# if  s2 proper subset of s1
print('17. if s2 is proper subset of s1 ?',s2 < s1)

# if sperst is a superset of s1 try by using isssuoerset()
print('18. if superset is a superset of s1 ?',superset >=s1)











