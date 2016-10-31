# Assigning Values to Variables
a = 100   # integer
b = 10.2  # float
c = "py"  # string

print(a, b, c, end="\n\n")

# Multiple Assignment
a = b = c = "values changed"
print(a, b, c, sep="\n", end="\n\n")
a, b, c = 0, 1, "Py"
print(a, b, c, sep="\n", end="\n\n")

# Standard Data Types
# -Numbers
# -String
# -List
# -Tuple
# -Dictionary

# --Numbers--
print("--Numbers--")
a = 10
b = 5
print(a, b, end="\n\n")

# Numerical Types: int, float, complex

a = 0xa1
b = 18.7e5
c = 12+3j
print(a, b, c, end="\n\n")

# --Strings--
print("--Strings--")

pyStr = "Hello World"

print(pyStr)                                            # string
print(pyStr[0])                                         # first character
print(pyStr[2:5])                                       # 3. character to 5. character
print(pyStr[2:])                                        # from 3. character to last
print(pyStr * 2)                                        # print 2 times
print(pyStr + "Py", end="\n\n")                         # concated string

# --Lists--
print("--Lists--")
listChr = ['a', 'b', 'c', 'd', 'e']
listNumeric = [1, 2]

print(listChr)                                          # list
print(listChr[0])                                       # first element
print(listChr[1:3])                                     # from 2. element to 3. element
print(listChr[2:])                                      # from 2. element to last
print(listNumeric * 2)                                  # print 2 times
print(listChr + listNumeric, end="\n\n")                # concated list

# --Tuples--
print("--Tuples--")
tupleChr = ('a', 'b', 'c', 'd', 'e')
tupleNumeric = (1, 2)

print(tupleChr)                                         # list
print(tupleChr[0])                                      # first element
print(tupleChr[1:3])                                    # from 2. element to 3. element
print(tupleChr[2:])                                     # from 2. element to last
print(tupleNumeric * 2)                                 # print 2 times
print(tupleChr + tupleNumeric, end="\n\n")              # concated tuple

# -- Dictionary--
dict = {}
dict['one'] = 'a'
dict[2] = 'b'
dictDate = {'day' : 31, 'month' : 10, 'year' : 2016}    # key : value
print(dict['one'])                                      # value for key 'one'
print(dict[2])                                          # value for key 2
print(dictDate)                                         # dictionary
print(dictDate.keys())                                  # the Keys
print(dictDate.values(), end="\n\n")                    # the Values
