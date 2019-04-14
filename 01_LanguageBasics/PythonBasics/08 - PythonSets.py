# A set is used to contain an unordered collection of objects.
# To create a set, use the set()function and supply a sequence of items such as follows:
s = set([3, 5, 9, 10])         # Create a set of numbers
t = set("Hello")            # Create a set of unique characters
u = set(((1, 2), (3, 4)))      # You can create a set from any iterable type, it does't matter what it is, as long as it's iterable

# Unlike lists and tuples, sets are unordered and cannot be indexed by numbers.Moreover, the elements of a set are never duplicated.
print s

# For example, if you inspect the value of t from the preceding code, you get the following:
print t         # Notice that only one 'l' appears.
print u         # Two different tuples
print len(u)    # Check cardinality

# Sets support a standard collection of operations, including union, intersection, difference, and symmetric difference. Here's an example
a = t | s       # Union of t and s
b = t & s       # Intersection of t and s
c = t - s       # Set difference (items in t, but not in s)
d = t ^ s       # Symmetric difference (items in t or s, but not both)

print ""
print a
print b
print c
print d

# Also possible with
a = t.union(s)
b = t.intersection(s)
c = t.difference(s)
d = t.symmetric_difference(s)

# New items can be added to a set using add() or update():
t.add('x')              # Add a single item
s.update([10, 37, 42])    # Adds multiple items to s

print ""
print t
print s

s2 = s.copy()                       # Shallow copy of a set


s2.difference_update(t)              # s -= t	return set s after removing elements found in t
print s2
s2.intersection_update(t)	        # s &= t	return set s keeping only elements also found in t
print s2
s2.symmetric_difference_update(t)    # s ^= t	return set s with elements from s or t but not both
print s2

# An item can be removed using remove():
t.remove('H')
print ""

# remove() will raise KeyError if the element is not found!
try:
    t.remove('H')
except KeyError:
    print "Item doesn't exist"

# Use discard to avoid exception
t.discard('H')

# pop() will remove and return an arbitrary element from the set
print t.pop()
print t


# Check if an element is inside the set
print ""
print 'e' in t, 'e' not in t
print 'e' in s, 'e' not in s

print ""
print b.issubset(a), b <= a     # is b subset of a?
print a.issuperset(b), a >= b   # is a superset of b?
print b.isdisjoint(d)    # are a and b disjoint?

# b < a is b proper subset of a? | b is a proper subset of a if b is a subset of a, but they are not equal
# b < a is b proper superset of a?
