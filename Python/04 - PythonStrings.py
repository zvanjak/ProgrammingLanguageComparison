#Python strings
# -*- coding: cp1250 -*-

import string

#Strings can use either single or double quotation marks


# To fill a string with values you can use % operator and a touple
print ("Name: %s, Number: %s" % ("Pajton Pajtonovi?", 5))


# Multiline strings are enclosed in triple double (or single) quotes(""")
multiLineString = """This is 
a multiline
string
"""
print (multiLineString)


# Watch out for the trailing s in "%(key)s".
print ("This %(verb)s a %(noun)s." % {"noun": "test", "verb": "is"})

s = 'The sum of 1 + 2 is {0}'
print ('Formatting example: ' + s.format(1+2))


# Concatenation is perfomed with '+' operator
s = 'Hello'
print ('Second character of a string "' + s + '" = ' + s[1])
print ('Adjacent' ' strings ' 'are concatenized')

# Don't use "len" as a variable name to avoid blocking out the len() function
sLength = len(s)

# '+' operator does not automatically convert numbers or other types to string form (unlike java)
# You have to convert other types to string manualy with str()
print ('Length of a string: ' + str(sLength))

print
# String methods
s = '  This is some example string!  '
print ('Lowercase: ' + s.lower())
print ('Uppercase: ' + s.upper())
print ('Swapcase: ' + s.swapcase())
print ('Titlecase: ' + s.title())
print ('Whitespace removed: ' + s.strip())
print ('Is this string digit? ' + str(s.isdigit()))
print ('Starts with "This"? ' + str(s.startswith('This')))
print ('How about now? ' + str(s.strip().startswith('This')))
print ('First occurence of string "some" is on index: ' + str(s.find('some')))
print ('Is "some" in this string? ' + str("some" in s))

# Python strings are "immutable" which means they cannot be changed after they are created
print ('Some replacement: ' + s.replace('example', 'real fine'))

# We can split a string with a delimiter (default is whitespace)
listOfWords = s.split()
print ('List of words: ' + str(listOfWords))

# We can join them using join and delimiter is current string value
s = ' ';
print('.. which we join now into string: ' + s.join(listOfWords))


# The "slice" syntax is a handy way to refer to sub-parts of sequences - typically strings and lists
# The slice s[start:end] is the elements beginning at start and extending up to but not including end
print
s = 'This is some example string'
print(s)
print('First character: ' + s[0])
print('Last character: ' + s[-1])
print('3rd character from the end: ' + s[-3])
print('Last 8 characters: ' + s[-8:])
print('Everything but last 8 characters: ' + s[:-8])


# To create unicode string we use 'u' prefix on the string literal:
print
print(u'This is a unicode \u018e string \xf1')
print(b'This is an 8 bit \u018e string \xf1')
print(r'A raw string where \ are kept (literalized): handy for regular expressions and windows paths!')














