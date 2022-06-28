#Practice String
#1.create a string
str1='this is my first BIKE'
print('1.',str1)
print('2.',str1[:])



#1.print whole string
my_str = 'welcome to the lecture'
print(my_str)


#2.print  wloe
str3 = 'welcome to the lecture'
print('2.',str3[0:8:2])


#3.reverse the string
str3 = 'welcome to the lecture'
print('3.',str3[::-1])


#4.print 'the lecture'
print('4.',str3[11:22])


#5.print the length of string
str3 = 'welcome to the lecture'
print('5.',len(str3))


#6.print how many times 't' is repeated
str3 = 'welcome to the lecture'
print('6.',str3.count('t'))


#7.replace 'lecture' with 'session'
print('7.',str3.replace('lecture','session'))


#8.what is the index of 'o' ?
print('8.',str3.index('o'))
print('8.1.',str3.find('o'))


#9. convert string into upper case
str3 = 'welcome to the lecture'
print('9.',str3.upper())


#10. print 'welcome lecture'
str3 = 'welcome to the lecture'
print('10.',str3.split(' to the '))

#11.seperate each word by comma
print('11.',str3.split(' '))

#12.check if string is alphanumeric
print('12',str3.isalnum())

#13.check if string has last character 'e'
print('13',str3.endswith('e'))

