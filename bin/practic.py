
x = input ("enter your number for")
y = input ("enter your number")
z= int(x) + int (y)
print (z)

c = input ("enter your number in cs")
c = int (c)
z= (5/9) * c + 32
print (z)

m= input ("enter your number for m")
s = input ("enter your number for s")
m = int(m)
s = int (s)
z = m/60 + s/3600
print (z)

def add (x, y):
	z = x + 6
	return print (z)
	
a = 4
b = 6
c = add (a, b)

d = 6
e = 7
g = add (d, e)


def add (x, y):
	z = x + 6
	return print (z)
	
a = input ("enter no ")
b = input ("enter no b")
a = int (a)
b = int (b)
c = add (a, b)


def temp (c):
	z = (5/9) * c + 32
	return print (z)
	
c= input ("enter no ")
c= int (c)
temp (c)


def temp (m, s):
	z = m/60 + s/3600
	return print (z)
	
m = input ("enter no m")
s = input ("enter no s")
m = int (m)
s = int (s)
temp (m, s)



def div (d,f):
	if (f == 0):
		return print ("no way my bro")
	else:
		g = d/f
		return print (g)
	
d = input ("numb")
f = input ("numb 2")
div (int (d), int (f))


