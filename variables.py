#Assigning Values to Variables
a=100; #integer
b=10.2 #float
c="py" #string

print(a,b,c,end="\n\n")

#Multiple Assignment
a=b=c="values changed"
print(a,b,c,sep="\n",end="\n\n")
a,b,c=0,1,"Py"
print(a,b,c,sep="\n",end="\n\n")

#Standard Data Types
#-Numbers
#-String
#-List
#-Tuple
#-Dictionary

#--Numbers--
a=10
b=5
print(a,b,end="\n\n")

#Numerical Types: int, float, complex

a=0xa1
b=18.7e5
c=12+3j
print(a,b,c,end="\n\n")

#--Strings--

str = "Hello World"

print(str)                      #string
print(str[0])                   #first character
print(str[2:5])                 #3. character to 5. character
print(str[2:])                  #from 3. character to last
print(str * 2)                  #print 2 times
print(str + "Py",end="\n\n")    #concated string

#--Lists--
listChr = ['a','b','c','d','e']
listNum = [1,2]

print(listChr)                  #list
print(listChr[0])               #first element
print(listChr[1:3])             #from 2. element to 3. element
print(listChr[2:])              #from 2. element to last
print(listNum * 2)              #print 2 times
print(listChr + listNum)        #concated list