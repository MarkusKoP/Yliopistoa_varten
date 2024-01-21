import random


def pelaa_peli(nimi):
    """ 
    tämä funktio valitsee vuorossa olevan satunnaisesti. 
    """
    
    vuorossa_oleva = False #tietokone aloittaa
    if random.randint(1,2) == 1:
        vuorossa_oleva = True # pelaaja aloittaa
        print(nimi, "aloittaa!")
    else:
        print("Botti3000 aloittaa!")

    rivit = 6
    sarakkeet = 7
    peli_kentta = matriisi_alustus(rivit, sarakkeet)
    pelaaja_merkki = "X"
    botti3000_merkki = "O"
    voittaja = ""

    while True:
        if vuorossa_oleva: # pelaajan vuoro
            print("Pelaajan", nimi, "vuoro!",end="\n\n")
            pelaa_vuoro(peli_kentta, pelaaja_merkki)
            matriisi_tulostus(peli_kentta)
            if kaiken_tarkistava(peli_kentta, pelaaja_merkki): 
                voittaja = nimi
                break
            else:
                vuorossa_oleva = False 
                
        else: # botti3000 vuoro
            print("Botti3000 vuoro!",end="\n\n")
            tietokone_vuoro(peli_kentta, botti3000_merkki)
            matriisi_tulostus(peli_kentta)
            if kaiken_tarkistava(peli_kentta, botti3000_merkki):
                voittaja = "Botti3000"
                break
            else:
                vuorossa_oleva = True
    print("Peli päättyi", voittaja, "voitti!")
    return voittaja

def tietokone_vuoro(matriisi, merkki):
    """ 
    Tämä funktio arpoo tietokoneen seuraavan pelimerkin paikan.
    """
    paikka = botti3000_sarakevalinta(matriisi)
    matriisi[paikka[0]][paikka[1]] = merkki

def botti3000_sarakevalinta(matriisi):
    """ 
    Apufunktio, jotta saadaan tietokoneelle valittu pelimerkin paikka
    """
    lista = ["0","1","2","3","4","5","6"]
    while True:
        valittu_sarake = random.choice(lista)
        if valittu_sarake in lista:
            valittu_sarake = int(valittu_sarake)
            rivi_indeksi = onko_sarake_taysi(matriisi, valittu_sarake)
            if rivi_indeksi == -1:
                continue

            else:
                return (rivi_indeksi, valittu_sarake)

def matriisi_alustus(rivit, sarakkeet):
    """
    Alustaa riveistä ja sarakkeista matriisin, joka toimii pelikenttänä
    """
    return [["-" for s in range(sarakkeet)] for rivi in range(rivit)]


def matriisi_tulostus(matriisi):
    """ 
    Tulostaa pelikentän.
    """
    for r in range(len(matriisi)):
        for s in range(len(matriisi[0])):
            print(matriisi[r][s], end="")
        print()   

def onko_sarake_taysi(matriisi, valittu_sarake):
    """ 
    Testaa voiko sarakkeeseen laittaa pelimerkkiä vai onko täysi
    """
    for i in range(len(matriisi)-1,-1,-1):
        if matriisi[i][valittu_sarake] == "-":
            return (i)
    return -1 


def valitse_sarake(matriisi):
    """ 
    Seuraavan pelimerkin sijoittamiseen funktio.
    """
    lista = ["0","1","2","3","4","5","6"]
    while True:
        valittu_sarake = input("Mihin haluat pudottaa, sarake:")
        if valittu_sarake in lista:
            valittu_sarake = int(valittu_sarake)
            rivi_indeksi = onko_sarake_taysi(matriisi, valittu_sarake)
            if rivi_indeksi == -1:
                print("Täynnä, valitse uusi sarake!")

            else:
                return (rivi_indeksi, valittu_sarake)


def pelaa_vuoro(matriisi, merkki):
    """ 
    Sijoittaa seuraavan pelimerkin paikan
    """
    paikka = valitse_sarake(matriisi)
    matriisi[paikka[0]][paikka[1]] = merkki
    

    
def tarkista_vaaka_pelikentta(matriisi, merkki):
    """ 
    Tarkistaa onko vaakatasossa neljän merkin suoria
    """
    laskuri = 0
    for rivi in matriisi:
        for i in rivi:
            if i == merkki:
                laskuri += 1
                if laskuri == 4:
                    # voitto
                    return True
            else:
                laskuri = 0
    return False

def tarkista_pysty_pelikentta(matriisi, merkki):
    """ 
    Tarkistaa onko pystytasossa neljän merkin suoria
    """
    laskuri = 0
    for sarake_indeksi in range(len(matriisi[0])):
        for rivi in matriisi:
            if rivi[sarake_indeksi] == merkki:
                laskuri += 1
                if laskuri == 4:
                    # voitto
                    return True
            else:
                laskuri = 0         
    return False

def tarkista_vasen_ylhaalta_alas_pelikentta(matriisi, merkki):
    """ 
    Tarkistaa onko viistosti vasemmalta ylhäältä alas neljän merkin suoria
    """
    laskuri = 0
    rivi_indeksi = 0
    for sarake_indeksi in range(len(matriisi[0])):
        while sarake_indeksi < len(matriisi[0]) and rivi_indeksi < len(matriisi):
            if matriisi[rivi_indeksi][sarake_indeksi] == merkki:
                laskuri += 1
                if laskuri == 4:
                    # voitto
                    return True
            else:
                laskuri = 0         
                
            rivi_indeksi += 1
            sarake_indeksi += 1
        rivi_indeksi = 0
    
    laskuri = 0
    sarake_indeksi = 0
    for rivi_indeksi in range(len(matriisi)):
        while sarake_indeksi < len(matriisi[0]) and rivi_indeksi < len(matriisi):
            if matriisi[rivi_indeksi][sarake_indeksi] == merkki:
                laskuri += 1
                if laskuri == 4:
                    # voitto
                    return True
            else:
                laskuri = 0   
            rivi_indeksi += 1
            sarake_indeksi += 1
        sarake_indeksi = 0

    return False

def tarkista_oikea_ylhaalta_alas_pelikentta(matriisi, merkki):
    """ 
    Tarkistaa onko viistosti oikealta ylhäältä alas neljän merkin suoria
    """
    kaannetty_matriisi = []
    for peli_rivi in matriisi:
        kaannetty_matriisi.append([peli_rivi[i] for i in range(len(peli_rivi)-1, -1, -1)])
    return (tarkista_vasen_ylhaalta_alas_pelikentta(kaannetty_matriisi, merkki))

def kaiken_tarkistava(matriisi, merkki):
    """ 
    Yhdistää muut funktiot ja tarkistaa onko pelin voiton ehdot toteutuneet
    """
    return tarkista_vaaka_pelikentta(matriisi, merkki) or tarkista_pysty_pelikentta(matriisi, merkki) or tarkista_vasen_ylhaalta_alas_pelikentta(matriisi, merkki) or tarkista_oikea_ylhaalta_alas_pelikentta(matriisi, merkki)

def kirjaa_voittaja(voittaja, neljan_suora_tiedosto):
    """ 
    Kirjaa voittajan tiedostoon
    """
    with open(neljan_suora_tiedosto, "a") as tiedosto:
        tiedosto.write(voittaja + "\n")       

def hae_voittaja_pisteet(neljan_suora_tiedosto):
    """ 
    Hakee pisteet tiedostosta
    """
    voittaja_sanakirja = {}
    with open(neljan_suora_tiedosto, "r") as tiedosto:
        for rivi in tiedosto:
            nimi = rivi.strip()
            voittaja_sanakirja[nimi] = voittaja_sanakirja.get(nimi, 0) + 1
    return voittaja_sanakirja
        
def tulosta_pisteet():
    """ 
    Tulostaa voitot
    """
    neljan_suora_tiedosto = "neljan_suora_voittaja_tilasto"
    pisteet = hae_voittaja_pisteet(neljan_suora_tiedosto)
    jarjestetty = sorted(pisteet.items(), key = lambda item : item[1])
    jarjestetty.reverse()
    for pisteet in jarjestetty:
        print(f"{pisteet[0]}: {pisteet[1]} voittoa")

def menu_looppi():
    """ 
    Ohjaa pelin kulkua
    """
    pelaajan_nimi = ""
    while True:
        if pelaajan_nimi == "":
            pelaajan_nimi = kysy_nimea()
        vaihtoehto = vaihtoehdot()
        if vaihtoehto == "1":
            pelaajan_nimi = kysy_nimea()
        elif vaihtoehto == "2":
            nimi = pelaa_peli(pelaajan_nimi)
            kirjaa_voittaja(nimi, "neljan_suora_voittaja_tilasto")
        elif vaihtoehto == "3":
            tulosta_pisteet()
        elif vaihtoehto == "4":
            print("Kiitos peleistä ja näkemiin!")
            break


def kysy_nimea():
    """ 
    Kysyy pelaajan nimeä
    """
    nimi = ""
    while True:
        nimi = input("Anna pelaajan nimi:")
        if nimi != "" and nimi != "botti3000":
            break
    return nimi

def vaihtoehdot():
    """ 
    Antaa pelaajalle vaihtoehdot seuraavasta toiminnosta
    """
    vaihtoehto = ""
    lista = ["1","2","3","4"]
    while True:
        print("Vaihtoehto 1: vaihda nimi")
        print("Vaihtoehto 2: pelaa peli")
        print("Vaihtoehto 3: pistetaulu")
        print("Vaihtoehto 4: lopeta peli")
        vaihtoehto = input("Valitse vaihtoehto 1,2,3 tai 4:")
        if vaihtoehto in lista:
            return vaihtoehto
    

if (__name__=="__main__"):
    menu_looppi()
    

