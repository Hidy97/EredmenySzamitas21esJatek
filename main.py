jatekosLapok = [4, 3, 2]
gepLapok = [4, 8, 9]


def pontszamitas(lapok: [list]):
    osszpontszam = 0
    for i in range(len(lapok)):
        osszpontszam += lapok[i]
    return osszpontszam


jatekos_Osszpontszam = pontszamitas(jatekosLapok)
gep_Osszpontszam = pontszamitas(gepLapok)

# megoldás


def eredmeny(jatekos_lapok: [int], gep_lapok: [int]):
    jatekos_lapok: int = jatekos_Osszpontszam
    gep_lapok: int = gep_Osszpontszam
    if jatekos_lapok > 21:
        print("Játékos vesztett")
    elif gep_lapok > 21:
        print("Gép vesztett")
    else:
        print("Mindkét fél lapja kevesebb mint 21")

# tesztesetek
    eredmeny(jatekos_Osszpontszam, gep_Osszpontszam)
