
import kostka
class Postava:

    def __init__(self, jmeno, zivoty, utok, obrana, inteligence, kostka):
        """
        Třída pro vytváření postav obsahuje základní vlastnosti a mechanismy

        """
        self.jmeno=jmeno
        self.zivoty=zivoty
        self.max_zivot=zivoty
        self.utok=utok
        self.obrana=obrana
        self.inteligence=inteligence
        self.kostka=kostka # kostka, kterou postava bude házet při boji

    def __str__(self):
        """
        :return: Grafické vypsání třídy postavy
        """
        return str(f"Ahoj, já jsem hrdina {self.jmeno} mám {self.zivoty} životů, a těším se na to, co spolu zažijeme")

    def je_nazivu(self):
        """
        :return: Zjišťuje zda je postava naživu
        """
        return self.zivoty>0


    def graficky_ukazatel(self, aktulani, maxilmani, popis):
        """
        Grafické znázornění hodnoty
        :param aktulani: Zadání aktuální hodnoty
        :param maxilmani: Zadání maxiální honoty
        :param popis: Popis o jakou hodnotu jde
        :return: Hrafické znázornění hodnoty
        """

        if aktulani==(maxilmani/2):
            return f"Aktuální počet {popis} je {aktulani} [{'-'*(maxilmani-aktulani)}{'X'*aktulani}]\n Jsi v půlce {popis}"
        if aktulani==3:
            return f"Aktuální počet {popis} je {aktulani} [{'-' * (maxilmani - aktulani)}{'X' * aktulani}]\n Nechci tě stresovat, ale zbývají ti jen 3 jednotky {popis}"
        if aktulani==1:
            return f"Aktuální počet {popis} je {aktulani} [{'-' * (maxilmani - aktulani)}{'X' * aktulani}]\n Konec se blíží !!! "
        else:
            return f"Aktuální počet {popis} je {aktulani} [{'-' * (maxilmani - aktulani)}{'X' * aktulani}]"


    def graficky_zivot(self):
        """
        Grafické znázornění životů
        """
        return self.graficky_ukazatel(self.zivoty, self.max_zivot, "životů")


    def utoc(self, protivnik):
        """
        Metoda pro útok na protivníka
        :param protivnik: protivník na kterého je útok veden
        :return: sílá útoku a zavolání metody braň se
        """
        hod_utok=self.kostka.hod() # zavolá hod kostkou
        uder = self.utok + hod_utok # vlastní útok je součtem útoku postavy a hodu jeho ksotkou
        print(f"Na kostce padlo {hod_utok}, takže {self.jmeno} útočí za {self.utok+hod_utok}")
        protivnik.bran_se(uder) # zavolá protivníka a jeho metodu braň se

    def bran_se(self, uder):
        """
        Metoda pro obranu před útokem
        :param uder: síla úderu který je na něj veden
        :return: Ubrání životů podle poměru obrany a útoku
        """
        hod_obrana=self.kostka.hod() # zavolá hod kostkou
        print(f"Na kostce padlo {hod_obrana}, takže {self.jmeno} se brání za {self.obrana+hod_obrana}")
        zraneni = uder - (self.obrana+hod_obrana) # od úderu se dečte obrana a pokud něco zbyde, odebírají se životy
        if zraneni > 0:
            print (f"{self.jmeno} utrpěl zranění {zraneni}")
            self.zivoty-=zraneni
            if self.zivoty<0:
                self.zivoty=0
                print(f"{self.jmeno} utrpěl smrtelné zranění a zemřel")

        else:
            print(f"{self.jmeno} bez potíží odrazil útok")


class Hrdina(Postava):
    def __init__(self, jmeno, zivoty, utok, obrana, inteligence, kostka, hlad ):
        """
        Třída pro hlavního hlavního hrdinu příběhu. Třída vychází s třídy Postava
        :param hlad: Když hodnota hladu klesena na nula, tak postava začne ztrácet životy
        """
        super().__init__(jmeno, zivoty, utok, obrana, inteligence, kostka)
        self.hlad=hlad # aktuální úroveň hladu
        self.max_hlad=hlad #maximální uroveň hladu

    def __str__(self):
        """
        Textový výpis Hrdiny
        """
        return str(f"""Ahoj, já jsem hrdina {self.jmeno} mám {self.zivoty} životů, útočím za {self.utok} bodů a můj štít vydrží až {self.obrana} ran.
Jsem docela jedlík, hlad začnu mít po {self.hlad} hodinách. Do menzy mě sice nevzali, ale moje inteligence dosahuje {self.inteligence} bodů.
        Ale teď už dost keců a hurá za dobrodružstvím .""")

    def jez (self):
        """
        Metoda která ubírá míru nasicení a podku kledne na nulu,  tak začne ubírat životy
        :return: upravenou hodnitu nasícení, popřápadě životů
        """
        self.hlad-=1
        if self.hlad <0:
            self.hlad=0
            self.zivoty-=1

    def graficky_hlad(self):
        """
        Grafické znázornění hladu
        """
        return self.graficky_ukazatel(self.hlad, self.max_hlad, "hladu")

    seznam_veci=[] # sem se ukládá název nalezenách věcí
    popis_veci=[] # sem se ukládá popis nalezených věcí
    ucinek_veci=[] # sem se ukládá účinek nalezených věcí.
        # pozor, vždy je potřeba mít v každém seznamu setejný poče věcí ve stejném pořadí #


    def vypis_veci(self):
        """
        Vypíše veškerý obsah v seznamu věcí, společně s jeho popisem a účinky
        """
        for polozka in range(len(self.seznam_veci)):
            print(f"{polozka} - {self.seznam_veci[polozka]} - Pomúže ti {self.popis_veci[polozka]} - Díky tomu máš vylepšení {self.ucinek_veci[polozka]}")
        print()
        print(f"Tvoje aktální schopnosti jsou: Životy: {self.zivoty}, Útok: {self.utok}, Obrana: {self.obrana}, Inteligence: {self.inteligence}, Hlad: {self.hlad},\n")

    def pouzij (self):
        """
        Podle zvoleného indexu aplikuje vylepšní dané položky a tu násleně ze seznamu smaže
        :return: Vylepšné atributy a aktulizivaný seznam věcí
        """
        index=int(input("Kterou položku chceš využít?\n"))
        if index <0 or index > len(self.seznam_veci):
            print("Netuším, jak jsi na to přišel, ale takovou položku v tlumoku nemáš")
        else:
            if "voda" in self.seznam_veci[index]: # pokud položka pod zvoleným indexem obsahuje slovo "voda" tak zvedne úroveň životů
                self.zivoty += int(self.ucinek_veci[index])
            if "meč" in self.seznam_veci[index]:  # pokud položka pod zvoleným indexem obsahuje slovo "meč" tak zvedne úroveň útoků
                self.utok += int(self.ucinek_veci[index])
            if "štít" in self.seznam_veci[index]: # pokud položka pod zvoleným indexem obsahuje slovo "štít" tak zvedne úroveň obrany
                self.obrana += int(self.ucinek_veci[index])
            if "kniha" in self.seznam_veci[index]: # pokud položka pod zvoleným indexem obsahuje slovo "kniha" tak zvedne úroveň inteligence
                self.inteligence += int(self.ucinek_veci[index])
            if "boruvka" in self.seznam_veci[index]:# pokud položka pod zvoleným indexem obsahuje slovo "boruvka" tak zvedne úroveň hladu
                self.hlad += int(self.ucinek_veci[index])

            print(f"Skvěle, použil jsi {self.seznam_veci[index]}")
            print(f"Tvoje aktální schopnosti jsou: Životy: {self.zivoty}, Útok: {self.utok}, Obrana: {self.obrana}, Inteligence: {self.inteligence}, Hlad: {self.hlad},")
            del self.seznam_veci[index] # vymaže název zvolené položky
            del self.popis_veci[index] # vymaže popis zvolené položky
            del self.ucinek_veci[index] # vymaže účinek zvolené položky


hrdina=Hrdina(None,10,10,10,10,kostka.desetistena,10) # instance Hlavního hrdiny
drak=Postava("Šmak", 20, 20, 20, 10, kostka.sestisnna) # instance Hlavního záporáka

