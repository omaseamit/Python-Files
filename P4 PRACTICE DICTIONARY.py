
#practice dictionary

#1.initialize dictionary(without using dictionary function)
#2.initialize elements(using dictionary function)
#dict13 = {1:'python' , 2:'java',3:'new',4:'last',5:'end'}
#3.print new from dict13
#4.change 'last' to 'hello' 
#5.add a new pair where, key=10 and value = 'lecture'
#6.pop last pair
#7.delete second pair
#8.print keys from dictionary
#9.print values from dictionary
#10.clear dict
#11.creat dictionary by using 1,2,3,4 as keys and 'is integer' as value

#1.initialize dictionary(without using dictionary function)
my_dict={}
print('1.',my_dict)

#2.initialize elements(using dictionary function)
my_dict=dict()
print('1.',my_dict)

dict13 = {1:'python' , 2:'java',3:'new',4:'last',5:'end'}

#3.print new from dict13
print(dict13.get(3))

#4.change 'last' to 'hello'
dict13[4]='hello'
print(dict13)

#5.add a new pair where, key=10 and value = 'lecture'
dict13['10']='lecture'
print('3.',dict13)

#6.pop last pair
b=dict13.popitem()
print(dict13)

#7.delete second pair
a=dict13.pop(2)
print(dict13)

#8.print keys from dictionary
print(dict13.keys())

#9.print values from dictionary
print(dict13.values())

#10.clear dict
dict13.clear()
print(dict13)

#11.creat dictionary by using 1,2,3,4 as keys and 'is integer' as value

keys=('1', '2', '3')
value=['is integer']
dict13=dict.fromkeys(keys,value)
print(dict13)






