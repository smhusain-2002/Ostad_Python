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

# Tuples
print ("=========== Tuples ================")

tupl = (1,2,3,45,6,78,9,0,87,65,3,3)
print ( tupl )
print (tupl[1:4])

print (tupl[-2])



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

# Dict comphrehension
print ("=========== Dictionary Comprehension ================") 

num = list(range(0,11))

result = {i: "Even" if i%2==0  else "Odd" for i in num}

print (result)




# check data
print ("Banana" in a)
print ("Apple" in a)
print ("Orange" in a)

