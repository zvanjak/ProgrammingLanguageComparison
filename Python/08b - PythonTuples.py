# To create simple data structures, you can pack a collection of values together into a single object using a tuple.
# You create a tuple by enclosing a group of values in parentheses like this:
first_name = 'Zvonimir'
last_name = 'Vanjak'
phone = '111-2222'
stock = ('GOOG', 100, 490.10)
address = ('www.python.org', 80)
person = (first_name, last_name, phone)
print("Basic tuple: {0}\n".format(person))

# Python often recognizes that a tuple is intended even if the parentheses are missing:
stock = 'GOOG', 100, 490.10
address = 'www.python.org',80
person = first_name, last_name, phone

# Tuples can be nested
nestedTuple = person, "Professor", "FER", ["2011/2012", "2012/2013"]
print("Nested tuple: {0}\n".format(nestedTuple))

# For completeness, 0- and 1-element tuples can be defined, but have special syntax:
item = "item"
a = ()          # 0-tuple (empty tuple)
b = (item,)     # 1-tuple (note the trailing comma)
c = item,       # 1-tuple (note the trailing comma)
print("Empty tuple: {0}".format(a))
print("Single element tuple (note the trailing coma): {0}\n".format(b))

# The values in a tuple can be extracted by numerical index just like a list. However, it is more common to unpack tuples
# into a set of variables like this:
name, shares, price = stock
host, port = address
first_name, last_name, phone = person
print("Tuple unpacking: {0}".format(person))
print("First name: {0}".format(first_name))
print("Last name: {0}".format(last_name))
print("Phone: {0}\n".format(phone))

try:
	stock[1] = 50
except TypeError:
	print("Tuples are IMUTABLE!!!\n")

# Tuples are IMUTABLE!!! -the contents of a tuple cannot be modified after creation

# Basic tuples operations
a = (1,2,3)
b = (4,5,6)

print("Basic tuples operations:")
print (len(a))			# 3
print (a + b)			# (1, 2, 3, 4, 5, 6)
print (("Hi!",) * 4)	# ('Hi!', 'Hi!', 'Hi!', 'Hi!') 
print (3 in a)			# True
print


# Tuples and lists are often used together to represent data. For example, this program
# shows how you might read a file consisting of different columns of data separated by commas:

# File containing lines:
# GOOG,100,490.10
# MSFT,50,54.23
filename = "portfolio.csv"
portfolio = []
for line in open(filename):
    fields = line.split(",")        # Split each line into a list
    name = fields[0]                # Extract and convert individual fields
    shares = int(fields[1])
    price = float(fields[2])
    stock = (name,shares,price)     # Create a tuple (name, shares, price)
    portfolio.append(stock)         # Append to list of records

print("portfolio[0] = {0}".format(portfolio[0]))  # prints ('GOOG', 100, 490.10)
print("portfolio[1] = {0}\n".format(portfolio[1]))  # ('MSFT', 50, 54.23)

# Individual items of data can be accessed like this:
print("portfolio[1][1] = {0}".format(portfolio[1][1]))       # 50
print("portfolio[1][2] = {0}".format(portfolio[1][2]))       # 54.23
print("portfolio[0][0:2] = {0}\n".format(portfolio[0][0:2]))   # ('GOOG', 100)

# Heres an easy way to loop over all of the records and expand fields into a set of variables:
total = 0.0
for name, shares, price in portfolio:
    total += shares * price
print("Total share price: {0}".format(total))
