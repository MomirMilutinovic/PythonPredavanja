import Grafika as g

def izaberiRec():
    #Bira rec (korisnik ukucava rec)
    
    rec = input('Unesite rec: ')
    return rec
    
    
def  ukucajSlovo(slova):
    # Kao parametar prima slova koja su vec pogadjana 
    # Govori korisniku da ukuca slovo
    # Ukoliko je slovo vec bilo uneto u nekom potezu korisnik mora da ukuca
    # neko drugo slovo koje do sada nije bilo ukucano
    # Kao povratnu vrednost vraca ukucano slovo
    
    slovo = input('Unesite slovo: ')
    while slovo in slova:
         slovo = input('Ponovo unesite slovo: ')
    return slovo


def ispisiRec(rec, slova):
    # Kao parametar uzima rec i slova koja su do momenta poziva pogodjena
    # Ispisuje slovo ako je pogodjeno, a ako nije ispisuje _
    # Nema povratnu vrednost
    
    for c in rec:
        if c in slova:
            print(c, end = '')
        else:
            print(' _ ', end = '')
    print('')
            
            
def igraj(slovo, trenutanBrojZivota, rec, slova):
    # Glavna funkcija igre
    # Kao parametre uzima ukucano slovo, trenutan broj zivota i pogodjena slova
    # koja prosledjuje ostalim funkcijama
    # Smanjuje prosledjen broj zivota za 1 (ova promena se ne cuva, potrebno je posle funkcije rucno smanjiti)
    # Vraca true ili false zavisno od toga da li je pogodjeno slovo
    
    if slovo not in rec:
        trenutanBrojZivota-=1
    ispisiRec(rec, slova)
    print(slova)
    print(g.stanja[trenutanBrojZivota])
    if slovo not in rec:
        trenutanBrojZivota-=1
        return False
    else:
        return True
    
    
def zavrsiIgru(trenutanBrojZivota, brojPogodjenihSlova, rec):
    # Kao parametre prima trenutan broj zivota, broj pogodjenih slova i rec
    # Proverava da li je igra izgubljena ili pobedjena i prikazuje odgovarajucu poruku

    if trenutanBrojZivota == 0:
        print("Niste uspeli pogoditi rec \nRec je bila: ", end = '')
        print(rec)
    if brojPogodjenihSlova == len(rec):
        print("Pogodili ste rec")
    