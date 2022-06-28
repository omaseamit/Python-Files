#strings are a collection of characters
#they are written within '' & ""
#Strings are not mutable and case sensitive

# create a string
mystr1 = 'this is my first string'
string = "this is my second string"
print(mystr1)
print(string)
print(type(string))


# slicing of string
str1='this is my first string'
print('1.',str1)
print('2.',str1[:])


# print from index 1 to 9
print('3.',str1[1:10])


# print till 'm' skipping 1 element
print('4.',str1.index('m'))
print('5.',str1[0:9:1])


# print from 0 to 13 skipping 3elements
print('6.',str1[0:14:3])


# reverse the string
print('7.',str1[::-1])


# reverse indexing
print('8.',str1[-8:-1])
print('9.',str1[-8])


# assigning a value
#a=(str1[2:10])
print('10.',str1[2:10])



# splitting string for the parameter passed
print('11.',str1.split(' rst '))


# breaks the string into tuple passed
print('12.',str1.partition(' rst '))


# replace the string
print('13.',str1.replace('string','day'))


# return the length of string
print('14.',len(str1))


# print count of character 't'
print('15.',str1.count('t'))


# convert to upper case
print('16.',str1.upper())


# convert to lower case
print('17.',str1.lower())


# return the index of element found
print('18.',str1.index('first'))
print('19.',str1.find('first'))


# check last string
print('20',str1.endswith('ing'))

str12="str3ring"


#returns True , if alphanumeric string (ex:abcde or 12345).
print('21',str12.isalnum())


#returns True , if all the characters are alphabet letters  (atoz).
print('22',str12.isalpha())

