
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

Sets {}
No duplicates allowed
.add() adds an element
.remove() removes
"exmaple" in A   >> to check
set1 & set2 >> intersection  or .intersection
set1.difference(set2)  >> finds the differences
.union
.issubset
.issuperset
"""

"""
Week 3
Conditions and Branching
== and != for comparison

if age>18:
    print('you can enter')
elif age==18:
    print('go see Pink Floyd')
else:
    print('go see Meat Loaf')
print('move on')    >> prints this line anyway

if or ()  if and if not ()
if not (): = if !=

Loops
range(n) > Range(0,n-1) a range of n items 

dates = [1982,1980,1973]
N = len(dates)

for i in range(N):
    print(dates[i])
    
for year in dates:  
    print(year)   
    
    
squares = ['red', 'yellow', 'green', 'purple', 'blue']
for i, square in enumerate(squares):           #passes index to i and value to square
    print(i, square)
  
While Loop
dates = [1982, 1980, 1973, 2000]
i = 0
year = 0
while(year != 1973):
    year = dates[i]
    i = i + 1
    print(year)
print("It took ", i ,"repetitions to get out of loop.")


Genres = ['rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']
for Genre in Genres:
    print(Genre)
    
For loop does the looping ovr a given range, however, for While we need to make the range 

squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []
i = 0
while(squares[i] == 'orange'):
    new_squares.append(squares[i])
    i = i + 1
    
    
Functions
def function(input):
    output=input+1
return output

built-in functions: 
sorted does not change the original list
sort, sorts that list
Mult can work on strings
"pass" as none in function

def Print(A):
    for a in A:
        print(a+'1')
Print(['a','b']) >>> a1 , b1     

Global vs local variable
add key "global" wihtin function to become global variable   
packing function inputs using *
oacking funxtion inputs into dictionary using **

Class***
Object is realization/instant of a class/type
class Circle(object):
    def _init_(self, radius, color):
        self.radius = radius
        self.color = color
dir(NameofObject): >> attributes        

exmaple:
class analysedText(object):

    def __init__ (self, text):
        # remove punctuation
        formattedText = text.replace('.','').replace('!','').replace('?','').replace(',','')

        # make text lowercase
        formattedText = formattedText.lower()

        self.fmtText = formattedText

    def freqAll(self):        
        # split text into words
        wordList = self.fmtText.split(' ')

        # Create dictionary
        freqMap = {}
        for word in set(wordList): # use set to remove duplicates in list
            freqMap[word] = wordList.count(word)

        return freqMap

    def freqOf(self,word):
        # get frequency map
        freqDict = self.freqAll()

        if word in freqDict:
            return freqDict[word]
        else:
            return 0
            
            
Expections****
a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")
else:
    print("success a=",a)
    
"""

"""
****Week4
Open

# Read first four characters
with open(example1, "r") as file1:
    print(file1.read(4))


Pandas
>import pandas as pd
#it includes dataframe
df = pd.read_csv(csv_path)
variable = pd.DataFrame(dictionary_name)

we can find a value in dataframe with loc (label based), or iloc(integer based) or ix(by label or integer)
df.loc[0, 'Artis'] : Michael Jackson

Working with Pandas:
df1 = df[ df[''columnName'] >= SomeValue]
df1.to_csv('new_dataframe.csv')


*Numpy - 1D
A numpy array is similar to a list. It's usually fixed in size and each element is of the same type. 
We can cast a list to a numpy array by first importing numpy:

import numpy as np 
a = np.array([0, 1, 2, 3, 4])
type(a) : numpy.ndarray
a.dtype : dtype('int64')
a[3:5] = 300,400    # slicing and assigning 4th and 5th elements

Assign value with list:
select = [0, 2, 3]
a[select] = 10
a.size >5
a.ndim : 1
a.shape : (5,0)
a.mean < average
a.std > standard deviation

np.dot(u, v)

np.pi > math pi

# Makeup a numpy array within [-2, 2] and 5 elements
np.linspace(-2, 2, num=5)

x = np.linspace(0, 2*np.pi, num=100)
y = np.sin(x)
plt.plot(x, y)
