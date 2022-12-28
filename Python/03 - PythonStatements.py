# IF
print ("if statement")
x = 3
if x == 1:
    print (True)
elif x == 2:
    print (False)
else:
    print ("???")
# elif dio moze se pojaviti vise puta ili ni jednom
# else dio nije obavezan
# Python nema switch ... case naredbu, umijesto toga se koristi if ... elif ... else


# PETLJE i ITERIRANJE

print ("\nfor statement")
# FOR petlja
# for petlja iterira po elementima lista, n-torki, skupova i nizova znakova redoslijedom kojim se oni pojavljuju u kolekciji
print ("iteriranje kroz listu borjeva listOfNumbers = [5, 4, 3, 2, 1]")
listOfNumbers = [5, 4, 3, 2, 1]
for i in listOfNumbers:
    print ("broj: ", i)

print ("iteriranje kroz n-torku tupleExample = ('a', 2, '13', 'b')")
#vrijednosti po koijma se iterira ne moraju biti istoga tipa
tupleExample = ('a', 2, '13', 'b')
for i in tupleExample:
    print (i)

print ("iteriranje kroz skup setExample = {1, 2, 3}")
setExample = {1, 2, 3}
for i in setExample:
    print (i)

print ("koristenje naredbe range(1, 10) za stvarenje niza")
for i in range(1, 10):     # for item in sequence: block
    print (i)

# range(i,j [,stride]) naredba stvara objekt tipa range koji predstavlja niz cijelih brojeva koji zapocinje s i, svaki sljedeci raste za korak stride dok je manji od j
a = range(0,14,3)   # a = 0,3,6,9,12

# ako se ne navede korak, pretpostavljena vrijednost je 1
b = range(1,8)      # b = 1,2,3,4,5,6,7

# ako se ispusti prvi argument, pretpostavljena vrijednost je 0
c = range(5)        # c = 0,1,2,3,4

# korak moze biti negativan broj
d = range(8,1,-1)   # d = 8,7,6,5,4,3,2

print ("iteriranje kroz znakovni niz word = \"Python\"")
word = "Python"
for ch in word:
    print (ch)

print ("rad s rjecnicima")
dictExample = { 1:'a', 2:'b', 3:'c' }
# iteriranje po kljucevima
for k in dictExample.keys():
    print ("kljuc: ", k)

# for ce iterirati po kljucevima i ako se ne pozove metoda keyes()
for key in dictExample:
    print (key, "=", dictExample[key])

# iteriranje po vrijednostima
for v in dictExample.values():
    print ("vrijednost: ", v)

# iteriranje po parovima (kljuc, vrijednost)
for p in dictExample.items():
    print ("parovi: ", p)

print ("koristenje naredbe enumerate(word)")
# enumerate(sequence, start=1) prima niz i numerira clanove, pocevsi od zadanog broja start
# vraca n-torke koje se sastoje od parova (redni broj, vrijednost)
# ako drugi argument nije naveden, pretpostavljena vrijednost je 0
dictExample = {}
for i, ch in enumerate(word):
    dictExample[i] = ch

print ("paralelno iteriranje kroz vise nizova koristenjem naredbe zip (list1, list2)")
# zip spaja clanove n nizova u n-torke
list1 = [1, 2, 3, 4, 5, 6]
list2 = ['a', 'b', 'c']
for (x, y) in zip (list1, list2):
    print (x, " iz prve liste, ", y, " iz druge liste")


# WHILE
print ("\nwhile statement")
# while petlja u Pythonu nema posebnosti u odnosu na druge programske jezike
# break i continue - standardni
i=5
while i < 10:
    i += 2
    print (i)
    

# EXCEPTIONS
print ("obrada pogrešaka")

# except blok hvata odredeni tip pogreske
try:
    f = open("test.txt")
except IOError:
    print ("Cannot open file.")
    
# except blok moze obraditi vise pogresaka
try:
    f = open("test.txt")
except (RuntimeError, IOError):
    pass    # pass je prazna naredba

# moguce je obraditi vise pogresaka u razlicitim except blokovima
try:
    f = open("test.txt")
except RuntimeError:
    pass
except IOError as e:
    # ispis teksta pogreske
    print ("ispis greske: ", e.strerror)
except:
    # prazna except naredba sluzi za hvatanje pogresaka svih tipova
    print ("Zanemarena pogreška.")
    raise   # bacanje iznimke

# else dio se izvrsava ako se u try bloku nije dogodila pogreska
try:
    f = open("test.txt")
except IOError:
    print ("Cannot open file.")
else:
    print ("Broj redaka je: ", len(f.readlines()))
    f.close()
# ako se navodi, else mora slijediti iza svake except naredbe

# finally blok se izvrsava uvijek
data = "TestData"
f = open("test.txt", "w+")
try:
    f.write(data)
except:
    pass    #pogreske su zanemarene
finally:
    f.close()
