import os
import pathlib
from pathlib import Path
from os import path
import shutil
from zipfile import ZipFile

# Read the file whole content

file = open('name.txt', "r")
content = file.read()
print (content)

file.close()


with open('name.txt', "r") as f:
    content = f.read()
    print (content)

f.close()

with open('name.txt', "w") as f:
    f.write("Hello World\n")

f.close()   

lines = ["Python is a popular programming language.\n", "Python can be used on a server to create web applications.\n", "Python is easy to learn - You will enjoy it!\n"]

with open('name.txt', "a") as f:
    for i in lines:
        f.write(i)
    f.writelines(lines)


f.close()  

with open('name.txt', "r") as f:
    content = f.read()
    print (content)

f.close()

# read file content line by line
file = open("name.txt", "r")
if file.mode == "r":
    file_lines = file.readline()
    for line in file_lines:
        print (line)

if os.path.exists('name.txt'):
    print ("File Exist")
else:
    print ("Not found")

file_path = pathlib.Path('name.txt')

if file_path.exists:
    print ("File Exist")
else:
    print ("Not found")


path = ['/home/User/Desktop', '/home/User/Media', '/home/User/Pictures']

print ( os.path.abspath('name.txt') )
print ( os.path.getsize('name.txt') )
longpath = os.path.commonprefix(path)

print (longpath )

# ================= Exception Error +++++++++++++++++
print ("================= Exception Error +++++++++++++++++")
try:
    with open('name1.txt', "r") as f:
        content = f.read()
        print (content)
    f.close()
except FileNotFoundError:
    print ("Not found")
except ZeroDivisionError:
    print ("ZeroDivisionError")
except Exception as e:
    print (e)


# Custom Error Exception
print ("+++++++++++++++ Custom Error Exception ================")
def checkfile_ext(filename):
    if not filename.endswith(".txt"):
        raise ValueError("Only .txt files are allowed")         # here raise helps to generate exception
    else:
        print("it is txt file")


try:
    checkfile_ext("name.csv")

except Exception as e:
    print ( e)



print("============ Duplicate File =================")
# Duplicate a file.
if os.path.exists("name.txt"):
    # Get the real path of a file
    src = os.path.realpath("name.txt")
    # backup the file
    dst = src+".bak"
    # copy the file without prtoerties
    # shutil.copy(src, dst)
    # copy2 the file prtoerties
    # shutil.copy2(src, dst)
    # rename the file
    # os.rename("name.txt", "name2.txt")
    # create a zip file
    root_dir = os.path.split(src)
    print(root_dir)
    root_dir, tail  = os.path.split(src)
    print(root_dir, "--------", tail)
    shutil.make_archive("archive", "zip", root_dir)

    # src.

    # another option of zip file
    with ZipFile("Test.zip", "w") as newzip:
        newzip.write("name.txt")
        newzip.write("name.txt.bak")


def file_info(st):
    print ("======= file info ==========")
    # p = Path(".")
    # files = p.glob("*.py")
    # global totbyte
    # totbyte = 0

    # for i in files:
    #     # file_path = pathlib.Path(i)
    #     # file_path.absolute()
    #     bsize = os.path.getsize(i) 
    #     # print ( file_path, " --- ", bsize )
    #     totbyte = totbyte + bsize
    # # print(totbyte)
    # return totbyte

    dir = os.path.abspath(".")
    files = dir.endswith(".txt")
    print (dir)
    for i in files:
        file_path = pathlib.Path(i)
        file_path.absolute()
        bsize = os.path.getsize(i) 
        print ( file_path, " --- ", bsize )
        totbyte = totbyte + bsize
    print(totbyte)
    

# result = 
file_info("Ahmad")
# print( result )