x = 1

if x == 1:
    print ( "The value of X is 1" )
else:
    print ("The value of X is not 1")


f = 10
print (f)

if f > 0:
    print ("The value of a is Positive")
elif f == 0:
    print ("The value of a is 0")
else:
    print ("The value of a is Negative")

result = "x is 1" if ( x== 1) else "X is not equal to 1"
print ( result )



# List 
print ("=========== List ================")
a = [1, 2, 4, "Ahmad", 2.3, 123, "Dhaka"]

print ( a )
print ( a[-1] )
print ( a.pop() )
print ( a.append(1.22))
print (a)

# Loop through list
# for i in a:
# for i in range(len(a)):



# Tuples
print ("=========== Tuples ================")

tupl = (1,2,3,45,6,78,9,0,87,65,3,3)
print ( tupl )
print (tupl[1:4])

print (tupl[-2])

# Loop for Tuples
# for i in tupl:
# for i in range(len(tupl)):
# for i in range(0, len(tupl), 2):
# for i in range(len(tupl)-1, -1, -1):


# SET
print ("=========== SET ================") 

a = {1,2,3,4,5,6}
b= {3,4,5,6,7,8,9}

print ( a )
print ( b )

c = a.intersection(b)
print ( c )

d = a.union (b)
print ( d )

e = b.union ( a )
print ( e )

e.update( [10] )
print (e)

e.remove (10)
print ( e )



# Dictionary 
print ("=========== Dictionary  ================") 

# key pair value
# No indexing
# Key must be immutable

a = { 'rahim': 12, 'karim': 14, 1:[1,2,3,4,5], 2:(4,5,6,7,8) }

# Only Key will display
for i in a: 
    print ( i )

print ("========")

# Dictionary loop patterns

# for <key> in <dict>:
# for <key> in <dict>.keys():
# for <value> in <dict>.values():
# for <key>, <value> in <dict>.items():



# display only values
for i in a.values():
    print ( i )


# view as list
print (a.keys(), a.values())

# both Key and values
for k,v in a.items():
    print (f"Keys: {k}, Values {v}")


# Merge 2 lists
a = ["Mango", "Banana", "Apple"]
b = ["230", "350", "300"]

c = dict(zip(a,b))

print (zip(a, b))           # display a object value
print (list(zip(a,b)))      # Display Key and value in List format
print (tuple(zip(a,b)))     # Display Key and value in Tuple format
print (dict(zip(a,b)))      # Display Key and value in Dict format

print (dict(zip(b,a)))      # Display Key and value in Dict format


print ( c["Mango"] )        # find the value of dict

# Comprehensions

# List:  {<element> for <element> in <iterable> if <condition>}
# dict:  {<key>: <value> for <key>, <value> in <iterable> if <condition>}
# set:   {<element> for <element> in <iterable> if <condition>}
# tuple: (<element> for <element> in <iterable> if <condition>)

# Dict comphrehension
print ("=========== Dictionary Comprehension ================") 

num = list(range(0,11))

result = {i: "Even" if i%2==0  else "Odd" for i in num}

print (result)

squares_dict = {i: i**2 for i in range(1, 11)}
print (squares_dict)

square_sum = sum(i**2 for i in range(1, 11))   # sum of squares from 1 to 10
print(square_sum)




# check data
print ("Banana" in a)
print ("Apple" in a)
print ("Orange" in a)


# List comprehension
print ("=========== List Comprehension ================") 

# Basic List 
squares = []
for i in range(1, 11):
    squares.append(i**2)

# List comprehension
squares = [i**2 for i in range(1, 11)]

print(squares)

squares_div_4 = [i**2 for i in range(1, 11) if i % 4 == 0]          # Include only those numbers which are divisible by 4
print(squares_div_4)
