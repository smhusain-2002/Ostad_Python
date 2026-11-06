a = "this is a string"
b = "this is also a string"
c= """
1. Creative Question: 10 Marks
2. Case Study: 5 Marks
3. Short Question or Short Notes: 5 Marks
"""

print (a)
print(type(a))


print (b)
print(type(b))


print (c)
print(type(c))


print (a[3])
print (a[14])
print (len(a))

# print()

print (a[-1])

b = "Rahim"

print (b.replace("a", "o", 1))

print ("")

print (b)


# input and format function in long

user = "Ahmad" # input("What is your name? ")
a = "Good Morning {}. How are you?".format(user)

print (a)

a = "Good Morning {u}. How are you?".format(u=user)

print (a)

# format function in short
b = f"Good Morning {user}. How are you?"

print(b)


name = "Ahmad"

rev = name[::-1]

print (rev)