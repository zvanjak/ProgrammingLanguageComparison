# The best thing to keep in mind is that functions are objects in the Python language and the parameters
# that are passed are really “applied” to the function object.

def fun(name, location, year=2006):
    print ("%s/%s/%d" % (name, location, year))

fun("Teag", "San Diego")

# passing param by name (moze se izmijeniti redoslijed!)
fun(location="L.A.", year=2004, name="Caleb" )

# mogu se i mijesati nacini pozivanja
fun("Aedan", year=2005, location="London")

# parametri se mogu predavati kao tuple
tuple = ("DaNae", "Paris", 2003)
fun(*tuple)

# a mogu se predavati i kao dictionary
dictionary = {'name':'Brendan', 'location':'Orlando', 'year':1999}
fun(**dictionary)

# vracanje VISE vrijednosti iz funkcije preko tuple:
def divide(a,b):
    q = a // b # If a and b are integers, q is integer
    r = a - q*b
    return (q,r)
quotient, remainder = divide(1456,33)

# LABMDA IZRAZI
# sintaksa - lambda <args> : <expression>
bigger = lambda a, b : a > b
print (bigger(1,2))   # --> False
print (bigger(2,1))   # --> True
