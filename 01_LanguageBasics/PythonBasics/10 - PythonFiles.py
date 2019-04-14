f=open('filef.txt','r') #otvara datoteku za citanje
'''
oblik: f=open(filename, mode)
-mode: r,w,r+(za citanje i pisanje),a(dodavanje na kraj)
-za hrvatske znakove u datotekama dodati argument encoding='utf8'
'''

wholef=f.read() #ucitava cijelu datoteku u string
'''
oblik: f.read(no_of_bytes)
-no_of_bytes nije obavezan; specificira broj znakova koje se zeli ucitati
'''

print('Cijela datoteka f:\n' + wholef)

print('Trenutna pozicija je:')
print(f.tell()) #trenutna pozicija kazaljke

f.seek(0) #"premotava" datoteku, postavlja kazaljku na pocetak
'''
oblik: f.seek(offset, from_what)
-offset se racuna u bajtovima(znakovima); moze biti negativan
-from_what: 0-pocetak datoteke (default), 1-trenutna pozicija, 2-kraj
'''

line=f.readline() #ucitava redak datoteke u string, ostavlja "\n"
print('Prvi redak:\n' + line)

f.seek(0)
alllines=f.readlines() #ucitava cijelu datoteku u listu stringova, ostavlja "\n"
print('Lista redaka:')
print(alllines)
f.close() #zatvara datoteku

g=open('fileg.txt','w') #ako datoteka ne postoji, stvori ju
g.write('Roses are red, violets are blue.\n\n') #zapisuje string u datoteku
bla=['bla\n','BlAa\n','b1@\n']
g.writelines(bla) #zapisuje listu stringova u datoteku; ne dodaje "\n"
print('Datoteka g se mo?e ?itati?')
print(g.readable)
g.close()

print('Datoteka g je zatvorena?')
print(g.closed) 


g=open('fileg.txt','r+')
print('\nDatoteka g:')
for line in g: 
    print(line, end='') #alternativni nacin citanja datoteke
g.close()

h=open('fileh.txt','r')
print('Datoteka h:')
print(h.read())
h.close()

h=open('fileh.txt','w')
h.seek(5)
h.truncate() #odsijeca datoteku od kazaljke na dalje; metoda radi samo za mode='w'
h.close()

i=open('filei.txt','r')
linesi=i.read().splitlines() #ucitava datoteku u listu, bez "\n"
objects=[eval(o) for o in linesi] #eval koristi string kao Pythonov izraz (izvrsivi kod)
print('Evaluirana datoteka i:')
print(objects)
    








