## read files and close them.

#f=open(r"C:\Users\user\Desktop\try.txt")


#f=open("C:/Users/Amol mahajan/Desktop/New Text Document.txt")

#f=open("C:\\Users\\Amol mahajan/Desktop\\New Text Document.txt")

#print(f.read()) #read whole file

#print(f.read(2))#read first 2 charactors
#print(f.readline())#read line by line
#print(f.readline())
#print(f.readline())
#print(f.readlines())
#f.close()

## no need to close file
#with open(r"C:\Users\user\Desktop\try.txt") as f:
      #print(f.read())



## combine open and read functions
#a1=open(r"C:\User\user\Desktop\try.txt").read()
#a1=open(r"C:\Users\user\Desktop\try.txt").readlines()
#print(a1)

### Diffirent modes:
# 'r' = for reading,it is default mode,Error if dose not exist.'rb' = for binary file
# 'r+ = for reading and writing ,'r+b' for binary
# 'a' = open or creates file for appending i.e new data is add after last line.'ab' for binary file
# 'w' = open or creates for writing.overwrites existing content.creates if does not exist.
# 'w+' =open or creates for reading and writing,'w+b' for binary
# 'rt' = for reading text file.


##write and append
#a1=open(r"C:\Users\user\Desktop\try.txt",'a')
#a1.write("3.every thing is cleared and i am in")
#a1.close()


###lstrip and rstrip fn
#f1=open(r"C:\Users\user\Desktop\try.txt","rt")
#a=(f1.read())
#print(a)
#b=a.lstrip("1.")
#print(b)
#f1.close()

##slit fn
#f1=open(r"C:\Users\user\Desktop\try.txt","rt")
#h=list(f1.read().split(" "))
#print(h)
#f1.close()

#slit from letter
#f1=open(r"C:\Users\user\Desktop\try.txt","rt")
#w=list(f1.read().split("a"))
#print(w)
#f1.close()




## checking file pointer
#tell where is the pointer
f=open(r"C:\Users\user\Desktop\try.txt")
print(f.read(22))
print(f.tell())
f.close()


##read after second character
f=open(r"C:\Users\user\Desktop\try.txt")
f.seek(12)
print(f.readline())
print(f.tell())
f.close()











# 'x' = creates new file for writing
