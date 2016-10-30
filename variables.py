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

print(str)
print(str[0])       #first character
print(str[2:5])     #3. character to 5. character
print(str[2:])      #from 3. character to last
print(str * 2)      #print 2 times
print(str + "Py")   #concat