import MehanikeIgre as Igra

# Postavljanje pocetnih vrednosti svih potrebnih promenljivih
rec = Igra.izaberiRec()
trenutanBrojZivota = 7
slova = '' # Cuva sva nagadjana slova
brojPogodjenihSlova = 0

while trenutanBrojZivota>0 and brojPogodjenihSlova < len(rec):
            slovo = Igra.ukucajSlovo(slova)
            slova = slova + slovo
            if Igra.igraj(slovo, trenutanBrojZivota, rec, slova):
                brojPogodjenihSlova = brojPogodjenihSlova + rec.count(slovo)
            else:
                trenutanBrojZivota = trenutanBrojZivota - 1

Igra.zavrsiIgru(trenutanBrojZivota, brojPogodjenihSlova, rec)