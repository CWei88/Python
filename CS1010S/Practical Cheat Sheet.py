#CS1010S PE Cheatsheet
import math

##################
###Introduction###
#################

##Types##
int
str
float
bool
None

#To convert
#int('5') = 5
#int('hi') = Error

##Operators##
x = 5
y = 3

print(x + y) #Adds x + y
print(x - y) #Subtracts x and y
print(x * y) #Multiplies x by y
print(x / y) #Divides x by y
print(x**y)  #Finds x to the power of y
print(x//y)  #Rounds down the result of x/y
print(x%y)   #Finds the remainder of x/y

##Strings##
x = "That is cool"
y = "That"
z = "Thas"
x > y #True as x has a space
z < y #True as s < t

##Conditionals##
def foo(x,y,z):
    if x < z:
        return y
    elif x > z:
        return z
    else:
        return x

##############################
### Functional Abstraction ###
##############################

##Backslash##
## Either ignore letter behind or continues code to the next line"
"That\s"
"Help\
     me"

##Function##
def foo(x):
    return x + x

##Anonymous Functions##
lambda x: x + x

##Variable Scoping##
x = 10

def square(x):
    return x * x #x here is bound to the function square

def addx(y):
    return y + x #x here will be taken from the x outside the function as the
                 #function does not bind the x. Hence, x = 10

##Block Structure##
def hypotenuse(a,b):
    def sum_of_squares():
        return square(a) + square(b) #Refers to parameter of hypotenuse
    return math.sqrt(sum_of_squares())


################################################
### Recursion, Iteration and Order of Growth ###
################################################

##Recursion
def fib(n):
    if n == 0: #base case
        return 0
    elif n == 1: #base case
        return 1
    else:
        return fib(n - 1) + fib(n - 2) #Recursively calling the function

##Mutual Recursion
# When a function calls another function which calls back itself
def ping(n):
    if n == 0:
        return n
    else:
        print("Ping")
        pong(n - 1)

def pong(n):
    if n == 0:
        return n
    else:
        print("Pong")
        ping(n - 1)

ping(10)

##Iteration
## While loop
def factorial_while(n):
    p, c = 1, 1
    while c <= n: #while the condition is satisfied
        p = p * c
        c += 1 #increments c such that it will not be in a infinite loop
    return p
#Time : O(n)
#Space: O(1)

## For loop
def factorial_for(n):
    p = 1
    for i in range(2, n + 1): #range is inclusive for start and non-inclusive for stop
        p = p * i
    return p

## Range function
# range(1,n) creates a sequence of integers from start to stop, not including
# stop. The function range has the parameters range([start], stop, [step])
# where [] is optional

## Break and continue
for j in range(10):
    print(j)
    if j == 3:
        break #when condition is met, the loop will be broken
print("done")

for i in range(10):
    if i%2 == 1: #when condition is met, the loop will continue with the next value
        continue
    print(i)
print("done")

## Loop in a loop
def floyd_row(n):
    result = []
    count = 1
    
    for i in range(1, n + 1):
        inter = []
        for j in range(1, i + 1):
            inter.append(count)
            count = count + 1
        result.append(tuple(inter))
    final = tuple(result)
    return final[n - 1]

#############################
### Higher Order Functions###
#############################

##Importing Modules
import math #to call a function in math, must use math.ceil
from numpy import * #we can directly call the function inside numpy
from matplotlib import pyplot as plt # we can only use the pyplot function

## Count Change
def cc(amount, kinds_of_coins):
    if amount == 0:
        return 1
    elif amount < 0 or kinds_of_coins == 0:
        return 0
    else:
        return cc(amount - first_denomination(kinds_of_coins), kinds_of_coins) + cc(amount, kinds_of_coins - 1)

def first_denom(kinds_of_coins):
    return kinds_of_coins[-1]

def count_change(amount):
    return cc(amount, 5)

##Higher Order Function
def sum_n(term, a, other, b):
    if a > b:
        return 0
    else:
        return term(a) + sum_n(term, a, other, b)

##E.g.
def sum_cubes(a, b):
    return sum_n(lambda x: x + 1, a, lambda x: x**3, b)

##Integral
def integral(f, a, b, dx):
    def add_dx(x):
        return x + dx
    return dx * sum_n(f, a+(dx/2), add_dx, b)

##Closures
def make_x(x):
    return lambda : x
five = make_x(5)
five
five()

########################
### Data Abstraction ###
########################

## Rational Number Data Abstraction
def make_rat(n,d):
    return (n,d)
def numer(rat):
    return rat[0]
def denom(rat):
    return rat[1]
def equal_rat(x, y):
    return numer(x) * denom(y) == numer(y) * denom(x)
        
## Tuples
x = (1,2)
x[0] # 1
x[1] # 2
y = (3,4)
z = (x,y)
z[0][0] # 1
z[1][1] # 4

##Tuple addition
x += (3,) #(1,2,3)
x += (4,5) #(1,2,3,4,5)
a = () #Empty Tuple

##Iterating over tuples
b = (4,2,1,3)
count = 0
for i in b:
    print(i)
    count += i
print(count)

## Equality
# Identity, We use the function is
# Equivalence, we use ==
x = 2
y = 2
z = x
w = 3
z is x #True
z == x #True
z == y #True
z == w #False
z is y #False

##############################
### Working with Sequences ###
##############################

##Reversal
def reverse(seq):
    if len(seq) == 0:
        return ()
    else:
        reverse(seq[1:]) + (seq[0],)
#Time: O(n**2)
#Space: O(n**2)
def reverse_iter(seq):
    result = ()
    for item in seq:
        result = (item,) + result
    return result
#Time: O(n**2)
#Space: O(n)

##mapping
def scale_seq(seq, factor):
    return tuple(map(lambda x: x * factor, seq))

##Counting leaves
def count_leaves(tree):
    if tree == ():
        return 0
    elif is_leaf(tree):
        return 1
    else:
        return count_leaves(tree[0]) + count_leaves(tree[1:])

def is_leaf(tree):
    return type(tree) != tuple

## Mapping over trees
def scale_tree(tree, factor):
    def scale_func(subtree):
        if is_leaf(subtree):
            return factor * subtree
        else:
            return scale_tree(subtree, factor)
    return tuple(map(scale_func, tree))

#Enumerating over a tree
def enumerate_tree(tree):
    if tree == ():
        return ()
    elif is_leaf(tree):
        return (tree,)
    else:
        return enumerate_tree(tree[0]) + enumerate_tree(tree[1:])

#Accumulating a result
def accumulate(fn, initial, seq):
    if seq == ():
        return initial
    else:
        return fn(seq[0], accumulate(fn, initial, seq[1:]))

### Example Filtering
def windest_location(fname, year):
    weather = read_csv(fname)
    temp_dict = {}
    filtered_weather = filter(lambda x: x[1] == str(year), weather[1:])

    for row in filtered_weather:
        month = row[2]
        if month not in temp_dict:
            temp_dict[month] = {}

        location = row[0]
        months = temp_dict[month]
        if location not in months:
            months[location] = [float(row[4])] #implement a list
        else:
            months[location].append(float(row[4]))

    for month, location in temp_dict.items():
        for key, value in location.items():
            location[key] = round(sum(value)/len(value), 2) #find average value from list

        temp_dict[month] = max(location.items(), key = lambda x: x[1]) #list a tuple by sorting x:x[1] value

    return temp_dict

##Example mapping
def gadgets_owned(self):
    return tuple(map(lambda x: x.name, self.gadgets))

## Working with files
# Reading a file
def readfile(fname):
    return open(fname, 'r')

#writing to a file
def write_file(fname):
    return open(fname, 'w')

#############################
### Searching and Sorting ###
#############################

## List Functions ##
lst = [1,2,3]
lst2 = [5,6,7,8]
lst.append(4) #[1,2,3,4]
lst.extend(lst2) #[1,2,3,4,5,6,7,8]
#Same As lst += lst2 but not lst = lst + lst2
del lst[0] #Takes in an index and deletes the element at that index #[2,3,4,5,6,7,8]
lst.copy() #Returns a shallow copy of the list
lst.insert(0,1) #Takes a (pos, ele) and insert ele into pos.
lst.pop(0) #Takes in an index and removes element at pos. If pos is omitted, it removes the last element
lst.remove(1) #Removes first occurence of element
lst.clear() #Clears the list.
lst.reverse() #Reverses order of list.

## Searching
# Linear Search
def search(x, lst):
    for ele in lst:
        if x == ele:
            return True
        return False
#Time: O(n)

# Binary Search
def binary_search(key, seq):
    def helper(low, high):
        if low > high:
            return False
        mid = (low + high)//2
        if key == seq[mid]:
            return True
        elif key < seq[mid]:
            return helper(low, mid - 1)
        else:
            return helper(mid + 1, high)
    return helper(0, len(seq - 1))

## Sorting
# Selection Sort
def select_sort(seq):
    sort = []
    while seq:
        smallest = seq[0]
        for ele in seq:
            if ele < smallest:
                smallest = ele
        a.remove(smallest)
        sort.append(smallest)

# Merge Sort
def merge_sort(lst):
    if len(lst) < 2:
        return lst
    mid = len(lst)//2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)

def merge(left, right):
    results = []
    while left and right:
        if left[0] < right[0]:
            results.append(left.pop(0))
        else:
            results.append(right.pop(0))
    results.extend(left)
    results.extend(right)
    return results

# Python sort
lst.sort(key = lambda x: x[0], reverse = True)
# key specifies which argument to extract as a key from a list element
# reverse indicates if the list is sorted in ascending or descending order.


####################################
### Implementing Data Structures ###
####################################

## Stacks
# A stack is a data structure with a LIFO property.
def make_stack():
    return []
def push(s, item):
    s.insert(0, item)
def pop(s):
    s.pop(0)
def is_empty(s):
    return not s

## Sets
# An unordered collection of objects without duplicates
{3,1,2} == {1,2,3} # True
# {1,1} will throw an error

##Unordered lists
# Constructors
def make_set():
    return []

# Predicates
def is_empty_set(s):
    return not s
def is_element_of_set(x,s):
    if x in s:
        return True
    return False
# Time: O(n)

#Constructors
def adjoin_set(x,s):
    if not is_element_of_set(x,s):
        s.append(x)
    return s
#Time: O(n)

def intersection_set(s1, s2):
    result = []
    for ele in s1:
        if ele in s2:
            result.append(ele)
    return result

## Ordered lists
def is_element_of_set(x,s):
    if is_empty_set(s):
        return False
    for e in s:
        if e == x:
            return True
        elif e > x:
            return False
    return False

#Time: O(n), but faster than previous implementation

def intersection_set(s1, s2):
    result = []
    i, j = 0,0
    while i < len(s1) and j < len(s2):
        if s1[i] == s2[j]:
            result.append(s1[i])
            i += 1
            j += 1
        elif s1[i] < s2[j]:
            i += 1
        else:
            j += 1
    return result
# Time: O(n)

## Binary Tree
def make_tree(entry, left, right):
    return (entry, left, right)

def entry(tree):
    return tree[0]

def left_branch(tree):
    return tree[1]

def right_branch(tree):
    return tree[2]

def adjoin_set(x, s):
    if is_empty_set(s):
        return make_tree(x, [], [])
    elif x == entry(s):
        return s
    elif x < entry(s):
        return make_tree(entry(s), adjoin_set(x, left_branch(s)), right_branch(s))
    else:
        return make_tree(entry(s), left_branch(s), adjoin_set(x, right_branch(s)))


##########################
### Generic Operations ###
##########################

## Generic Operators
def real_part(z):
    if is_rectangular(z):
        return real_part_rectangular(contents(z))
    elif is_polat(z):
        return real_part_polar(contents(z))
    else:
        raise Exception ("Unknown type -- real_part" + z)
# Type checking and tag removal are hidden from the user.

## Dictionaries
weather = {'wind':0, 'desc':'cloudy', 'temp':[25.5,29.0],'rainfall': {2:15, 15:7, 18:22}}
dict([(1,2), (3,4), (5,6)]) #Taking in a sequence of pairs to form a dictionary
weather['temp'] #[25.5, 29.0]
'wind' in weather #Check if key exists
weather['nice'] = True #adds an entry
del weather['desc'] #deletes an entry
list(weather.keys()) #Returns the keys of a dictionary
list(weather.values()) #Retunes the values of a dictionary

#Looping Construct
for key in weather:
    print(weather[key]) #print keys from weather

for key, value in weather.items():
    print(key,value) #return a key value pair

#filtering dictionary in place
needed_keys = {"Male", "Female"}
all_keys = []
for key in sex.keys():
    all_keys.append(key)

unwanted = set(all_keys) - needed_keys
for unwant in unwanted:
    del sex[unwant] 

weather.clear() #deletes all entries

## Table implementation
def put(op, types, proc):
    if op not in procs:
        procs[op] = {}
    procs[op][types] = proc

def get(op, types):
    return procs[op][types]

## * notation
def f(x,y,*z): #z can take in an arbitrary number of funtions
    return (x,y,z)

def foo(op, args):
    return (op, *args) #it will expand args out of its sequence to its individual elements

def apply_generic(op, *args):
    type_tags = tuple(map(type_tag, args))
    proc = get(op, type_tags)
    return proc(*args)

## Message Passing
def make_from_real_imag(x,y):
    def dispatch(op):
        if op == "real_part":
            return x
        elif op == "imag_part":
            return y
        elif op == "magnitude":
            return math.hypot(x,y)
        elif op == "angle":
            return math.atan(y/x)
        else:
            raise Exception ("Unknown op -- make_from_real_img " + op)
    return dispatch
#dispatch accepts a message op and performs the necessary action according to the op

###################################
### Object-oriented Programming ###
####################################

## Variable Scoping
x = 10
def bar():
    print(x) #10

x = 10
def foo():
    x = 5
    print(x) #5

# However, we cannot edit x if x is defined outside of the scope of the function.
def adder(x):
    def do():
        nonlocal x
        x += 1
        print(x)
    return do
# However, lists works as it rebinds the first element of x instead of x.
x = [10]
def bar():
    print(x)
    x[0] += 1

## OOP
class BankAccount(object):
    def __init__ (self, initial_balance): #created when first initialized
        self.balance = initial_balance

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
            return self.balance
        else:
            return "Insufficient Funds"

    def deposit(self, amount):
        self.balance += amount
        return self.balance

## Inheritance
class NamedObject(object):
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

class MobileObject(NamedObject):
    def __init__(self, name, location):
        super().__init__(name)
        self.location = location

#Note that a subclass inherits all of the superclass methods, hence, MobileObject is able to use get_name.

## isinstance vs Type

x = MobileObject('x', 10)
y = NamedObject('y')
isinstance(x, MobileObject) #True
type(x) == MobileObject # True
isinstance(x, NamedObject) #True
type(x) == NamedObject # False
type(y) == NamedObject # True

## Multiple inheritance
class A(object):
    def __init__ (self, name):
        self.name = name

class B(object):
    def __init__ (self, height):
        self.height = height

class C(A, B):
    def __init__(self, name, height):
        super().__init__(name)
        super().__init__(height)

# If a function is called that is not in Class C, it will first look in A then B.

## Diamond Inheritance
class D(A):
    def __init__(self, name):
        super().__init__(name)

    def talk(self):
        return "Hi"

class E(A):
    def __init__(self, name):
        super().__init__(name)

    def talk(self):
        return "I'm tall"

def F(D, E):
    def __init__(self,name):
        super().__init__(name)

    def talk(self):
        super().talk()

# For this case, F will first invoke D's say first. Then as all the subclass
# methods needs to be used before the superclass, it will then invoke E's say
# before invoking A.

##########################################
### Memoization, DP and Error Handling ###
##########################################

## Memoize
memoize_table = {}
def memoize(f, name):
    if name not in memoize_table:
        memoize_table[name] = {}

    table = memoize_table[name]
    def helper(*args):
        if args in table:
            return table[args]
        else:
            result = f(*args)
            table[args] = result
            return result
    return helper

def memo_fib(n):
    def helper(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return memo_fib(n-1) + memo_fib(n-2)
    return memoize_table(helper, "memo_fib")(n)

## Dynamic Programming
# Choose
def dp_choose(n,k):
    row = [1] * [k+1]
    table = []
    for i in range(n + 1):
        table.append(row.copy())

    for j in range(1, k + 1):
        table[0][j] = 0

    for i in range(1, n + 1):
        for j in range(1, k + 1):
            table[i][j] = table[i - 1][j - 1] + table[i - 1][j]

    return table[n][k]

## Errors and Exceptions

## Syntax Errors
#while True print("hello world")

## Zero Division Errors
1/0

## Name Error
4 + spam * 3

## Type Error
'2' + 2

## Value Error
int('one')

## Try Except
def divide_test(x,y):
    try:
        result = x/y
    except ZeroDivisionError: #if zero error occurs
        print("division by zero!")
    else:
        print("result is", result) 
    finally:
        print("executing finally clause") #always executed

## Raising Errors
raise NameError("Hi There")

## User defined Exceptions
# Note that all exceptions must be inherited from the exception class.
class MyError(Exception):
    def __init__ (self, value):
        self.value = value

    def __str__ (self):
        return repr(self.value) #returns printable representation of object

try:
    raise MyError(2*2)
except MyError as e:
    print("Exception Value:", e.value)


