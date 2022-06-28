#Mean is average value.
#1. Find mean of given numbers.
#a. 9,7,11,13,2,4,5,5  \\7
#b) 16,18,19,21,23,23,27,29,29,35  \\24
#c) 2.2,10.2,14.7,5.9,4.9,11.1,10.5  \\8.5


a=[9,7,11,13,2,4,5,5]

mean=sum(a)/len(a)
print(mean)

b=[16,18,19,21,23,23,27,29,29,35]
mean=sum(b)/len(b)
print(mean)


c=[2.2,10.2,14.7,5.9,4.9,11.1,10.5]
mean=sum(c)/len(c)
print(mean)


#Median

e=[12,17,3,14,5,8,7,20]
n=len(e)
e.sort()    
print(e)

if n%2==0:
    m1=e[n//2]
    m2=e[n//2-1]
    median=(m1+m2)/2
    print(median)
else:
    median=e[n//2]

    print(median)


# mode

a=[12,8,4,8,1,8,9,11,9,10,12,8]

b=list(set(a))
list1=[]
for i in b:
    n=a.count(i)
    list1.append(n)
x=list1.index(max(list1))

mode=b[x]

if max(list1)==1:
    print('No mode')
else:
    print('Mode: ',mode)

    
#standard deviation

list4 = [1,2,3,4]
b=0
mean=sum(list4)/len(list4)
for i in list4:
    x=(((i-mean)**2)/len(list4))
    b=b+x

print(b**0.5)

    
