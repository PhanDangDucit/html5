# ----------- Notice that in the prior examples, we were not changing the original string with any of the operations we ran on it.
# Every string operation is defined to produce a new string
# as its result, because strings are immutable in Python—they cannot be changed in-place after they are created. 
# For example, you can’t change a string by assigning to one of its
# positions, but you can always build a new one and assign it to the same name.
# Because Python cleans up old objects as you go (as you’ll see later), this isn’t as inefficient as it may sound.
# ----------- Every object in Python is classified as either immutable (unchangeable) or not.
# In terms of the core types, numbers, strings, and tuples are immutable; lists and dictionaries are not (they can be changed in-place freely).
# Among other things, immutability can be used to guarantee that an object remains constant throughout your program.



a = 'hello'
b = 'world'

print(a)
print(b)

c = 'this is also a string'
print(c)

#backslash
d = 'I\'m Duc'
print(d)

e = "I'm duc"

print(e)

# len
len(a)
len(b)
len(c)

## string indexing and slicing
# index
mystr = 'hello world'

print(mystr[1])
print(mystr[-1])

# new knowledge
# mystr[start:end:step]
# step: buoc nhay
print(mystr[1:])
print(mystr[2:])
print(mystr[:3])
print(mystr[3:5])
print(mystr[3:5:2])

x = 5
y = "John"
print(type(x))
print(type(y))

mystring = 'hello guy!'
print(len(mystring))

print(mystring.find('guy'))

print(mystring.replace('guy', 'world'))
print(mystring)

mystring1 = 'a,b,c'
print(mystring1.split(' '))
print(mystring1)
# split
mystring2 = 'a b c'
print(mystring2.split(' '))
print(mystring2)
# upper
print(mystring2.upper())
print(mystring2)
# lower
mystring3 = 'A B C'
print(mystring3.lower())
print(mystring3)

# isalpha / isdigit
mystring4 = 'a b c'
print(mystring4.isalpha()) # alpha?
print(mystring4)
# rstrip
mystring5 = '   a b c   '
print(mystring5.rstrip())
print(mystring5)

# how to check python string/number method
print(dir(mystr))
mystr = 5
print(dir(mystr))

# help function
mystr = 'a b c'
help(mystr.replace)
