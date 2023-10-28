#  _____ _______         _                      _
# |_   _|__   __|       | |                    | |
#   | |    | |_ __   ___| |___      _____  _ __| | __  ___ ____
#   | |    | | '_ \ / _ \ __\ \ /\ / / _ \| '__| |/ / / __|_  /
#  _| |_   | | | | |  __/ |_ \ V  V / (_) | |  |   < | (__ / /
# |_____|  |_|_| |_|\___|\__| \_/\_/ \___/|_|  |_|\_(_)___/___|
#                                _
#              ___ ___ ___ _____|_|_ _ _____
#             | . |  _| -_|     | | | |     |  LICENCE
#             |  _|_| |___|_|_|_|_|___|_|_|_|
#             |_|
#
# IT ZPRAVODAJSTVÍ  <>  PROGRAMOVÁNÍ  <>  HW A SW  <>  KOMUNITA
#
# Tento zdrojový kód je součástí výukových seriálů na
# IT sociální síti WWW.ITNETWORK.CZ
#
# Kód spadá pod licenci prémiového obsahu a vznikl díky podpoře
# našich členů. Je určen pouze pro osobní užití a nesmí být šířen.
# Více informací na http://www.itnetwork.cz/licence

from lokace import Lokace

class Hra():

    hrad = Lokace("Hrad", "Stojíš před okovanou branou gotického hradu, která je zřejmě jediným vchodem do pevnosti. Klíčová dírka je pokryta pavučinami, což vzbuzuje dojem, že je budova opuštěná.")
    les1 = Lokace("Les", "Jsi na lesní cestě, která se klikatí až za obzor, kde mizí v siluetě zapadajícího slunce. Ticho podvečerního lesa občas přeruší zpěv posledních ptáků.")
    les2 = Lokace("Lesní rozcestí", "Nacházíš se na lesním rozcestí.")
    les3 = Lokace("Les", "Jsi na lesní cestě, která se klikatí až za obzor, kde mizí v siluetě zapadajícího slunce. Ticho podvečerního lesa občas přeruší zpěv posledních ptáků.")
    rybnik = Lokace("Rybník", "Došel jsi ke břehu malého rybníka. Hladina je v bezvětří jako zrcadlo. Kousek od tebe je dřevěná plošina se stavidlem.")
    les4 = Lokace("Les", "Jsi na lesní cestě, která se klikatí až za obzor, kde mizí v siluetě zapadajícího slunce. Ticho podvečerního lesa občas přeruší zpěv posledních ptáků.")
    dum = Lokace("Dům", "Stojíš před svým rodným domem, citíš vůni čerstvě nasekaného dřeva, která se line z hromady vedle vstupních dvěří.")
    
	# Propojení lokací
    hrad.vychod = les1
    les1.zapad = hrad
    les1.vychod = les2
    les2.zapad = les1
    les2.vychod = les3
    les2.jih = les4
    les3.zapad = les2
    les3.vychod = rybnik
    rybnik.zapad = les3
    les4.sever = les2
    les4.vychod = dum
    dum.zapad = les4
    # Uložení aktuální lokace
    aktualni_lokace = dum

    # Zpracuje textová příkaz
    def zpracuj_prikaz(self, prikaz):      
        prikaz = prikaz.lower()
        if prikaz.startswith("jdi"):
            
            if prikaz.endswith("sever") and self.aktualni_lokace.sever:
                self.aktualni_lokace = self.aktualni_lokace.sever
            elif prikaz.endswith("jih") and self.aktualni_lokace.jih:
                self.aktualni_lokace = self.aktualni_lokace.jih
            elif prikaz.endswith("západ") and self.aktualni_lokace.zapad:
                self.aktualni_lokace = self.aktualni_lokace.zapad
            elif prikaz.endswith("východ") and self.aktualni_lokace.vychod:
                self.aktualni_lokace = self.aktualni_lokace.vychod
            else:
                print("Tímto směrem nelze jít.")
            
        elif prikaz != "konec":           
            print("Můj vstupní slovník neobsahuje tento příkaz.")

    # Vrátí aktuální lokaci
    def vrat_auktualni_lokaci(self):
        return self.aktualni_lokace