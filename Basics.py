
"""
Created on Thu Sep 26 22:31:25 2019
@author: snikkho based on Mosh Hamedani courses on Youtube
"""
#Basics
# Begin and end comments in paragraphs with """

# first, print a string
# print("Hello World\nThis is Saber")

"""left off
Started on 10/13/2020 with 
Coursera Python for Data Science and AI
""" 

""" Week 1
Types: integer (int), float, string (str), and boolean (bool)
bool output is True or False
type(True):bool
int(True):1
int(False):0
bool(0):False
bool(1):True

Expressions: + - / *
default "/" is a float type
integer division result: //
11//2: 5
Python complies with math order of operations 

Variables
x= int(2)
x=2/1
type(x): float
"""

#Lab
# Try your first Python output
print('Hello, Python!')
# " or ' both work

# Check the Python Version
import sys
print(sys.version)

# System settings about float type
sys.float_info

"""
Strings
' or " work
Sequencing starts at zero
negative indexing starts from -1
Name[0:3] 0 is start, 3 is the 3rd in sequence [2]
Back slash is the begining of an escape seq
Place r before ' or use \\ for actual back slash in a string
String operations : .upper > upper case
.replace("...",",,,")
"""

"""
Week 2
Tuples: oredered sequence > IMMUTABLE (value CANNOT change), written with ()
Lists: like tuple, ,MUTABLE (value can change), and uses []
+ another list or .extend([])
.append([]) adds only one element to the list
.del() > to delete some elements of a list
.split(",")> separates a string at each space or to any char to a list
.sorted() sorts a tuple or list
.index() gives the index in the tuple/list
 = is aliasing, B changes when A changes
 B=A[:] B is CLONING A, B does not change when A changes
 
 Disctionaries:
{"key1":value1, "key2":"value2"}
Keys can be immutable objects such as tuples
Keys can only be strings, numbers, or tuples, but values can be any data type.

dict["key1"] >> value1
dict.keys()  >> gives the keys
dict.values()
del(dict['key1'])

"key1" in dict >> True
up