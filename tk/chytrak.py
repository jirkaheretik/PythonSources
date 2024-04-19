"""
Hra Chytrák z Apple iOS
1. Nastavení/spuštění hry:
- počet hráčů (2+)
- jména hráčů, tím je dané i pořadí
- počet vítězných bodů
- jazyk, v případě, že bude více mutací (zejména balíků otázek)
2. Samotná hra:
- vyzve hráče, který je na řadě, potvrdí
- objeví se otázka a deset odpovědí, z nichž 5 je správných
- hráčům jsou odpovědi zobrazovány v náhodném pořadí (tj. dva různí hráči typicky budou mít stejnou odpověď na jiné pozici)
- hráč může na kteroukoli odpověď kliknout, objeví se zeleně/červeně podle toho, zdali je správně
- v případě, že je odpověď správná, může hrát dál a označit další odpověď, vždy má k dispozici tlačítko "Konec kola"
- hráč obdrží N*(N+1) bodů v daném kole, pokud neudělal chybu, a 0 bodů, pokud udělal chybu
- zvuky pro správné a špatné odpovědi
- během hraní je hráči vždy k dispozici tabulka s dosavadním stavem bodů
- po ukončení kola je na řadě další hráč, který dostane *stejnou* otázku
- když se vystřídají všichni, vyhodnotí se, zda není konec (někdo dosáhl vítězného skóre),
  a pokud není, hra pokračuje prvním hráčem a další otázkou
- v případě přebírání dat od dalších uživatelů možno sledovat/zaznamenávat počet zobrazení otázky,
  případně hash vybrané sady odpovědí, možno označit "bullshit question", "question needs repairs", "problems with answers"

- Solitér režim: nějaký větší počet bodů, např. 200, a na kolik otázek to dokáže překonat+žebříček
- Hardcore režim:
1) Ke každé otázce více správných i nesprávných odpovědí, tři levely obtížnosti odpovědí,
   vybrat vždy jednu easy, 1-3 mid, 1-3 hard
2) Viz výše, ale možno v konkrétní sadě mít i 4 nebo 6 správných (a tedy i špatných) odpovědí

Navrhovaný název: PUDOVKA
Pudovka, "pade na pade", tedy "buď to půjde, nebo to nepůjde". Máš na to?
V každém kole dostaneš otázku a s ní deset odpovědí, ale jen pět z nich je správných. Tvým úkolem je vybrat z nabízené
sady odpovědí pouze ty správné. Někde si budeš jist, někde budeš váhat. A tím to začne být zajímavé, protože každá další
odpověď přináší zvýšený zisk, ale také zvýšené riziko, protože pokud se spleteš, přijdeš o všechny body za dané kolo!


Funkce:
- připojení k db
- načtení otázky včetně odpovědí
- inicializace, tj. získání tuplu s objekty hráčů, každý obsahuje dictionary
  s jménem hráče a jeho skóre (na začátku vždy 0). Dále získáme počet vítězných bodů.
-

JSON pro otázky:
- lang
- question
- good answers
- bad answers


"""
import json
import random

LANG = "cz"
GOOD_COUNT = 5
BAD_COUNT = 5

class Db:
    def __init__(self):
        with open('pudovka.json', 'r') as otazky_file:
            self.otazky = json.load(otazky_file)
        print(f"Loaded questions, length: {len(self.otazky)}")

    def get_question(self):
        if self.otazky is None:
            print("ERROR: No question file")
            return None
        num = random.randrange(len(self.otazky))
        data = self.otazky[num]
        # sanity check:
        if data["lang"] != LANG:
            print(f"ERROR: Wrong language in question {num}: {data['lang']}")
            return None
        if len(data["good"]) < GOOD_COUNT or len(data["bad"]) < BAD_COUNT:
            print(f"ERROR: Not enough answers in question {num}")
            return None
        good = tuple(self._get_number_of_items(data["good"], GOOD_COUNT))
        bad = tuple(self._get_number_of_items(data["bad"], BAD_COUNT))
        return data["q"], good, bad

    def _get_number_of_items(self, haystack, count):
        result = []
        while len(result) < count:
            good_num = random.randrange(len(haystack))
            if not haystack[good_num] in result:
                result.append(haystack[good_num])
        return result


def _sort_by_score(e):
    return e['score']


class Game:
    def __init__(self, db, players, target_score = 50):
        self._db = db
        self._target_score = target_score
        my_players = []
        for p in players:
            rec = {}
            rec["name"] = p
            rec["score"] = 0
            my_players.append(rec)
        self._players = my_players

    def __str__(self):
        result = f"Playing to {self._target_score}\n"
        for p in self._players:
            result += f"{p['name']}: {p['score']} "
        return result

    def play(self):
        while not self.check_score():
            self.do_round()
        print("\n" * 10)
        print("KONEC HRY!")
        print("==========")
        self._players.sort(key=_sort_by_score, reverse=True)
        poradi = 1
        for player in self._players:
            print(f"{poradi}. {player['name']}\t\t{player['score']}")
            poradi += 1

    def do_round(self):
        # get a question from db
        q, good, bad = self._db.get_question()
        #print(q)
        #print(good)
        #print(bad)
        all_answers = list(good + bad)
        #print(all_answers)
        # for each player:
        for player in self._players:
            random.shuffle(all_answers)
            # display notification, let player confirm
            print(f"Na řadě je hráč {player['name']}!")
            input("Stiskni ENTER, až budeš připraven.")
            # display question and answers
            print(self)
            print("Otázka:")
            print(q)
            print("0. Konec kola (hraje další hráč)")
            i = 1
            for a in all_answers:
                print(f"{i}. {a}")
                i += 1
            dead = False
            answer = 0
            answers = set()
            while not dead and answer != -1:
                answer = int(input("Tvoje volba? ")) - 1
                if answer < 0:
                    break
                if all_answers[answer] in good:
                    print("To je správná odpověď!")
                    answers.add(answer)
                else:
                    print(f"Chyba! Vybraná odpověď {all_answers[answer]} není správně!")
                    answers = set() # clear the answers so that no points are given!
                    dead = True

            # wait for End-of-round
            score = len(answers) * (len(answers) + 1) // 2
            player['score'] += score
            print(f"Hráč {player['name']} v tomto kole nahrál {score} bodů a má celkem {player['score']}")
            print("\n" * 3)

    def check_score(self):
        """
        Returns true if any of the players reached the final score
        :return:
        """
        for p in self._players:
            if p["score"] >= self._target_score:
                return True
        return False

if __name__ == '__main__':
    game = Game(Db(), ["Jirka", "Karel", "Heretik", "Charlie"], 20)
    game.play()
