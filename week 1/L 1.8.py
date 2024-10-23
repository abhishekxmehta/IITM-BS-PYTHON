i = 10
k = 5.6
s = 'india'
b1 = True
b2 = False

print(type(i))
print(type(k))
print(type(s))
print(type(b1))
print(type(b2))

##changing the type 
## changing into float

a=int(5.7)
#here 5.7 is a float but its save as integar hence a just stores 5 and not 5.7
print (a)

b=int('10')

print (type(a))
print (type(b))

##now lets covert to float

c=float(9)
#here 9 to covert into float it become 9.0
d=float('5.3')

print(c,type(c))
print(d,type(d))

## now lets convert into string

e=str(9)
f=str(5.3)

print(e,type(e))
print(f,type(f))

## now lets convert to boolean value

g=bool(10)
h=bool(0)
l=bool(-10)

# #here when any integar is converted into boolean 0 becomes flase and every other int becomes true this holds true for float to 0.0 is false rest are true
# this condition doesnt apply to string in string an empty string is false rest all are true

print(g,type(g))
print(h,type(h))
print(l,type(l))

