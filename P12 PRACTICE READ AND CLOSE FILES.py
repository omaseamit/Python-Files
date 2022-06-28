

###1.Make a copy of file

#f=open(r"C:\Users\user\Desktop\try.txt")
#f.close()

#f1=open(r"C:\Users\user\Desktop\try1.txt",'w')
#f1.close()

###2.add your educational information in some already existing file

#a1=open(r"C:\Users\user\Desktop\try.txt",'a')
#a1.write("2.i am mechanical engineer 2018 passout from sppu with first class.")
#a1.close()

###3.convert the given file in list and print the common data



f= open(r'C:\Users\user\Desktop\happy.txt') 
h1=list(f.read().split(','))
f.close()


f1= open(r'C:\Users\user\Desktop\prime (1).txt')
h2=list(f1.read().split(','))
f1.close()

list1=[]
for i in h1:
    for j in h2:
        if i==j :
            list1.append(i)
print(list1)

           

###4.store an hd image (use binary file)

f=open(r"C:\Users\user\Desktop\image binary.jpg",'rb')
a=f.read()
f.close()

f1=open(r"C:\Users\user\Desktop\creat file.jpg",'wb')
f1.write(a)
f1.close()


###5.find number of lines in any text file

f=open(r"C:\Users\user\Desktop\try.txt")
count=0
for i in f:
      count+=1
print(count)
f.close()

#or

with open(r"C:\Users\user\Desktop\try.txt") as f:
   a=f.readlines()
   print("Number of lines are:",len(a))




