import string
import math

a = (1, 2, 3, 4, 5, 6, 6, 7, 8)

# ispis old way s %
print("Duljina = ", len(a))
print("Duljina = %d" % len(a))
print("Duljina je %d a prvi element je %d" % (len(a), a[0]))

# ispis s format
print('1. Duljina je {0} a prvi element je {1}'.format(len(a), a[0]))
print('2. Duljina je {0:10} a prvi element je {1:10}'.format(len(a), a[0]))             # specificiranje sirine polja za ispis
print('3. Duljina je {lenTotal} a prvi element je {elemVal}'.format(lenTotal=len(a), elemVal=a[0]))

print('The value of PI is approximately {0:.3f}'.format(math.pi))

# REPR i STR funkcije - pretvaranje u string
print("str(123.35) = ", str(123.35))
print("repr(123.35 + 23.45) = ", repr(123.35 + 23.45))

# str.rjust(), str.ljust(), str.center() - left/right padding, odnosno centriranje
print("Desni padding:", repr(12.345).rjust(10))


# TODO - ucitavanje

print("Unesite nesto:")
s = input()
print(isinstance(s,str))  # provjera tipa unesenog podatka

s = input('Unesite opet nesto ----> ') 
print("Upisali ste {0}".format(s))

input('I za kraj upisite opet nesto ----> ')     # funkcija ne hvata greske, preporuca se raw_input

"""
"""
