
###dictionary

#dictionary is mutable

#1. initialize dictionary
my_dict={}
my_dict1=dict()
print('1.',my_dict)
print('2.',my_dict1)

##2. creating dictionary
dict1={1:'python',2:'java'}
dict2=dict({1:'one',2:'two'})
print('1.',dict1)
print('2.',dict2)

##3. changing an elements
dict3={'one':'python','two':'data science','three':'analysis'}
print('1. This is dict3',dict3)

#changing value 'data science' to 'machine learning'
dict4={'one':'python','two':'data science','three':'analysis'}
dict3['two']='machine learing'

##4. delete element
dict4={'one':'python','two':'data science','three':'analysis'}
print('1.',dict4)
print('2.',dict4.pop('two')) #remove key and value
print('3.',dict4)

##5. adding key and value
dict3={'one':'python','two':'data science','three':'analysis'}
dict3['four']='maths'
print('3.',dict3)

##6. pop element in dictionary
dict4={'one':'python','two':'data science','three':'analysis'}
a=dict4.pop('two')
print('4.',a)
print('5.',dict4)
      
##7. popitem function (pop last print)
dict4={'one':'python','two':'data science','three':'analysis'}
print('1.',dict4)
b=dict4.popitem()
print('2.',b)
print('3.',dict4)

##8. copy function
dict4={'one':'python','two':'data science','three':'analysis'}
dict5=dict4.copy()
print(dict5)

##9. clearing dictionary
dict5={'one':'python','two':'data science','three':'analysis'}
dict5.clear()
print('5.',dict5)

##10. get function (return value for given key)
dict5={'one':'python','two':'data science','three':'analysis'}
print(dict5.get('one'))

##11. print keys from dictionary
print('1.',dict5.keys())

##12. print values from dictionary
print('2.',dict5.values())

##13. formkeys function (creat adictionary from sequence
dict6={'one':'python','two':'data science','three':'analysis'}
keys={'one','two','three'}
value=['great']
dict6=dict.fromkeys(keys,value)
print(dict6)

#changing dictionary
value.append('nember')
print(dict6)



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
























