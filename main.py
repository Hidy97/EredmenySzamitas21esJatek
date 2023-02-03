def pontszamitas(lapok: [list]):
    osszpontszam = 0
    for i in range(len(lapok)):
        osszpontszam += lapok[i]
    return osszpontszam
# megoldás


def eredmeny(jatekos_lapok: [int], gep_lapok: [int]):
    jatekos_pontok: int = pontszamitas(jatekos_lapok)
    gep_pontok: int = pontszamitas(gep_lapok)
    if jatekos_pontok > 21:
        szoveg = "Játékos vesztett"
    elif gep_pontok > 21:
        szoveg = "Gép vesztett"
    else:
        szoveg = "Mindkét fél lapja kevesebb mint 21"
    return szoveg

# tesztesetek


def jatekos_vesztett_teszt():
    jatekos_lista = [9, 10, 2, 8]
    gep_lista = [5, 4, 3]
    kapott_eredmeny = eredmeny(jatekos_lista, gep_lista)
    vart_eredmeny = "Játékos vesztett"

    # Játékos veszít, pontszám nagyobb mint 21
    if kapott_eredmeny == vart_eredmeny:
        print("A teszt sikeres!")
    else:
        print("A teszt sikertelen!")
    # Játékos veszít nagyobb lapszám miatt
    if len(jatekos_lista) > len(gep_lista):
        print("Játékos vesztett! Neki van több lapja van.")
    else:
        print("A teszt sikertelen állapotban van!")


def tesztek():
    jatekos_vesztett_teszt()


tesztek()
