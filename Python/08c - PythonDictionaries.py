import math

# A dictionary is an associative array or hash table that contains objects indexed by keys.
stock = {
    "name" : "GOOG",
    "shares" : 100,
    "price" : 490.10
}

# To access members of a dictionary, use the key-indexing operator as follows:
name = stock["name"]
value = stock["shares"] * stock["price"]

# Inserting or modifying objects works like this:
stock["shares"] = 75
stock["date"] = "June 7, 2007"

# An empty dictionary is created in one of two ways:
prices = {}         # An empty dict
prices = dict()     # An empty dict

#A dictionary can be created by passing a list of key-value pairs to the dict  constructor
prices = dict([ ("One", 123), ("Two", 741) ])

#  dictionaries are also used as a container for performing fast lookups on unordered data
prices = {
    "GOOG" : 490.10,
    "AAPL" : 123.50,
    "IBM" : 91.50,
    "MSFT" : 52.13
}

# Dictionary membership is tested with the in operator, as in the following example:
if "SCOX" in prices:
    p = prices["SCOX"]
else:
    p = 0.0

# This particular sequence of steps can also be performed more compactly as follows:
p = prices.get("SCOX",0.0)

# has_key was removed in Python 3
#exist = prices.has_key("SCOX")      # vraca True ako key postoji, inace false

# To obtain a list of dictionary keys, convert a dictionary to a list:
syms = list(prices)         # syms = ["AAPL", "MSFT", "IBM", "GOOG"]
# ili ovako
syms = prices.keys()

# mozemo dohvatiti i values
vals = prices.values()

# Use the del statement to remove an element of a dictionary:
del prices["MSFT"]

# shallow copy
shallowCopy = prices.copy()

# dictionaries can also be nested
nestedDict = { "key" : {"name" : "stock name", "price" : 123}}

#indexing nested dictionaries
nestedDict["key"]["price"]

#testing if something is a dictionary
result = type(nestedDict) is dict
print(result)

#another way of testing
result = isinstance(nestedDict, dict)
print(result)

#get the size of the dictionary
len(prices)

#returns key-value tuples from the dictionary
prices.items()

#merges the keys and values of one dictionary with another
#overrites the values of the old dictionary in case of duplicate keys
nestedDict.update(prices)

#deletes the specified key from the dictionary and returns its value
nestedDict.pop("IBM")

#shorthand for prices.keys
for key in prices:
    print (key, "\t", prices[key])

#keys can be any immutable object
orderings = { 1: "First", 2 :"Second", 3: "Third" }

#keys returns only a reference to the dictionary keys
#if elements are added or deleted, it will immediately have effect on the keys list
dictkeys = orderings.keys()
print (dictkeys)
del(orderings[3])
print(dictkeys)

#removes an arbitrary item (key, value) from the dictionary
item = orderings.popitem()
print(item)

#removes all entries from the dictionary
orderings.clear()
print(len(orderings))


#Python 3 specific code

#Dictionary comprehension
keyList = [1,2,3,4,5]
valueList = ["Red", "Blue", "Green", "Yellow", "Black"]
colors = { k:v for (k,v) in zip(keyList, valueList)}
for key in colors:
    print (key, "\t", colors[key])

#it is possible to specify a condition in the dictionary comprehension
squares = { k:k**2 for k in range(1,10) if k%2!=0 }
for key in squares:
    print (key, "\t", squares[key])

#functions can also be used in dictionary comprehension
squares = { k:int(math.pow(k,2)) for k in range(1,10) if k%2!=0 }
for key in squares:
    print (key, "\t", squares[key])


#easily iterating through sorted keys
for key in sorted(prices):
    print (key, "\t", prices[key])

