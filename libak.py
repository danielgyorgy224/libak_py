"""
LIBÁK

A róka libát lop a faluból. A libák súlyát – pontosabban tömegét – listában adjuk meg. A farkas a dűlőútnál várja a rókát, és a három kilónál nagyobb libákat elveszi – a piciket nagylel�kűen otthagyja a rókának.
libak = [1,5,2,3,4]

a. Hány kiló libát ehet meg a róka?
b. Átlagosan hány kilósak a rókának maradt libák?
c1. Előfordult-e olyan, hogy a róka legalább háromkilós libát lopott?
c2. Előfordult-e olyan, hogy a róka kisebb libát hozott, mint az előző napon?
d. Hányadik napon sikerült a rókának először legalább háromkilós libát lopnia?
e. Melyik a róka első legalább háromkilós libája?
f. Hány libát tarthat meg a róka?
g. Mekkora a legkisebb liba, amit a farkas elvesz a rókától?
"""

# alprogramok
def beolvasas():
    l = []
    with open("./libak.txt", "r", encoding="utf-8") as fm:
        for sor in fm:
            l.append(int(sor.strip()))
    return l

def roka_osszeg(l):
    db = 0
    sum = 0
    for suly in l:
        if suly < 4:
            db+=1
            sum+=suly
    return sum, db

def kiir(list, ro, rdb):
    print(f"Libák súlyai (kg): {', '.join(map(str, list))}")
    print(f"a. {ro} kiló libát ehet meg a róka.")
    print(f"b. Átlagosan {ro/rdb:.2f} kilósak a rókának maradt libák.")

# főprogram
# input
libak = beolvasas()
# számítás
rosszeg, rdarab = roka_osszeg(libak)
# output
kiir(libak, rosszeg, rdarab)