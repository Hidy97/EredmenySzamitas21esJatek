def pontszamitas(lapok: [list]):
    osszpontszam = 0
    for i in range(len(lapok)):
        osszpontszam += lapok[i]
    return osszpontszam
# megoldás


"""
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
"""


def eredmeny(jatekos_lapok: [int], gep_lapok: [int]):
    jatekos_pontok: int = pontszamitas(jatekos_lapok)
    gep_pontok: int = pontszamitas(gep_lapok)
    szoveg = ""

    if jatekos_pontok <= 21 and jatekos_pontok <= 21:
        if jatekos_pontok > gep_pontok:
            szoveg = "Játékos nyert"
        elif gep_pontok > jatekos_pontok:
            szoveg = "Gép nyert"
        elif gep_pontok == jatekos_pontok:
            if len(jatekos_lapok) < len(gep_lapok):
                szoveg = "Játékos nyert"
            elif len(jatekos_lapok) < len(gep_lapok):
                szoveg = "Gép nyert"
            else:
                szoveg = "Döntetlen, osztoztok a nyereségen!"
    else:
        if jatekos_pontok > 21:
            szoveg = "Játékos vesztett"
        elif gep_pontok > 21:
            szoveg = "Gép vesztett"
        elif jatekos_pontok > 21 and gep_pontok > 21:
            szoveg = "Döntetlen! A Ház nyert!"
    return szoveg

# tesztesetek

# 1.teszteset


def jatekos_vesztett_nagyobbmint_21_teszt():
    print("Eset: amikor a játékos pontszáma nagyobb mint 21.\n\t")
    jatekos_lista = [9, 10, 2, 8]
    gep_lista = [5, 4, 3, 1]
    kapott_eredmeny = eredmeny(jatekos_lista, gep_lista)
    vart_eredmeny = "Játékos vesztett"

    # Játékos veszít, pontszám nagyobb mint 21
    if kapott_eredmeny == vart_eredmeny:
        print("Játékos vesztett!")
    else:
        print("A teszt sikertelen!")
    return kapott_eredmeny

# 2.teszteset


def jatekos_vesztett_nagyobb_lapokszama_teszt():
    print("Eset: amikor a játékos lapja több mint a gépé.\n\t")
    jatekos_lista = [7, 3, 1, 8]
    gep_lista = [5, 4, 3]
    kapott_eredmeny = eredmeny(jatekos_lista, gep_lista)
    vart_eredmeny = "Játékos vesztett"

    if kapott_eredmeny == vart_eredmeny:
        print("Játékos vesztett!")
    else:
        print("A teszt sikertelen!")
    return kapott_eredmeny

# 3.teszteset


def jatekos_vesztett_gepnel_es_21nel_kisebb_teszt():
    print("Eset: amikor a játékos veszít kevesebb lappal és kevesebb pontszámmal.\n\t")
    jatekos_lista = [10, 9]
    gep_lista = [5, 4, 3, 7, 1]
    kapott_eredmeny = eredmeny(jatekos_lista, gep_lista)
    vart_eredmeny = ""

    # Játékos veszít, pontszám nagyobb mint 21
    if kapott_eredmeny == vart_eredmeny:
        print("Játékos vesztett!")
    else:
        print("A teszt sikertelen!")
    return kapott_eredmeny

# 4.teszteset


def gep_vesztett_nagyobbmint_21_teszt():
    print("Eset: amikor a gép pontszáma nagyobb mint 21.\n\t")
    jatekos_lista = [1, 4, 2, 7]
    gep_lista = [5, 9, 3, 6]
    kapott_eredmeny = eredmeny(jatekos_lista, gep_lista)
    vart_eredmeny = "Gép vesztett"

    # Játékos veszít, pontszám nagyobb mint 21
    if kapott_eredmeny == vart_eredmeny:
        print("Gép vesztett")
    else:
        print("A teszt sikertelen!")
    return kapott_eredmeny

# 5.teszteset


def gep_vesztett_nagyobb_lapokszama_teszt():
    print("Eset: amikor a gép lapja több mint a játékosé.\n\t")
    jatekos_lista = [9, 10, 2, 8]
    gep_lista = [5, 4, 3]
    kapott_eredmeny = eredmeny(jatekos_lista, gep_lista)
    vart_eredmeny = "Gép vesztett"

    if kapott_eredmeny == vart_eredmeny:
        print("Gép vesztett")
    else:
        print("A teszt sikertelen!")
    return kapott_eredmeny

# 6.teszteset


def gep_vesztett_jatekosnal_es_21nel_kisebb_teszt():
    print("Eset: amikor a gép a játékosnál is és 21nél is kisebb a pontszámmal rendelkezik.\n\t")
    jatekos_lista = [9, 10, 2, 8]
    gep_lista = [5, 4, 3, 1]
    kapott_eredmeny = eredmeny(jatekos_lista, gep_lista)
    vart_eredmeny = "Gép vesztett"

    # Játékos veszít, pontszám nagyobb mint 21
    if kapott_eredmeny == vart_eredmeny:
        print("Gép vesztett")
    else:
        print("A teszt sikertelen!")
    return kapott_eredmeny

# 7.teszteset


def jatekos_vesztett_minden_egyenlo_teszt():
    print("Eset: amikor mindkét fél lapjainak és pontjainak száma egyenlő.\n\t")
    jatekos_lista = [9, 10, 2, 8]
    gep_lista = [5, 4, 3, 1]
    kapott_eredmeny = eredmeny(jatekos_lista, gep_lista)
    vart_eredmeny = "Játékos vesztett"

    # Játékos veszít, pontszám nagyobb mint 21
    if kapott_eredmeny == vart_eredmeny:
        print("Játékos vesztett!")
    else:
        print("A teszt sikertelen!")
    return kapott_eredmeny


def tesztek():
    # játékos ellenőrzése
    jatekos_vesztett_nagyobbmint_21_teszt()
    jatekos_vesztett_nagyobb_lapokszama_teszt()
    jatekos_vesztett_gepnel_es_21nel_kisebb_teszt()
    # gép ellenőrzése
    gep_vesztett_nagyobbmint_21_teszt()
    gep_vesztett_nagyobb_lapokszama_teszt()
    gep_vesztett_jatekosnal_es_21nel_kisebb_teszt()
    # egyéb
    jatekos_vesztett_minden_egyenlo_teszt()


tesztek()
