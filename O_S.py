import os
from os import path
import time
from datetime import datetime

print (os.name)

print ("File Exists: ", path.exists("name.txt"))
print ("Is it file", path.isfile("name.txt"))
print ("is it directory", path.isdir("name.txt"))

# get real path

print ("File Exists: ", path.realpath("name.txt"))
print ("File Exists: ", path.split (path.realpath("name.txt")))

# File modify date
t = time.ctime( path.getmtime("name.txt") )
print ( t )
print ( datetime.fromtimestamp(path.getmtime("name.txt")) )


# last 
now = datetime.now()
dif = now - datetime.fromtimestamp(path.getmtime("name.txt"))
print ( dif.days, dif.min )
