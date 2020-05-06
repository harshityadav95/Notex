# Python 

# To Insert Exit the Python shell quit(), use its integrated IDLE3

Compiler Vs Interpreter\
High level Language vs Low Level language\
![Image of Python interpreter](https://hackernoon.com/hn-images/0*xpjHLIxmK0fOR_4T)
![Python Virtual Machine](https://i.imgur.com/PJME67T.png)

#### Using the Help in Python3\

s=" "\
help(s.spilt)

###### without the the () in the function






# Order of Presedence [High to Low ]\

 Parentheseis ()\
 Power **\
 Mulitplication *\
 Addition  +\
 Rest Left to Right



```python
# Predict the output of the following Program 
x=1+2*3-8/4
y=16 - 2 * 5 // 3 + 1
z=2 + (3 - 1) * 10 / 5 * (2 + 3)
print(x)
```

    5.0
    14


Explanation :
16 - 2 * 5 // 3 + 1\
16 - 10 // 3 + 1\
16 - 3 + 1\
13 + 1\
14

Python3 has 33 Keywords\
C++ has 60 Keywords\
C language has 30 Keywords\
C# has 79 keywords\
Java has 51 keywords


```python
# Boolean  
print(type(True))
print(type("True"))

```

    <class 'bool'>
    <class 'str'>



```python
# Taking the Input from the User
# str,int,float 
x=(int)(input("Enter the value of the string "))
x=input("Enter the Strinf that is not type casted")
#type() function is used to tell the type of the input entered if you want to know what was entererd
print("Input value of the type,",type(x))

```

    Enter the value of the string 1
    Enter the Strinf that is not type casted1
    Input value of the type, <class 'str'>


Source [Google for Education Python](https://developers.google.com/edu/python/strings)\
Python Uses %d, %s like other languages to give output inside the print line\
Triple quotes ''' are used to contain combination of single and double quotes and can span across multiple lines\

## Usefull Inbuilt Functions

-len(variable)  is ised to tell the length of the variable in the integer format\
-square(a,b)\
-sub(a,b)



```python
# % operator
text = "%d little pigs come out, or I'll %s, and I'll %s, and I'll blow your %s down." % (3, 'huff', 'puff', 'house')
print(text)
print('''"Oh no", she exclaimed, "Ben's bike is broken!"''')

```

    3 little pigs come out, or I'll huff, and I'll puff, and I'll blow your house down.
    "Oh no", she exclaimed, "Ben's bike is broken!"



```python
# Condition statemets in Python  
x=3
if x>5:
    print(x)
elif x<4:
    print(x)
else:
    print(x)
```

    3



```python
# Try - Catch Block in python is called the try except Block
x=3
try:
    x=x+"CPU"
except:
    print("Error")
```


```python
'Ayushi'<'ayushi'
0.9999999<True
(1,2,3)<(1,2,3,4)
(1,2,3)<(1,3,2)
()<(0,)

```

Functions Using Python ,Python dosent have return type signature in its function
it just return the residual value using return


```python
#Trucated Division  - eats the value after decimal but still show the decimal
print(9 // 5)
print(9.0 // 5)

```

    1
    1.0



```python
def fn(a,b):
    print("Hello World",a+b)
fn(2,3)
```

#iterations in Python\
#while works same it does in other programming languages\
#Difference between Formal Parameters and actual parameters


```python
while True:
    if true:
        break
#break us used to break the loop
continue 
```


```python
# it takes the control to the start of the loop  
for i in [5,4,3,2,1]:
    print(i)
```


```python
for i in ["Harshit","Yadav", "Python"]: #iterating through list
    print(i)
# none value is absence of value in Python 
x=None
print(x)
```

Skipping the variable in the for loop




```python
# Both Print 0-4  
print(list(range(5)))
print(list(range(0,5)))


for _ in range(2):
    print("This line will execute three times"*2)
```

    This line will execute three timesThis line will execute three times
    This line will execute three timesThis line will execute three times



```python
# this will execute character by character of the the string provided
for character in "Cool string":
    print(character)
#for running a loop until the desired character or string is entered
grocery_item = ""
while grocery_item != "done":
    grocery_item = input("Please write down an item")
    print(grocery_item)
# to print them in s single line
print(''.join(l))

```


```python
#using the random function
#The correct code to generate a random number between 1 and 100 (inclusive)
import random

prob = random.random()
prob = random.randrange(1, 101)
```

# Lists ,String , Tuples

- String Mutation
- Mutable and Immutable
- Lists are ordered collection, where each item can be of different type
- Tuples is like lists where [] is replaced by () ,and elements are seprated by commas
- Tuples is Immutable

![String Indexing in Python](https://qph.fs.quoracdn.net/main-qimg-a380b1bc159589df5e0b9842e5b56b6d)



```python
# Printing or assigning multiline string
s="""Multiline
     String
      """
print(s)
lst=["hello", 2.0, 5, [10, 20]]
print(lst)
ls=(1,2,3)
print(type(ls))

#Printing the class character of the  Python String  
print(lst[len(lst)-1])
#or 
print(lst[-1])
#or Printing it in reverse 
print(lst[::-1])

s = "python rocks"
print(s[2] + s[-4])

# Predict the output  
L = [0.34, '6', 'SI106', 'Python', -2]
print(len(L[1:-1]))
```

    Multiline
         String
          
    ['hello', 2.0, 5, [10, 20]]
    <class 'tuple'>
    [10, 20]
    [10, 20]
    [[10, 20], 5, 2.0, 'hello']
    to
    3


## The Slice Operator

#### [starting_index:ending_index]

When we take a slice of something, it includes the item at the first index and excludes the item at the second index.



```python
fruit = "banana"
print(fruit[:3])
print(fruit[3:])
print(fruit[:])
```

    ban
    ana
    banana


# String Count Operator


```python
a = "I have had an apple on my desk before!"
print(a.count("e"))
print(a.count("ha"))
z = ['atoms', 4, 'neutron', 6, 'proton', 4, 'electron', 4, 'electron', 'atoms',[]]
print(z.count("4"))
print(z.count(4))
print(z.index("neutron"))
print(z.index([]))
print(a.index("ha"))

```

    5
    2
    0
    3
    2
    10
    2


# Splitting and Joining Strings


```python
# splitting the string into list 
song = "The rain in Spain..."
wds = song.split()
wds = song.split('ai')
print(wds)
#joining the String

```

    ['The r', 'n in Sp', 'n...']


# Conditional Statement


```python
a=3
if a<10:
    if a<9:
        print("Check")
    elif a>0:
        print("fail")
        
else:
    print("none")
```

    Check


# The in and not in operators


```python
print('p' in 'apple')
print('ap' in 'apple')
print('pa' in 'apple')
print('x' not in 'apple')
print("a" in ["a", "b", "c", "d"])
print(9 in [3, 2, 9, 10, 9.0])
print('wow' not in ['gee wiz', 'gosh golly', 'wow', 'amazing'])

```

    True
    True
    False
    True
    True
    True
    False


# Adding and Removing Items from List


```python
fruit = ["banana", "apple", "cherry"]
fruit[0] = "pear"
fruit[-1] = "orange"
fruit[1:2]= ['x', 'y']
print(fruit)
#Good one
fruit[1:2]="12"
print(fruit)
```

    ['pear', 'x', 'y', 'orange']
    ['pear', '1', '2', 'y', 'orange']


# Strings are Immutable



```python
greeting = "Hello, world!"l
greeting[0] = 'J'            # ERROR!
```

# List Element Deletion


```python
alist = ['a', 'b', 'c', 'd', 'e', 'f']
del alist[2:5]
del alist[1]
print(alist)
```

    ['a', 'f']


# Objects and References


```python
a = "banana"
b = "banana"
print(id(a)) # element id
print(id(b))
print(a is b)
```

    139843332398384
    139843332398384
    True


# Aliasing


```python
a = [81, 82, 83]
b = a
print(a is b)
```

    True



```python
alist = [4,2,8,6,5]
blist = alist * 2
print(blist)
```

    [4, 2, 8, 6, 5, 4, 2, 8, 6, 5]


# Mutating Methods

count(item) -> Returns the number of occurrences of item


```python
mylist = [1,2,3,4,5,6,7]
mylist.append(5)
mylist.insert(1, 12)
print(mylist.index(3))
print(mylist.count(5))
mylist.reverse()
mylist.sort()
del mylist[-1] #index value
mylist.remove(5) #works with strings and value
lastitem = mylist.pop()
```

    3
    2


# Non-mutating Methods on Strings

strip ->Returns a string with the leading and trailing whitespace removed\
replace(old, new) -> Replaces all occurrences of old substring with new




```python
ss = "Hello, World "
print(ss.upper())
tt = ss.lower()
print("***"+ss.strip()+"***")
news = ss.replace("o", "***")
```

    HELLO, WORLD 
    ***Hello, World***


# String Format Method


```python
scores = [("Rodney Dangerfield", -1), ("Marlon Brando", 1), ("You", 100)]
for person in scores:
    name = person[0]
    score = person[1]
    print("Hello " + name + ". Your score is " + str(score))
```

    Hello Rodney Dangerfield. Your score is -1
    Hello Marlon Brando. Your score is 1
    Hello You. Your score is 100


# String Example-2 **



```python
origPrice = float(input('Enter the original price: $'))
discount = float(input('Enter discount percentage: '))
newPrice = (1 - discount/100)*origPrice
calculation = '${:.2f} discounted by {}% is ${:.2f}.'.format(origPrice, discount, newPrice)
print(calculation)
```

    Enter the original price: $1
    Enter discount percentage: 1
    $1.00 discounted by 1.0% is $0.99.


# String Example-3


```python
winners = ['Alice Munro', 'Alvin E. Roth', 'Kazuo Ishiguro', 'Malala Yousafzai', 'Rainer Weiss', 'Youyou Tu']
winners.sort()
winners.reverse()
print(winners)
```

    ['Youyou Tu', 'Rainer Weiss', 'Malala Yousafzai', 'Kazuo Ishiguro', 'Alvin E. Roth', 'Alice Munro']


# String Example-4


```python
numbs = [5, 10, 15, 20, 25]

for i in range(len(numbs)):
    a=numbs[i]
    numbs[i]=a+5

```

    [10, 15, 20, 25, 30]


# String Example ****-5


```python
s = "ball"
r = ""
for item in s:
   r = item.upper() + r
print(r)
```

    LLAB

# Python Functions, Files, and Dictionaries

# Opening a File


```python
fileref = open("filename.txt", "r")
fileref.close()
```

# Reading from a file

- file_variable.write("Text") , adds it to the end of the file
- file_variable.read(n) , returns the string of 'n' characters or the entire file
- file_variable.readline() , returns the string upto the newline 
- file_variable.readlines() , returns a list of string upto the newline 


# Number of Lines in a Python File


```python
num_lines = sum(1 for line in open('travel_plans2.txt'))
#or
num_lines= len(open("travel_plans2.txt").readlines(  ))

```

# Using with to Open Files

- When the program exits the with block, the context manager handles the common stuff that normally happens at the end, in our case closing a file


```python
with open('mydata.txt', 'r') as md:
    for line in md:
        print(line)
# continue on with other code
```

# Writing data to a CSV File


```python
olympians = [("John Aalberg", 31, "Cross Country Skiing"),
             ("Minna Maarit Aalto", 30, "Sailing"),
             ("Win Valdemar Aaltonen", 54, "Art Competitions"),
             ("Wakako Abe", 18, "Cycling")]

outfile = open("reduced_olympics.csv", "w")
# output the header row
outfile.write('Name,Age,Sport')
outfile.write('\n')
# output each of the rows:
for olympian in olympians:
    row_string = '{},{},{}'.format(olympian[0], olympian[1], olympian[2])
    outfile.write(row_string)
    outfile.write('\n')
outfile.close()

```

# Dictionaries


```python
# Creating an Empty Dictionary 
d={}
# Creating an Empty List
l=[]

#Creating a dictionary with some elements
eng2sp = {'three': 'tres', 'one': 'uno', 'two': 2}
print(eng2sp)
```

    {'three': 'tres', 'one': 'uno', 'two': 'dos'}


# Operations on Dictionary

-  Dictionaries are mutable


```python
# delete
eng2sp['two']=0
del eng2sp['two']
# append
eng2sp['two']=3
eng2sp['two']=eng2sp['two']+2
print(eng2sp)
print(len(eng2sp))

```

    {'three': 'tres', 'one': 'uno', 'entry': 0, 'two': 5}
    4



```python
# iterating over elements in the dictionary
# Keys are not iterated in the order always
for i in eng2sp.keys():
    print(i)
for i in eng2sp.values():
    print(i)
```

    three
    one
    entry
    two
    tres
    uno
    0
    5


# Converting the the dictionary into the List


```python
# list of all the keys
l=list(eng2sp.keys())
print(l)
# list of all the values
l=list(eng2sp.values()) #values , items are same
print(l)
```

    ['three', 'one', 'entry', 'two']
    ['tres', 'uno', 0, 5]


# The in and not in operators can test if a key is in the dictionary


```python
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
if 'bananas' in inventory:
    print(inventory['bananas'])
```

    312


# The GET() method for Dictionary


```python
print(inventory.get("cherries"))
print(inventory.get("cherries",0))
```

    None
    0


# Aliasing and Copying

- Whenever two variables refer to the same dictionary object, changes to one affect the other


```python
opposites = {'up': 'down', 'right': 'wrong', 'true': 'false'}
alias = opposites
print(alias)
del opposites['up']
print(alias)
acopy=alias.copy()
del alias['true']
print(acopy)
```

    {'up': 'down', 'right': 'wrong', 'true': 'false'}
    {'right': 'wrong', 'true': 'false'}
    {'right': 'wrong', 'true': 'false'}


# Creating N-gram count of every character the book


```python
#f = open('scarlet.txt', 'r')
#txt = f.read()
txt="THis is the sample text to feed in the word processor"
# now txt is one long string containing all the characters
x = {} # start with an empty dictionary
for c in txt:
    if c not in x:
        # we have not seen this character before, so initialize a counter for it
        x[c] = 0

    #whether we've seen it before or not, increment its counter
    x[c] = x[c] + 1

print("t: " + str(x['t']) + " occurrences")
print("s: " + str(x['s']) + " occurrences")
```

    t: 5 occurrences
    s: 5 occurrences



```python
product = "iphone and android phones"
l=product.split()
lett_d={}
max_value=0
for i in l:
    for a in i:
        if a not in lett_d:
            lett_d[a]=1
        else:
            lett_d[a]=lett_d[a]+1
print(lett_d)
tmp=list(lett_d.values())
tmp=max(tmp)
print(tmp)
max_value=None
for i in lett_d:
    if lett_d[i]==tmp:
        max_value=i
        break
print(max_value)
```

    {'i': 2, 'p': 2, 'h': 2, 'o': 3, 'n': 4, 'e': 2, 'a': 2, 'd': 3, 'r': 1, 's': 1}
    4
    n


# Function docstring


```python
def sample_function():
    """this will serve as function name and example in IDE Intellisense"""
    print("Hello World")
    
sample_function()
print(type(sample_function))
```

    Hello World
    <class 'function'>


# Function Returning Value


```python
def square(x):
    y = x * x
    return y

toSquare = 10
result = square(toSquare)
print("The result of {} squared is {}.".format(toSquare, result))

```

    The result of 10 squared is 100.


# Tuples

-  Wherever python expects a single value, if multiple expressions are provided, separated by commas, they are automatically packed into a tuple


```python
julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")
# or equivalently
julia = "Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia"
print(julia[4])
```

#  Tuples as Return Values

- Functions can return tuples as return values.


```python
def circleInfo(r):
    """ Return (circumference, area) of a circle of radius r """
    c = 2 * 3.14159 * r
    a = 3.14159 * r * r
    return (c, a)

print(circleInfo(10))
```

# Tuple Assignment with Unpacking


```python
julia = "Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia"

name, surname, birth_year, movie, movie_year, profession, birth_place = julia
```

# Swapping Values between Variables


```python
a = 1
b = 2
(a, b) = (b, a)
print(a, b)
```

    2 1


# Unpacking Into Iterator Variables


```python
authors = [['Paul', 'Resnick'], ('Brad', 'Miller'), ('Lauren', 'Murphy')]
for first_name, last_name in authors:
    print("first name:", first_name, "last name:", last_name)
```

    first name: Paul last name: Resnick
    first name: Brad last name: Miller
    first name: Lauren last name: Murphy


# Enumerate


```python
fruits = ['apple', 'pear', 'apricot', 'cherry', 'peach']
for idx, fruit in enumerate(fruits):
    print(idx, fruit)
```

    0 apple
    1 pear
    2 apricot
    3 cherry
    4 peach


# Iterating of Dictionary into Tuples


```python
pokemon = {'Rattata': 19, 'Machop': 66, 'Seel': 86, 'Volbeat': 86, 'Solrock': 126}
p_names=[]
p_number=[]
for i in (pokemon.items()):
    p_names.append(i[0])
    p_number.append(i[1])

print(p_names)
print(p_number)
```

    ['Rattata', 'Machop', 'Seel', 'Volbeat', 'Solrock']
    [19, 66, 86, 86, 126]


# Unpacking Tuples as Arguments to Function Calls


```python
def add(x, y):
    return x + y

print(add(3, 4))
z = (5, 4)
#print(add(z)) # this line will cause the error  
print(add(*z))
```

    7
    9


# Break and Continue


```python
x = 0
while x < 10:
    print("we are incrementing x")
    if x % 2 == 0:
        x += 3
        continue
    if x % 3 == 0:
        x += 5
    x += 1
print("Done with our loop! X has the value: " + str(x))
```

    we are incrementing x
    we are incrementing x
    we are incrementing x
    Done with our loop! X has the value: 15


# Optional Parameters


```python
print(int("100"))
print(int("100", 10))   # same thing, 10 is the default value for the base
print(int("100", 8))     # now the base is 8, so the result is 1*64 = 64

```

[Formal Paramters as Dictionary](https://docs.python.org/3/tutorial/controlflow.html#keyword-arguments)
When a final formal parameter of the form **name is present, it receives a dictionary (see Mapping Types — dict) containing all keyword arguments except for those corresponding to a formal parameter. This may be combined with a formal parameter of the form *name (described in the next subsection) which receives a tuple containing the positional arguments beyond the formal parameter list. (*name must occur before **name.) 


# Keyword Parameters with .format


```python
names_scores = [("Jack",[67,89,91]),("Emily",[72,95,42]),("Taylor",[83,92,86])]
for name, scores in names_scores:
    print("The scores {nm} got were: {s1},{s2},{s3}.".format(nm=name,s1=scores[0],s2=scores[1],s3=scores[2]))
```

    The scores Jack got were: 67,89,91.
    The scores Emily got were: 72,95,42.
    The scores Taylor got were: 83,92,86.


# .format() method ....


```python
# but this also works!
names = ["Jack","Jill","Mary"]
for n in names:
    print("'{0}!' she yelled. '{0}! {0}, {1}!'".format(n,"say hello"))
```

    'Jack!' she yelled. 'Jack! Jack, say hello!'
    'Jill!' she yelled. 'Jill! Jill, say hello!'
    'Mary!' she yelled. 'Mary! Mary, say hello!'


# Anonymous functions with lambda expressions

- lambda arguments: expression


```python
print(lambda x: x-2)
print(type(lambda x: x-2))
print((lambda x: x-2)(6))
```

    <function <lambda> at 0x7f194824f7a0>
    <class 'function'>
    4


# Introduction: Sorting with Sort and Sorted


```python
L1 = [1, 7, 4, -2, 3]
L2 = ["Cherry", "Apple", "Blueberry"]
L1.sort()
print(L1)
```

    [-2, 1, 3, 4, 7]


# Sorted(Optional reverse parameter)


```python
def absolute(x):
    if x >= 0:
        return x
    else:
        return -x
L2 = ["Cherry", "Apple", "Blueberry"]
print(sorted(L2, reverse=True))
print(sorted(L1, reverse=True, key=absolute))
```

    ['Cherry', 'Blueberry', 'Apple']
    [7, 4, 3, -2, 1]



```python
ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']
def second_let(x):
    return x[1]
sorted_by_second_let=(sorted(ex_lst,reverse=False,key=second_let))
```

# Lambdas + Reverse Parameters


```python
nums = ['1450', '33', '871', '19', '14378', '32', '1005', '44', '8907', '16']

nums_sorted_lambda =(sorted(nums,reverse=True,key=lambda x:x[-1]))
```

# Sorting Dictionaries (keys,values,items)

- Sorting dictionaries simple example


```python
L = ['E', 'F', 'B', 'A', 'D', 'I', 'I', 'C', 'B', 'A', 'D', 'D', 'E', 'D']

d = {}
for x in L:
    if x in d:
        d[x] = d[x] + 1
    else:
        d[x] = 1

# now loop through the sorted keys
for k in sorted(d, key=lambda k: d[k], reverse=True):
      print("{} appears {} times".format(k, d[k]))
```

    D appears 4 times
    E appears 2 times
    B appears 2 times
    A appears 2 times
    I appears 2 times
    F appears 1 times
    C appears 1 times


# Sorting Dictionaries based on key Values 



```python
dictionary = {"Flowers": 10, 'Trees': 20, 'Chairs': 6, "Firepit": 1, 'Grill': 2, 'Lights': 14}
tmp=sorted(dictionary.items())
tmp2=sorted(dictionary.keys())
tmp3=sorted(dictionary.values())
print(tmp)
print(tmp2)
print(tmp3)
if (tmp)==(tmp2):
    print("Idenitcal")
sorted_keys=[]
for i in tmp:
    sorted_keys.append(i[0])
    

#print(sorted_keys)

```

    [('Chairs', 6), ('Firepit', 1), ('Flowers', 10), ('Grill', 2), ('Lights', 14), ('Trees', 20)]
    ['Chairs', 'Firepit', 'Flowers', 'Grill', 'Lights', 'Trees']
    [1, 2, 6, 10, 14, 20]


# Sorting Dictionaries based on Values


```python
dictionary = {"Flowers": 10, 'Trees': 20, 'Chairs': 6, "Firepit": 1, 'Grill': 2, 'Lights': 14}
# sorting only the values()
tmp=sorted(dictionary.values())
tmp2=sorted(dictionary.items(),reverse=False,key= lambda x:(x[1],x[0]))
print(tmp2)

sorted_keys=[]
print(tmp)
#for i in tmp:
    #sorted_keys.append(i[0])

print(sorted_keys)

```

    [('Firepit', 1), ('Grill', 2), ('Chairs', 6), ('Flowers', 10), ('Lights', 14), ('Trees', 20)]
    [1, 2, 6, 10, 14, 20]
    []



```python
groceries = {'apples': 5, 'pasta': 3, 'carrots': 12, 'orange juice': 2, 'bananas': 8, 'popcorn': 1, 'salsa': 3, 'cereal': 4, 'coffee': 5, 'granola bars': 15, 'onions': 7, 'rice': 1, 'peanut butter': 2, 'spinach': 9}

tmp=sorted(groceries.keys())
grocery_keys_sorted=[]
for i in tmp:
    grocery_keys_sorted.append(i)
    
print(grocery_keys_sorted)
```

    ['apples', 'bananas', 'carrots', 'cereal', 'coffee', 'granola bars', 'onions', 'orange juice', 'pasta', 'peanut butter', 'popcorn', 'rice', 'salsa', 'spinach']


# Breaking Ties: Second Sorting

What happens when two items are “tied” in the sort order? For example, suppose we sort a list of words by their lengths. Which five letter word will appear first?

The answer is that the python interpreter will sort the tied items in the same order they were in before the sorting


```python
fruits = ['peach', 'kiwi', 'apple', 'blueberry', 'papaya', 'mango', 'pear']
new_order = sorted(fruits, key=lambda fruit_name: (len(fruit_name), fruit_name))
for fruit in new_order:
    print(fruit)
```

    kiwi
    pear
    apple
    mango
    peach
    papaya
    blueberry


# Using the Negative Length in Python


```python
fruits = ['peach', 'kiwi', 'apple', 'blueberry', 'papaya', 'mango', 'pear']
new_order = sorted(fruits, key=lambda fruit_name: (-len(fruit_name), fruit_name))
for fruit in new_order:
    print(fruit)

```

    blueberry
    papaya
    apple
    mango
    peach
    kiwi
    pear



```python
weather = {'Reykjavik': {'temp':60, 'condition': 'rainy'},
           'Buenos Aires': {'temp': 55, 'condition': 'cloudy'},
           'Cairo': {'temp': 96, 'condition': 'sunny'},
           'Berlin': {'temp': 89, 'condition': 'sunny'},
           'Caloocan': {'temp': 78, 'condition': 'sunny'}}

sorted_weather = sorted(weather, key=lambda w: (w, -weather[w]['temp']), reverse=True)
print(sorted_weather)
```

    ['Reykjavik', 'Caloocan', 'Cairo', 'Buenos Aires', 'Berlin']


# Using Lambda vs Functions

-Though you can often use a lambda expression or a named function interchangeably when sorting, it’s generally best to use lambda expressions until the process is too complicated, and then a function should be used

### Simple Labda Expression


```python
states = {"Minnesota": ["St. Paul", "Minneapolis", "Saint Cloud", "Stillwater"],
          "Michigan": ["Ann Arbor", "Traverse City", "Lansing", "Kalamazoo"],
          "Washington": ["Seattle", "Tacoma", "Olympia", "Vancouver"]}

print(sorted(states, key=lambda state: len(states[state][0])))
```

    ['Washington', 'Minnesota', 'Michigan']


### Complex Lambda Expression


```python
def s_cities_count(city_list):
    ct = 0
    for city in city_list:
        if city[0] == "S":
            ct += 1
    return ct

states = {"Minnesota": ["St. Paul", "Minneapolis", "Saint Cloud", "Stillwater"],
          "Michigan": ["Ann Arbor", "Traverse City", "Lansing", "Kalamazoo"],
          "Washington": ["Seattle", "Tacoma", "Olympia", "Vancouver"]}

print(sorted(states, key=lambda state: s_cities_count(states[state])))
```

    ['Michigan', 'Washington', 'Minnesota']



```python
letters = "alwnfiwaksuezlaeiajsdl"
sorted_letters=sorted(letters,reverse=True)

```


```python
medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}

tmp=sorted(medals.items(),reverse=True,key=lambda x:(x[1],x[0]))
top_three=[]
for i in range(3):
    top_three.append(tmp[i][0])
    
```

    [('United States', 121), ('China', 70), ('Russia', 56), ('Germany', 42), ('Japan', 41), ('South Korea', 21)]
    [('United States', 121), ('China', 70), ('Russia', 56)]



```python
groceries = {'apples': 5, 'pasta': 3, 'carrots': 12, 'orange juice': 2, 'bananas': 8, 'popcorn': 1, 'salsa': 3, 'cereal': 4, 'coffee': 5, 'granola bars': 15, 'onions': 7, 'rice': 1, 'peanut butter': 2, 'spinach': 9}
print(len(groceries))
tmp=sorted(groceries.items(),reverse=True,key=lambda x:(x[1],x[0]))
print(len(tmp))
```

    14
    14



```python
def last_four(x):
    tmp=str(x)
    itmp=tmp[-1]+tmp[-2]+tmp[-3]+tmp[-4]
    return(str(itmp))
        

sorted_ids=[]
ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]

sorted_ids=sorted(ids,reverse=False,key=lambda x:last_four(x))

```


```python
groceries = {'apples': 5, 'pasta': 3, 'carrots': 12, 'orange juice': 2, 'bananas': 8, 'popcorn': 1, 'salsa': 3, 'cereal': 4, 'coffee': 5, 'granola bars': 15, 'onions': 7, 'rice': 1, 'peanut butter': 2, 'spinach': 9}

tmp=sorted(groceries.items(),reverse=True,key=lambda x:(x[1],x[0]))
most_needed=[]
for i in range(len(groceries)):
    most_needed.append(tmp[i][0])
```


```python
ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]

def last_four(x):
    tmp=str(x)
    itmp=tmp[-1]+tmp[-2]+tmp[-3]+tmp[-4]
    return(str(itmp))
        

sorted_ids=[]
sorted_id=sorted(ids,reverse=False,key=lambda x:last_four(x))
print(sorted_id)
```

    [17579000, 17570002, 17572342, 17573005, 17572345, 17579329]



```python
ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]
sorted_id=sorted(ids, key=lambda x: str(x)[-4:])
print(sorted_id)
```

    [17570002, 17572342, 17572345, 17573005, 17579000, 17579329]


# Test Project Sentiment Analysis 

- 1.Clean up the Data  : remove the following listed characted from the string  




```python
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']


def strip_punctuation(x):
    for i in x:
        
        print(i)
        if i in punctuation_chars:
            print("Match Found")
            x=x.replace(i,'')
    
    print(x)
    return x
strip_punctuation("#hello i am good")


```

    #
    Match Found
    h
    e
    l
    l
    o
     
    i
     
    a
    m
     
    g
    o
    o
    d
    hello i am good





    'hello i am good'




```python
a="Hello my name is HArshit"
for i in a:  
    print(i)
    
```

    H
    e
    l
    l
    o
     
    m
    y
     
    n
    a
    m
    e
     
    i
    s
     
    H
    A
    r
    s
    h
    i
    t


```python

```

# Nested Iteration

### Lists with Complex Items

- Appending the List as an element in the list 


```python
nested1 = [['a', 'b', 'c'],['d', 'e'],['f', 'g', 'h']]
nested1.append(['i'])
print(nested1)
```

    [['a', 'b', 'c'], ['d', 'e'], ['f', 'g', 'h'], ['i']]



```python
print([10, 20, 30][1])
print(nested1[1][0])
```

    20
    d


## List of Functions 



```python
def square(x):
    return x*x

L = [square, abs, lambda x: x+1]
# 3 Elements of the List per element 
print("****names****")
for f in L:
    print(f)

print("****call each of them****")
for f in L:
    print(f(-2))

print("****just the first one in the list****")
print(L[0])
print(L[0](3))
```

    ****names****
    <function square at 0x7f94484633b0>
    <built-in function abs>
    <function <lambda> at 0x7f9448463560>
    ****call each of them****
    4
    2
    -1
    ****just the first one in the list****
    <function square at 0x7f94484633b0>
    9


# Nested Dictionaries


```python
info = {'personal_data':
         {'name': 'Lauren',
          'age': 20,
          'major': 'Information Science',
          'physical_features':
             {'color': {'eye': 'blue',
                        'hair': 'brown'},
              'height': "5'8"}
         },
       'other':
         {'favorite_colors': ['purple', 'green', 'blue'],
          'interested_in': ['social media', 'intellectual property', 'copyright', 'music', 'books']
         }
      }
color=info['personal_data']['physical_features']['color']
print(color)
```

    {'eye': 'blue', 'hair': 'brown'}


# Processing JSON results

- JSON stands for JavaScript Object Notation
- json.loads() takes a string as input and produces a python object (a dictionary or a list) as output.
- json.dump() It takes a python object, typically a dictionary or a list, and returns a string, in JSON format. It has a few other parameters. Two useful parameters are sort_keys and indent. When the value True is passed for the sort_keys parameter, the keys of dictionaries are output in alphabetic order with their values. The indent parameter expects an integer. When it is provided, dumps generates a string suitable for displaying to people, with newlines and indentation for nested lists or dictionaries. For example, the following function uses json.dumps to make a human-readable printout of a nested data structure.




```python
#library for Json file
import json

a_string = '\n\n\n{\n "resultCount":25,\n "results": [\n{"wrapperType":"track", "kind":"podcast", "collectionId":10892}]}'
print(a_string)
d = json.loads(a_string)
print("------")
print(type(d))
print(d.keys())
print(d['resultCount'])


########################################################

def pretty(obj):
    return json.dumps(obj, sort_keys=True, indent=2)

d = {'key1': {'c': True, 'a': 90, '5': 50}, 'key2':{'b': 3, 'c': "yes"}}

print(d)
print('--------')
print(pretty(d))
```


​    
​    

    {
     "resultCount":25,
     "results": [
    {"wrapperType":"track", "kind":"podcast", "collectionId":10892}]}
    ------
    <class 'dict'>
    dict_keys(['resultCount', 'results'])
    25
    {'key1': {'c': True, 'a': 90, '5': 50}, 'key2': {'b': 3, 'c': 'yes'}}
    --------
    {
      "key1": {
        "5": 50,
        "a": 90,
        "c": true
      },
      "key2": {
        "b": 3,
        "c": "yes"
      }
    }


# Typechecking in Complex List Iteration


```python
nested1 = [1, 2, ['a', 'b', 'c'],['d', 'e'],['f', 'g', 'h']]
for x in nested1:
    print("level1: ")
    if type(x) is list:
        for y in x:
            print("     level2: {}".format(y))
    else:
        print(x)
```

    level1: 
    1
    level1: 
    2
    level1: 
         level2: a
         level2: b
         level2: c
    level1: 
         level2: d
         level2: e
    level1: 
         level2: f
         level2: g
         level2: h


#  Deep and Shallow Copies

- simply cloning a list using [:] would take care of any issues with having two lists unintentionally connected to each other

- That was definitely true for making shallow copies (copying a list at the highest level)
- We can have second-level aliasing in these cases, which means we need to make deep copies.
- When you copy a nested list, you do not also get copies of the internal lists. This means that if you perform a mutation operation on one of the original sublists, the copied version will also change

### in shallow copies the variable pointer pointers are different  but the data pointed by are same shared one for both of them 

### Deep Copyied list has Different  copy of the data and no sharing

# is and '==' Operator in Python

- The == operator is used when the values of two operands are equal, then the condition becomes true.
- The is operator evaluates to true if the variables on either side of the operator point to the same object and false otherwise



```python
original = [['dogs', 'puppies'], ['cats', "kittens"]]
copied_version = original[:]
print(copied_version)
print(copied_version is original)
print(copied_version == original)
original[0].append(["canines"])
print(original)
print("-------- Now look at the copied version -----------")
print(copied_version)
```

    [['dogs', 'puppies'], ['cats', 'kittens']]
    False
    True
    [['dogs', 'puppies', ['canines']], ['cats', 'kittens']]
    -------- Now look at the copied version -----------
    [['dogs', 'puppies', ['canines']], ['cats', 'kittens']]


### Assuming that you don’t want to have aliased lists inside of your nested list ,you could take advantage of the slice operator to do the copying of the inner list



```python
original = [['dogs', 'puppies'], ['cats', "kittens"]]
copied_outer_list = []
for inner_list in original:
    copied_inner_list = inner_list[:]
    copied_outer_list.append(copied_inner_list)
print(copied_outer_list)
original[0].append(["canines"])
print(original)
print("-------- Now look at the copied version -----------")
print(copied_outer_list)
```

    [['dogs', 'puppies'], ['cats', 'kittens']]
    [['dogs', 'puppies', ['canines']], ['cats', 'kittens']]
    -------- Now look at the copied version -----------
    [['dogs', 'puppies'], ['cats', 'kittens']]


# Extracting from Nested Data

Copy and paste it to a site like https://jsoneditoronline.org/ which will let you explore and collapse levels


```python
import json
print(type(res))
print(res.keys())
res2 = res['statuses']
print("----Level 2: a list of tweets-----")
print(type(res2)) # it's a list!
print(len(res2))  # looks like one item representing each of the three tweets
for res3 in res2[:1]:
   print("----Level 3: a tweet----")
   print(json.dumps(res3, indent=2)[:30])
   res4 = res3['user']
   print("----Level 4: the user who wrote the tweet----")
   print(type(res4)) # it's a dictionary
   print(res4.keys())
```

## Assignement Questions


```python
output=nested[1][2]


#Test to see if 'yellow' is in the third list of lst. Save to variable ``yellow``
yellow=( "yellow" in lst[2] )

#Test to see if 4 is in the second list of lst. Save to variable ``four``
four=(4 in lst[1])

#Test to see if 'orange' is in the first element of lst. Save to variable ``orange``

orange=("orange" in lst[0] )




# Test if 'hola' is in the list L. Save to variable name test1
test1=('hola' in L)
# Test if [5, 8, 7] is in the list L. Save to variable name test2
test2=([5, 8, 7] in L)
# Test if 6.6 is in the third element of list L. Save to variable name test3
test3=(6.6 in L[2])


nested = {'data': ['finding', 23, ['exercises', 'hangout', 34]], 'window': ['part', 'whole', [], 'sum', ['math', 'calculus', 'algebra', 'geometry', 'statistics',['physics', 'chemistry', 'biology']]]}

# Check to see if the string data is a key in nested, if it is, assign True to the variable data, otherwise assign False.
data=( 'data' in nested  )
# Check to see if the integer 24 is in the value of the key data, if it is then assign to the variable twentyfour the value of True, otherwise False.
twentyfour=(24 in nested['data'])
# Check to see that the string 'whole' is not in the value of the key window. If it's not, then assign to the variable whole the value of True, otherwise False.
whole=('whole' not in nested['window'] )
# Check to see if the string 'physics' is a key in the dictionary nested. If it is, assign to the variable physics, the value of True, otherwise False.

physics=('physics' in nested)


sports = {'swimming': ['butterfly', 'breaststroke', 'backstroke', 'freestyle'], 'diving': ['springboard', 'platform', 'synchronized'], 'track': ['sprint', 'distance', 'jumps', 'throws'], 'gymnastics': {'women':['vault', 'floor', 'uneven bars', 'balance beam'], 'men': ['vault', 'parallel bars', 'floor', 'rings']}}

# Assign the string 'backstroke' to the name v1
v1=sports['swimming'][2]
# Assign the string 'platform' to the name v2
v2=sports['diving'][1]
# Assign the list ['vault', 'floor', 'uneven bars', 'balance beam'] to the name v3
v3 = sports['gymnastics']['women']
# Assign the string 'rings' to the name v4

v4 = sports['gymnastics']['men'][3]


nested_d = {'Beijing':{'China':51, 'USA':36, 'Russia':22, 'Great Britain':19}, 'London':{'USA':46, 'China':38, 'Great Britain':29, 'Russia':22}, 'Rio':{'USA':35, 'Great Britain':22, 'China':20, 'Germany':13}}

US_count = []
for i in nested_d:
    US_count.append(nested_d[i]['USA'])
```

# Map and Filter

#### Example of Map


```python
def triple(value):
    return 3*value

def tripleStuff(a_list):
    new_seq = map(triple, a_list)
    return list(new_seq)

def quadrupleStuff(a_list):
    new_seq = map(lambda value: 4*value, a_list)
    return list(new_seq)

things = [2, 5, 9]
things3 = tripleStuff(things)
print(things3)
things4 = quadrupleStuff(things)
```

    [6, 15, 27]


#### Example


```python
lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]
greeting_doubled=map(lambda x:x*2,lst)

```

# Filter

##### Example 


```python
# eleminate the value that are fale to the condition
lst_check=["wonder","orange"]
filter_testing=filter(lambda x: 'w' in x,lst_check)
```

# List Comprehension

- Python provides an alternative way to do map and filter operations, called a list comprehension  

#### Examples



```python
# [<transformer_expression> for <loop_var> in <sequence> if <filtration_expression>]
# Example 1
things = [2, 5, 9]
yourlist = [value * 2 for value in things]
print(yourlist)

# Example 2
def keep_evens(nums):
    new_list = [num for num in nums if num % 2 == 0]
    return new_list

print(keep_evens([3, 4, 6, 7, 0, 1]))

#Example 3
things = [3, 4, 6, 7, 0, 1]
print(map(lambda x: x*2, filter(lambda y: y % 2 == 0, things)))

# equivalent version using list comprehension
print([x*2 for x in things if x % 2 == 0])


```

    [4, 10, 18]


### List Comprehension In Dictionaries


```python
tester = {'info': [{"name": "Lauren", 'class standing': 'Junior', 'major': "Information Science"},{'name': 'Ayo', 'class standing': "Bachelor's", 'major': 'Information Science'}, {'name': 'Kathryn', 'class standing': 'Senior', 'major': 'Sociology'}, {'name': 'Nick', 'class standing': 'Junior', 'major': 'Computer Science'}, {'name': 'Gladys', 'class standing': 'Sophomore', 'major': 'History'}, {'name': 'Adam', 'major': 'Violin Performance', 'class standing': 'Senior'}]}
l=tester['info']
compri=[d['name'] for d in l]

```

# Zip 

-The zip function takes multiple lists and turns them into a list of tuples (actually, an iterator, but they work like lists for most practical purposes),


```python
# Simple Implementation  
L1 = [3, 4, 5]
L2 = [1, 2, 3]
L3 = []

for i in range(len(L1)):
    L3.append(L1[i] + L2[i])

print(L3)

```

    [4, 6, 8]


### iterating thorough loop


```python
L1 = [3, 4, 5]
L2 = [1, 2, 3]
L3 = []
L4 = list(zip(L1, L2))

for (x1, x2) in L4:
    L3.append(x1+x2)

print(L3)
```

    [4, 6, 8]


## Zip + List Comprehension


```python
L1 = [3, 4, 5]
L2 = [1, 2, 3]
L3 = [x1 + x2 for (x1, x2) in list(zip(L1, L2))]
print(L3)
```

    [4, 6, 8]


## Map + Lambda +Zip


```python
L1 = [3, 4, 5]
L2 = [1, 2, 3]
L3 = map(lambda x: x[0] + x[1], zip(L1, L2))
print(L3)


L1 = [1, 5, 2, 16, 32, 3, 54, 8, 100]
L2 = [1, 3, 10, 2, 42, 2, 3, 4, 3]
L3=[x1+x2 for (x1,x2) in list(zip(L1,L2)) if x1 >10 and x2<5 ]


```

    <map object at 0x7f2f947adb90>



```python
l1 = ['left', 'up', 'front']
l2 = ['right', 'down', 'back']
l3 = zip(l1, l2)
opposites=list(filter(lambda s:len(s[0])>3 and len(s[1]) >3 ,l3))
```

# Classes and Inheritance

#### User Defined Classes

- Every class should have a method with the special name __init__. This initializer method, often referred to as the constructor, is automatically called whenever a new instance of Point is created. It gives the programmer the opportunity to set up the attributes required within the new instance by giving them their initial state values

- It gives the programmer the opportunity to set up the attributes required within the new instance by giving them their initial state values. The self parameter (you could choose any other name, but nobody ever does!) is automatically set to reference the newly created object that needs to be initialized




```python
class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self):
        """ Create a new point at the origin """
        self.x = 0
        self.y = 0
        
p = Point()         # Instantiate an object of type Point
q = Point()         # and make a second point

print("Nothing seems to have happened with the points")

```

## Adding Parameters to the Constructor




```python
class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

p = Point(7,6)


```

## Adding Other Methods to a Class


```python
class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5


p = Point(7,6)
print(p.distanceFromOrigin())
```

### Converting an Object to a String

- The """__str__""" method is responsible for returning a string representation as defined by the class creator. 
- Whatever string the __str__ method for a class returns, that is the string that will print when you put any instance of that class in a print statement.



```python
class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __str__(self):
        return "x = {}, y = {}".format(self.x, self.y)

p = Point(7,6)
print(p)
```

    x = 7, y = 6


### Sorting List of Instance


```python
L = ["Cherry", "Apple", "Blueberry"]
print(sorted(L, key=len))
print(sorted(L, key= lambda x: len(x)))

class Fruit():
    def __init__(self, name, price):
        self.name = name
        self.price = price

L = [Fruit("Cherry", 10), Fruit("Apple", 5), Fruit("Blueberry", 20)]
for f in sorted(L, key=lambda x: x.price):
    print(f.name)
    
```


```python
### Calling Functions of a class with its object
```


```python
class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    printed_rep = "*"

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

    def graph(self):
        rows = []
        size = max(int(self.x), int(self.y)) + 2
        for j in range(size-1) :
            if (j+1) == int(self.y):
                special_row = str((j+1) % 10) + (" "*(int(self.x) -1)) + self.printed_rep
                rows.append(special_row)
            else:
                rows.append(str((j+1) % 10))
        rows.reverse()  # put higher values of y first
        x_axis = ""
        for i in range(size):
            x_axis += str(i % 10)
        rows.append(x_axis)

        return "\n".join(rows)


p1 = Point(2, 3)
p2 = Point(3, 12)
print(p1.graph())
print()
print(p2.graph())

```

# Tamagotchi


```python
from random import randrange

class Pet():
    boredom_decrement = 4
    hunger_decrement = 6
    boredom_threshold = 5
    hunger_threshold = 10
    sounds = ['Mrrp']
    def __init__(self, name = "Kitty"):
        self.name = name
        self.hunger = randrange(self.hunger_threshold)
        self.boredom = randrange(self.boredom_threshold)
        self.sounds = self.sounds[:]  # copy the class attribute, so that when we make changes to it, we won't affect the other Pets in the class

    def clock_tick(self):
        self.boredom += 1
        self.hunger += 1

    def mood(self):
        if self.hunger <= self.hunger_threshold and self.boredom <= self.boredom_threshold:
            return "happy"
        elif self.hunger > self.hunger_threshold:
            return "hungry"
        else:
            return "bored"

    def __str__(self):
        state = "     I'm " + self.name + ". "
        state += " I feel " + self.mood() + ". "
        # state += "Hunger {} Boredom {} Words {}".format(self.hunger, self.boredom, self.sounds)
        return state

    def hi(self):
        print(self.sounds[randrange(len(self.sounds))])
        self.reduce_boredom()

    def teach(self, word):
        self.sounds.append(word)
        self.reduce_boredom()

    def feed(self):
        self.reduce_hunger()

    def reduce_hunger(self):
        self.hunger = max(0, self.hunger - self.hunger_decrement)

    def reduce_boredom(self):
        self.boredom = max(0, self.boredom - self.boredom_decrement)

```

## Inheritance


```python
from random import randrange

# Here's the original Pet class
class Pet():
    boredom_decrement = 4
    hunger_decrement = 6
    boredom_threshold = 5
    hunger_threshold = 10
    sounds = ['Mrrp']
    def __init__(self, name = "Kitty"):
        self.name = name
        self.hunger = randrange(self.hunger_threshold)
        self.boredom = randrange(self.boredom_threshold)
        self.sounds = self.sounds[:]  # copy the class attribute, so that when we make changes to it, we won't affect the other Pets in the class

    def clock_tick(self):
        self.boredom += 1
        self.hunger += 1

    def mood(self):
        if self.hunger <= self.hunger_threshold and self.boredom <= self.boredom_threshold:
            return "happy"
        elif self.hunger > self.hunger_threshold:
            return "hungry"
        else:
            return "bored"

    def __str__(self):
        state = "     I'm " + self.name + ". "
        state += " I feel " + self.mood() + ". "
        # state += "Hunger %d Boredom %d Words %s" % (self.hunger, self.boredom, self.sounds)
        return state

    def hi(self):
        print(self.sounds[randrange(len(self.sounds))])
        self.reduce_boredom()

    def teach(self, word):
        self.sounds.append(word)
        self.reduce_boredom()

    def feed(self):
        self.reduce_hunger()

    def reduce_hunger(self):
        self.hunger = max(0, self.hunger - self.hunger_decrement)

    def reduce_boredom(self):
        self.boredom = max(0, self.boredom - self.boredom_decrement)

# Here's the new definition of class Cat, a subclass of Pet.
class Cat(Pet): # the class name that the new class inherits from goes in the parentheses, like so.
    sounds = ['Meow']

    def chasing_rats(self):
        return "What are you doing, Pinky? Taking over the world?!"
    
class Cheshire(Cat): # this inherits from Cat, which inherits from Pet

    def smile(self): # this method is specific to instances of Cheshire
        print(":D :D :D")

# Let's try it with instances.
cat1 = Cat("Fluffy")
cat1.feed() # Totally fine, because the cat class inherits from the Pet class!
cat1.hi() # Uses the special Cat hello.
print(cat1)

print(cat1.chasing_rats())

new_cat = Cheshire("Pumpkin") # create a Cheshire cat instance with name "Pumpkin"
new_cat.hi() # same as Cat!
new_cat.chasing_rats() # OK, because Cheshire inherits from Cat
new_cat.smile() # Only for Cheshire instances (and any classes that you make inherit from Cheshire)

# cat1.smile() # This line would give you an error, because the Cat class does not have this method!

# None of the subclass methods can be used on the parent class, though.
p1 = Pet("Teddy")
p1.hi() # just the regular Pet hello
#p1.chasing_rats() # This will give you an error -- this method doesn't exist on instances of the Pet class.
#p1.smile() # This will give you an error, too. This method does not exist on instances of the Pet class.


```

## Overriding Methods

-  If a method is defined for a class, and also defined for its parent class, the subclass’ method is called and not the parent’s.


## Invoking the Parent Class’s Method

-Missing



# Python Test Case :

- A test case expresses requirements for a program, in a way that can be checked automatically. Specifically, a test asserts something about the state of the program at a particular point in its execution

- Python provides a statement called assert.

Following the word assert there will be a python expression.

- If that expression evaluates to the Boolean False, then the interpreter will raise a runtime error.

A useful function will do some combination of three things, given its input parameters:

- Return a value. For these, you will write return value tests.

- Modify the contents of some mutable object, like a list or dictionary. For these you will write side effect tests.

- Print something or write something to a file. Tests of whether a function generates the right printed output are beyond the scope of this testing framework; you won’t write these tests.


```python
def square(x):
    return x*x

assert square(3) == 9

```


```python
def update_counts(letters, counts_d):
    for c in letters:
        counts_d[c] = 1
        if c in counts_d:
            counts_d[c] = counts_d[c] + 1


counts = {'a': 3, 'b': 2}
update_counts("aaab", counts)
# 3 more occurrences of a, so 6 in all
assert counts['a'] == 6
# 1 more occurrence of b, so 3 in all
assert counts['b'] == 3
```


    ---------------------------------------------------------------------------
    
    AssertionError                            Traceback (most recent call last)
    
    <ipython-input-7-3042d7a07621> in <module>
          9 update_counts("aaab", counts)
         10 # 3 more occurrences of a, so 6 in all
    ---> 11 assert counts['a'] == 6
         12 # 1 more occurrence of b, so 3 in all
         13 assert counts['b'] == 3


    AssertionError: 



```python
def distance(x1, y1, x2, y2):
    return None

assert distance(1, 2, 1, 2) == 0


```


    ---------------------------------------------------------------------------
    
    AssertionError                            Traceback (most recent call last)
    
    <ipython-input-1-817e0079736d> in <module>
          2     return None
          3 
    ----> 4 assert distance(1, 2, 1, 2) == 0
          5 


    AssertionError: 


# Testing Classes


```python
class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy


#testing class constructor (__init__ method)
p = Point(3, 4)
assert p.y == 4
assert p.x == 3

#testing the distance method
p = Point(3, 4)
assert p.distanceFromOrigin() == 5.0

#testing the move method
p = Point(3, 4)
p.move(-2, 3)
assert p.x == 1
assert p.y == 7

```

## Exception Handling Flow-of-control

- Try Except


```python
try:
    items = ['a', 'b']
    third = items[2]
    print("This won't print")
except Exception:
    print("got an error")

print("continuing")

```

    got an error
    continuing



```python
try:
    items = ['a', 'b']
    third = items[2]
    print("This won't print")
except Exception as e:
    print("got an error")
    print(e)

print("continuing")

```

    got an error
    list index out of range
    continuing



```python

```


```python

```

## Python Resources and List

- [Automate Boring Stuff with Python](https://automatetheboringstuff.com/2e/chapter1/)

- [Microsft Python for Beginners web Series](https://www.youtube.com/playlist?list=PLlrxD0HtieHhS8VzuMCfQD4uJ9yne1mE6)



