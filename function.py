import functools

def add_number( a , b ):
    print (a + b)


def multiple_number ( a, b ):
    return a * b

add_number ( 3, 5 )
res = multiple_number ( 4, 8)

print ( res )

def addition_number (*args):
    print (args)
    
    return sum(args)


sum = addition_number( 2,3,4,5,6,7,8,9,9)
print ( sum )



def greeting ():
    pass

greeting


print ("======== Lambda Function +++++++++++++++")

square = lambda x: x*x

print (square(2))

add = lambda y: y*5
print ( add( 4 ))

students = [("Rahim",39), ("Karim",10), ("Abu", 23)]

sort_student = sorted( students, key=lambda x : x[1], reverse="true" )  # Based on x[1] value it will sort
print (sort_student)


# map()
num = [2,3,6,9,8]
sqr_num = list(map(lambda x:x*x, num))
print (sqr_num)


# filter()
evennum = list(filter(lambda x:x%2==0, num))
print (evennum)

# reduce
add = functools.reduce( lambda x,y: x+y, num)
print (add)
