# A class is defined using the class statement.The body of a class contains a series of statements that execute during class definition
class Account(object):
    num_accounts = 0                        # ovo je CLASS VARIABLE (definirana na razini klase!!! - znaci zajednicka za sve instance)

    def __init__(self,name,balance):        # poziva se kod inicijalizacije
        self.name = name                    # clanska varijabla
        self.balance = balance              # clanska varijabla
        Account.num_accounts += 1

    def __del__(self):
        Account.num_accounts -= 1

    # instance metode - imaju self kao prvi parametar
    def deposit(self,amt):
        self.balance = self.balance + amt

    def withdraw(self,amt):
        self.balance = self.balance - amt

    def inquiry(self):
        return self.balance

# kreiranje accounta
a = Account("Pero", 1000.00)
b = Account("Marko", 10.00)

a.deposit(100.00)       # Calls Account.deposit(a,100.00)
b.withdraw(50.00)       # Calls Account.withdraw(b,50.00)

# SCOPING
# Although classes define a namespace, classes do not create a scope for names used inside the bodies of methods.
# Therefore, when you're implementing a class, references to attributes and methods must be fully qualified.
class Foo(object):
    def bar(self):
        print("bar!")
    def spam(self):
#        bar(self)           # NE MOZE!!! 'bar' generira NameError
        self.bar()          # Radi
        Foo.bar(self)       # I ovo moze

# NASLJEDJIVANJE
import random
class EvilAccount(Account):
    def __init__(self,name,balance,evilfactor):         # dodajemo parametar u konstruktor za izvedenu klasu
        Account.__init__(self,name,balance)             # pozivamo ctor za baznu klasu (ne poziva se automatski!)
        self.evilfactor = evilfactor
    def inquiry(self):
        if random.randint(0,4) == 1:
            return self.balance * self.evilfactor
        else:
            return self.balance

# u reimplementaciji metode, mozemo pozvati i metodu iz bazne klase
class MoreEvilAccount(EvilAccount):
    def deposit(self,amount):
        self.withdraw(5.00)                 # Subtract the "convenience" fee
        EvilAccount.deposit(self,amount)    # Now, make deposit

# mozemo koristiti i super
# super(cls, instance)returns a special object that lets you perform attribute lookups on the base classes. If you use this,
# Python will search for an attribute using the normal search rules that would have been used on the base classes.
class MoreEvilAccount(EvilAccount):
    def deposit(self,amount):
        self.withdraw(5.00)                 # Subtract convenience fee
        super(MoreEvilAccount,self).deposit(amount)

# STATICKE METODE
class Foo(object):
    @staticmethod
    def add(x,y):
        return x + y

x = Foo.add(3,4)            # x = 7

# zgodno koristiti staticke metode kad postoje razliciti nacini za kreiranje novih instanci
import time
class Date(object):
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day
    @staticmethod
    def now():
        t = time.localtime()
        return Date(t.tm_year, t.tm_mon, t.tm_mday)
    @staticmethod
    def tomorrow():
        t = time.localtime(time.time()+86400)
        return Date(t.tm_year, t.tm_mon, t.tm_mday)

# Example of creating some dates
a = Date(1967, 4, 9)
b = Date.now()          # Calls static method now()
c = Date.tomorrow()     # Calls static method tomorrow()

# PROPERTIES -  property is a special kind of attribute that computes its value when accessed.
import math
class Circle(object):
    def __init__(self,radius):
        self.radius = radius
    # Some additional properties of Circles
    @property
    def area(self):
        return math.pi*self.radius**2
    @property
    def perimeter(self):
        return 2*math.pi*self.radius

c = Circle(4.0)
print (c.radius)      # 4.0
print (c.area)        # 50.26548245743669
print (c.perimeter)   # 25.132741228718345
# c.area = 2          # ovo generira gresku!!!

# ENKAPSULACIJA - Python nema public/private, vec se one varijable koje se zele staviti privatnim, prefiksiraju s double underscore
# cime se njihovo ime mijenja (Mangled) u oblik _Classname__Ime
class A(object):
    def __init__(self):
        self.__X = 3        # Mangled to self._A__X
    def __spam(self):       # Mangled to _A__spam()
        pass
    def bar(self):
        self.__spam()       # Only calls A.__spam()

class B(A):
    def __init__(self):
        A.__init__(self)
        self.__X = 37       # Mangled to self._B__X
    def __spam(self):       # Mangled to _B__spam()
        pass

# OPERATOR OVERLOADING
# User-defined objects can be made to work with all of Python's built-in operators by adding implementations of the special methods.
# to a class. For example, if you wanted to add a new kind of number to Python, you could define a class in which special methods
# such as __add__()were defined to make instances work with the standard mathematical operators
class Complex(object):
    def __init__(self,real,imag=0):
        self.real = float(real)
        self.imag = float(imag)
    def __repr__(self):
        return "Complex(%s,%s)" % (self.real, self.imag)
    def __str__(self):
        return "(%g+%gj)" % (self.real, self.imag)
    # self + other
    def __add__(self,other):
        return Complex(self.real + other.real, self.imag + other.imag)
    # self - other
    def __sub__(self,other):
        return Complex(self.real - other.real, self.imag - other.imag)