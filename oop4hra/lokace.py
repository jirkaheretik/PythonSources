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

class Lokace():
    # Třída reprezentuje lokaci

    sever   = None # Lokace na severu
    jih     = None # Lokace na jihu
    zapad   = None # Lokace na západě
    vychod  = None # Lokace na východě

    nazev   = None # Název lokace
    popis   = None # Dlouhý popis lokace

    def __init__(self, nazev, popis):
        self.nazev = nazev
        self.popis = popis

    def __str__(self):
        vystup = ( self.nazev + "\n"
                 + self.popis + "\n\n")
        smery = ""
        if self.sever:
            smery += "sever "
        if self.jih:
            smery += "jih "
        if self.zapad:
            smery += "západ "
        if self.vychod:
            smery += "východ "
        vystup += "Můžeš jít na {0}\n".format(smery)
        return vystup