############################################################################################################
######################################### CREATING LISTS ###################################################
############################################################################################################

# These statements are equivalent and both create an empty list:
A = []
A = list()

# A list can be assigned items at creation, for example:
A = [1, 4, 6, 9]

# List can also be created from an existing sequence:
B = [1, 2, 3, 4]
A = list(B)

# NOTE: Expression A = list(B) from the above example and A = B are not equivalent - the former
# creates a new list, while the latter assignes the same list to another name it does not create
# a new list), e.g.:
B = [1, 2, 3, 4]
A = B # Both A and B point to the same list

print("B:", B) # Prints "1, 2, 3, 4"
print("A = B: ", A) # Prints "1, 2, 3, 4"

B.append(5) # Adds element 5 at the end of the list
print("Appended 5 to B.")
print("B: ", B)    # Prints "1, 2, 3, 4, 5"
print("A: ", A)    # Prints "1, 2, 3, 4, 5"

B = [1, 2, 3, 4]
A = list(B)

print("")

print("B:", B)            # Prints "1, 2, 3, 4"
print("A = list(B): ", A) # Prints "1, 2, 3, 4"

B.append(5)        # Adds element 5 at the end of the list
print("Appended 5 to B.")
print("B: ", B)    # Prints "1, 2, 3, 4, 5"
print("A: ", A)    # Prints "1, 2, 3, 4"

# To get length of the list use len(L), where L is a list:
len(A) == 4

# To check whether an element is in the list use the in statement:
1 in A  # True
10 in A # False

############################################################################################################
####################################### ACCESSING LIST ELEMENTS ############################################
############################################################################################################

names = [ "Dave", "Mark", "Ann", "Phil" ]

# Lists are indexed by integers, starting with zero. Use the indexing operator to access and
# modify individual items of the list:
a = names[2]        # Returns the third item of the list, "Ann"
names[0] = "Jeff"   # Changes the first item to "Jeff"

# List elements can also be indexed by negative indices starting with -1 (index of the last
# element in the list) to -len(list) (index of the first element in the list)
names[-1] == names[len(names) - 1]
names[-len(names)] == names[0]

# Lists can contain elements of mixed types, including other lists and sequences.
A = [1, 2, "Dave", True, [2.3, 15, False]]

# In order of accessing 2nd element of the inner list, we need to use index of that list
# in the outer list and then the index of the element we wish to acces:
A[-1][1] == 15

############################################################################################################
######################################### LIST OPERATORS ###################################################
############################################################################################################

# Concatenation is performed with + operator (the result is a new list):
A = [1, 2, 3]
B = [4, 5, 6]
C = A + B
C == [1, 2, 3, 4, 5, 6]
C += [7, 8, 9]
C == [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Repetition if performed with * operator. Expression for repetition is <number> * <list> or <list> * <number>.
# The result is a new list that is ceated by joining <number> of <ists>-s (the result is a new list):
A = [1, 2, 3]
B = 4 * A
C = A * 4
B == C
B == [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
D = [1, 2]
D *= 3
D == [1, 2, 1, 2, 1, 2]

############################################################################################################
########################################## LIST METHODS ####################################################
############################################################################################################
# NOTE: These do not create a new list. They just change an existing one.

# list.append(x) adds an element to the end of the list:
A = [1, 2, 3, 4]
A.append(5)
A = [1, 2, 3, 4, 5]

# list.extend(L) adds all elements of the list L at the end of the list:
A = [1, 2, 3, 4]
A.extend([5, 6, 7])
A == [1, 2, 3, 4, 5, 6, 7]

# NOTE: extend(L) and append(x) are not equivalent. extend method takes elements of the list L
# and adds them to the list, while append takes the argument passed to it and adds it as the last
# element in the list. If the argument is a list, then that list itself is added as the last element:
A = [1, 2, 3, 4]
B = [5, 6, 7]
A.append(B)
A == [1, 2, 3 ,4, [5, 6, 7]]

C = [1, 2, 3, 4]
C.extend(B)
C == [1, 2, 3, 4, 5, 6, 7]
C != A

# NOTE: extend(L) and append(x) are not equivalent to + operator becuase they simply change existing lists,
# while + creates a new list. This means that these methods are faster in terms of performance.

# list.insert(i, x) inserts element x at index i in the list:
A = [1, 3, 4, 5, 6, 7, 8]
A.insert(1, 2)
A == [1, 2, 3, 4, 5, 6, 7]

# NOTE: list.insert(0, x) inserts x at the beggining of the list, while list.insert(len(list), x) is equivalen of list.append(x)

# list.remove(x) removes the first item (item with the least index) with value x from the list. If there is no such item, it raises an exception.
A = [1, 2, 3, 4, 5]
A.remove(3)
A == [1, 2, 4, 5]

# list.pop([i]) removes and returns element at the index i in the list. If the index isn't provided, it removes and returns
# the last element in the list:
A = [1, 2, 3, 4, 5, 6, 7]
a = A.pop(4)
A = [1, 2, 3, 4, 6, 7]
a == 5
a = A.pop()
A = [1, 2, 3, 4, 6]
a == 7

# NOTE: An alternative to pop(i) and is del list[i], although del does not return a value.
A = [1, 2, 3, 4, 5]
del A[2]
A = [1, 2, 4, 5]


# list.index(x, [start],[stop]) returns index of the first element in a list with value x, between indices start and stop. 
# If there is no such element, it raises an exception. start and stop are optional arguments - if they are not provided,
# the entire list is searched.
A = [1, 2, 3, 4, 5]
A.index(3) == 2
B = [1, 4, 5, 'a', "Dave", True, 2, 4, 5]
B.index(4) == 1
B.index(4, 4) == 7
B.index(4, 4, len(B) - 1) == 7

# list.count(x) counts number of times value x appears in the list:
A = [1, 2, 3, 1, 3, 4, 2, 5, 6, 4, 2, 3, 4, 1]
A.count(1) == 3

# list.sort([key], reverse = false) sorts items, in place. key is a function used as a key for sorting, while reverse signals
# whether the list will be sorted in reverse order.
A.sort()
A == [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 6]

# list.reverse() reverses the elements of the list, in place.
A.reverse()
A == [6, 5, 4, 4, 4, 3, 3, 3, 2, 2, 2, 1, 1, 1]

# NOTE: Lists can be usd as stacks (last-in, first-out) by using append(x) method for pushing itmes on stack
# and pop() without a specified index for popping itmes from a stack:
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
stack == [3, 4, 5, 6, 7]
stack.pop() == 7
stack == [3, 4, 5, 6]
stack.pop() == 6
stack.pop() == 5
stack == [3, 4]

# NOTE: It is also possible to use a list as a queue, where the first element added is the first element
# retrieved (first-in, first-out). However, lists are not efficient for this purpose. While appends and 
# pops from the end of list are fast, doing inserts or pops from the beginning of a list is slow (because 
# all of the other elements have to be shifted by one). To implement a queue, use collections.deque which
# was designed to have fast appends and pops from both ends. For example:
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")                           # Terry arrives
queue.append("Graham")                          # Graham arrives
queue.popleft() == 'Eric'                       # The first to arrive now leaves
queue.popleft() == 'John'                       # The second to arrive now leaves
queue == deque(['Michael', 'Terry', 'Graham'])  # Remaining queue in order of arrival

############################################################################################################
############################################# SLICING ######################################################
############################################################################################################

# Slicing is performed using the expression <list name>[start index : end index : step]. This expression
# extracts every <step>-th element from a list starting at index <start index> and ending at <end index> - 1.
# If any of the values aren't provided, the default values for that argumet are used. Step can be ommitted.
# Default values are 0 for start index, len(<list name>) for end index and 1 for step. Also, step cannot be 0.
# Result of slicing is a list. 
A = [0, 1, 2, 3, 4, 5, 6, 7]
A[3:4] == 3
A[2:4] == [2, 3]
A[1:] == [1, 2, 3, 4, 5, 6, 7]
A[:3] == [0, 1, 2]
A[::2] == [0, 2, 4, 6]              # Only even numbers.
A[::-1] = [7, 6, 5, 4, 3 , 2, 1, 0] # Reverse order.

# Negative indices can also be used for slicing:
A[-4:-1] == [4, 5, 6]
A[-5:] == [3, 4, 5, 6, 7]

# NOTE: L[:] is equivalent of list(L).
A[:] == [0, 1, 2, 3, 4, 5, 6, 7]

# Slicing can be used for some insertion and manipulation operations for lists:
A = [0, 0, 0, 0, 0, 0, 0, 0, 0]
A[1:1] = [2, 3, 4]                              # Inserts 2, 3, 4 at index 1
A == [0, 2, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0]
A[1:1] = [0]                                    # Inserts 0 at index 1
A == [0, 0, 2, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0]
A[2:6] = [5]                                    # Replaces elements at indices 2 through 5 with 5
A == [0, 0, 5, 0, 0, 0, 0, 0, 0, 0]
A[::2] = [2, 3, 4, 5, 6]                        # Replaces every other element with 2, 3, 4, 5 and 6, respectievly
A == [2, 0, 3, 0, 4, 0, 5, 0, 6, 0]

# NOTE: del can also be used to remove more than one element from the list,
# using the element index instead of value.
A = [1, 2, 3, 4, 5, 6, 7, 8]
del A[2:5]
A == [1, 2, 6, 7, 8]
del A[:]
A == []

############################################################################################################
####################################### LIST COMPREHENSIONS ################################################
############################################################################################################

# List comprehensions provide an alternative and concise way of creating lists. They are used when list elements
# are a part of some subset of iterable collection. A list comprehension consists of brackets containing an expression 
# followed by a for clause, then zero or more for or if clauses. The result will be a new list resulting from evaluating 
# the expression in the context of the for and if clauses which follow it.

squares = [x**2 for x in range(10)]

# Above statement is equivalent to:
squares = []
for x in range(10):
     squares.append(x**2)

# Another example of list comprehensions:
combs = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
combs == [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

# Equivalent to:
combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))

# Note how the order of the for and if statements is the same in both these snippets.
# NOTE: Tuples must be parenthesized. [x, y for x in [1,2,3] for y in [3,1,4] if x != y] 
# is an example of invalid syntax.

# Functions and methods can also be used in list comprehensions:
vec = [-4, -2, 0, 2, 4]
[abs(x) for x in vec] == [4, 2, 0, 2, 4] # A function is applyed in the expression.

freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
[weapon.strip() for weapon in freshfruit] == ['banana', 'loganberry', 'passion fruit'] # A method is appled in the expression

# Flatten a list using a listcomp with two 'for':
vec = [[1,2,3], [4,5,6], [7,8,9]]
[num for elem in vec for num in elem] == [1, 2, 3, 4, 5, 6, 7, 8, 9]

# List comprehensions can contain complex expressions and nested functions:
from math import pi
[str(round(pi, i)) for i in range(1, 6)] == ['3.1', '3.14', '3.142', '3.1416', '3.14159']

# The initial expression in a list comprehension can be any arbitrary expression, 
# including another list comprehension. Consider the following example of a 3x4 matrix
# implemented as a list of 3 lists of length 4:
matrix = [
          [1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
]

# The following list comprehension will transpose rows and columns:
[[row[i] for row in matrix] for i in range(4)] == [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

############################################################################################################
################################### FUNCTIONAL PROGRAMMING TOOLS ###########################################
############################################################################################################

# filter(function, sequence) returns a sequence consisting of those items from the sequence for which function(item)
# is true. If sequence is a string or tuple, the result will be of the same type; otherwise, it is always a list. For
# example, to compute a sequence of numbers not divisible by 2 and 3:
def f(x): return x % 2 != 0 and x % 3 != 0
filter(f, range(2, 25)) == [5, 7, 11, 13, 17, 19, 23]

# map(function, sequence) calls function(item) for each of the sequence's items and returns a list of the return values.
# For example, to compute some cubes:
def cube(x): return x*x*x
map(cube, range(1, 11)) == [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

# More than one sequence may be passed; the function must then have as many arguments as there are sequences and is called
# with the corresponding item from each sequence (or None if some sequence is shorter than another). For example:
seq = range(8)
def addOperation(x, y): return x+y
map(addOperation, seq, seq) == [0, 2, 4, 6, 8, 10, 12, 14]

# reduce(function, sequence) returns a single value constructed by calling the binary function function on the first two items
# of the sequence, then on the result and the next item, and so on. If there's only one item in the sequence, its value is returned.
# If the sequence is empty, an exception is raised. For example, to compute the sum of the numbers 1 through 10:
from _functools import reduce
reduce(addOperation, range(1, 11)) == 55

# A third argument can be passed to indicate the starting value. In this case the starting value is returned for an empty sequence,
# and the function is first applied to the starting value and the first sequence item, then to the result and the next item, and so on.
# For example:
def sumOperation(seq):
     def addOperation(x,y): return x+y
     return reduce(addOperation, seq, 0)
sumOperation (range(1, 11)) == 55
sumOperation([]) == 0