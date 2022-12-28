import math
# -*- coding: cp1250 -*-
# built-in types
normalInt = 12345
decimalInt = 12345678       # long int
binaryInt = 0b1011110011     # pocinje s 0b ili 0B
octalInt = 0o4567123         # pocinje s 0o
hexInt = 0xABCD
floatNum = 10.               # 3.14e-10, 1E3
complexNum = 1J              # 2+3j
s = "string"

# nastavak linije u iducem retku
total_sum = 1
sum2 = 2
sum = total_sum + \
      sum2

# lokacija objekta u memoriji
#print id(normalInt)

# tip objekta
print(type(decimalInt).__name__)

# provjera tipa podatka
print(isinstance(s, str))

#duljina bitova
print("Binarni prikaz broja {0} je {1}".format(normalInt, bin(normalInt))) # pretvorba u bin. broj
print("Duljina bitova broja {0} je {1}".format(normalInt, normalInt.bit_length()))

#float
print (floatNum.as_integer_ratio()) # float kao omjer dva integera, vra�a tuple

tupleOmjeraPI = math.pi.as_integer_ratio()
print ("Brojevi za omjer broja pi: {0}".format(tupleOmjeraPI))

print ("{0} odgovara integer vrijednosti: {1}".format(floatNum, floatNum.is_integer()))   # provjera odgovara li float broja integer vrijednosti

print (floatNum.hex()) # heksidecimalna vrijednost floata

#kompleksni brojevi
print ("Realni dio kompleksnog broja {0} je {1}, a imaginarni je {2}".format(complexNum, complexNum.real, complexNum.imag))

complexNum1 = complex(0,1)      # kompleksni broj pomocu built-in funkcije complex()
print (complexNum1)

complexNum2 = complex()         # complex bez argumenta, analogno se mo�e izostaviti samo realni ili imaginarni dio 
print (complexNum2)

complexNum3 = complex('3+2j')   # string kao argument, javlja value error za npr. '3 + 2j'
print (complexNum3)

print (complexNum1 * complexNum3)

#divmod
print (divmod(normalInt, 2))  # vra�a tuple (x//y, x%y)

'''
    komentar
    kroz
    vi�e
    redaka
'''


#raw_input()



