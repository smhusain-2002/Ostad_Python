a = [1,2,3,4,5,6,7,8,9,0]

for item in a:
    print ( item )

b = "Hello World"

for item in b:
    print ( item )

b = "Hello World"

c = []

for item in a:
    if item % 2:
        print ( item )
        c.append(item)

print (c )


# List  comprehension
d = [ i for i in a ]

print ( d )

# List  comprehension
# newlist = [expression for item in iterable if condition == True]
e = [ i for i in a if i%2 ]

print ( e )


# newlist = [expression if condition == True else for item in iterable ]
f = [i**2 if i%2 else i for i in a]
print ( f )

g = [i**2 for i in a if i%2 ]
print ( g )

# List comprehension
# [ operation ]

days = ["Mon", "Tue", "Weds", "Thus", "Fri", "Sat", "Sun"]

for i, d in enumerate(days):
    print (i, d)

