"""
Hra Chytrák z Apple iOS
1. Nastavení/spuštění hry:
- počet hráčů (2+)
- jména hráčů, tím je dané i pořadí
- počet vítězných bodů
- jazyk, v případě, že bude více mutací (zejména balíků otázek)
2. Samotná hra:
+ vyzve hráče, který je na řadě, potvrdí
+ objeví se otázka a deset odpovědí, z nichž 5 je správných
+ hráčům jsou odpovědi zobrazovány v náhodném pořadí (tj. dva různí hráči typicky budou mít stejnou odpověď na jiné pozici)
+ hráč může na kteroukoli odpověď kliknout, objeví se zeleně/červeně podle toho, zdali je správně
+ v případě, že je odpověď správná, může hrát dál a označit další odpověď, vždy má k dispozici tlačítko "Konec kola"
+ hráč obdrží N*(N+1) bodů v daném kole, pokud neudělal chybu, a 0 bodů, pokud udělal chybu
- zvuky pro správné a špatné odpovědi
+ během hraní je hráči vždy k dispozici tabulka s dosavadním stavem bodů
+ po ukončení kola je na řadě další hráč, který dostane *stejnou* otázku
+ když se vystřídají všichni, vyhodnotí se, zda není konec (někdo dosáhl vítězného skóre),
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
import hashlib

LANG = "cz"
GOOD_COUNT = 5
BAD_COUNT = 5

class BgColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class ConsoleUi:
    """
    Represents object interacting with the user.
    Basic representation uses console, you can create a child object and overwrite anything needed, others will still
    use console, if that makes sense.
    """

    @staticmethod
    def pprint(text, color):
        print(f"{color}{text}{BgColors.ENDC}")

    @staticmethod
    def clear():
        print("\n" * 5)

    def error(self, text):
        """
        Displays error message to the user
        """
        self.pprint(text, BgColors.FAIL)

    def status(self, text):
        """
        Displays status message to the user
        """
        self.pprint(text, BgColors.HEADER)

    def player_update(self, name, current, total):
        self.status(f"Hráč {name} v tomto kole nahrál {current} bodů a má celkem {total}")

    def log(self, text):
        self.pprint(text, BgColors.OKCYAN)

    def game_over(self, players):
        self.clear()
        self.pprint("KONEC HRY!\n==========", BgColors.OKBLUE)
        poradi = 1
        for player in players:
            print(f"{poradi}. {player['name']}\t\t{player['score']}")
            poradi += 1

    def notify_player(self, name):
        self.pprint("Na řadě je hráč " + name + "!", BgColors.OKGREEN)
        input("Stiskni ENTER, až budeš připraven.")

    def get_guess(self):
        again = True
        answer = -1
        while again:
            try:
                answer = int(input("Tvoje volba? ")) - 1
                again = False
            except ValueError:
                print("To ne, zkus číslo.")
        self._last_answer = answer
        self._answers.append(answer)
        return answer

    def guess_status(self, isCorrect):
        if isCorrect:
            self.pprint(f"To je {len(self._answers)}. správná odpověď!", BgColors.OKGREEN)
        else:
            self.pprint(f"Chyba! Vybraná odpověď {self._all_answers[self._last_answer]} není správně!", BgColors.FAIL)

        pass

    def game_state(self, status):
        self.pprint(status, BgColors.OKCYAN)

    def display_question(self, status, q, answers):
        self.game_state(status)
        self._all_answers = answers
        self._answers = []
        self.pprint("Otázka:", BgColors.BOLD)
        self.pprint(q, BgColors.BOLD)
        self.pprint("0. Konec kola (hraje další hráč)", BgColors.OKBLUE)
        i = 1
        for a in answers:
            self.pprint(f"{i}. {a}", BgColors.OKBLUE)
            i += 1

    def enter_player_list(self):
        pass

    def enter_player(self):
        pass

    def enter_max_score(self):
        pass


class Db:
    def __init__(self, ui):
        self._ui = ui
        with open('pudovka.json', 'r') as otazky_file:
            data = json.load(otazky_file)
            self.otazky = data[LANG]
        self._ui.status(f"Loaded questions, length: {len(self.otazky)}")

    def get_number_of_questions(self):
        return len(self.otazky)

    def get_question(self):
        if self.otazky is None:
            self._ui.error("ERROR: No question file for current language.")
            return None
        num = random.randrange(len(self.otazky))
        data = self.otazky[num]
        if len(data["good"]) < GOOD_COUNT or len(data["bad"]) < BAD_COUNT:
            self._ui.error(f"ERROR: Not enough answers in question {num}")
            return None
        good = tuple(self._get_number_of_items(data["good"], GOOD_COUNT))
        bad = tuple(self._get_number_of_items(data["bad"], BAD_COUNT))
        return data["q"], good, bad

    @staticmethod
    def _get_number_of_items(haystack, count):
        result = []
        while len(result) < count:
            good_num = random.randrange(len(haystack))
            if not haystack[good_num] in result:
                result.append(haystack[good_num])
        return result


def _sort_by_score(e):
    return e['score']


class Game:
    def __init__(self, db, ui, players, target_score = 50):
        self._db = db
        self._ui = ui
        self._target_score = target_score
        self._question_hashlist = []
        my_players = []
        for p in players:
            my_players.append({"name": p, "score": 0})
        self._players = my_players

    def __str__(self):
        result = f"Playing to {self._target_score} - "
        for p in self._players:
            result += f"{p['name']}: {p['score']} "
        return result

    def play(self):
        self._question_hashlist = []
        while not self.check_score():
            if not self.do_round():
                break
        self._players.sort(key=_sort_by_score, reverse=True)
        self._ui.game_over(self._players)

    def do_round(self):
        # get a question from db
        generate = True
        digest = ""
        while generate:
            try:
                q, good, bad = self._db.get_question()
            except TypeError:
                return False
            digest = hashlib.md5(q.encode()).hexdigest()
            if digest not in self._question_hashlist:
                generate = False
                self._question_hashlist.append(digest)
            elif len(self._question_hashlist) >= self._db.get_number_of_questions():
                generate = False
        self._ui.status(f"Máme tu otázku {digest}")

        all_answers = list(good + bad)
        # for each player:
        for player in self._players:
            random.shuffle(all_answers)
            # display notification, let player confirm
            self._ui.notify_player(player['name'])
            # display question and answers
            self._ui.display_question(self.__str__(), q, tuple(all_answers))
            dead = False
            answer = 0
            answers = set()
            while not dead and answer != -1:
                answer = self._ui.get_guess()
                if answer < 0:
                    break
                if all_answers[answer] in good:
                    answers.add(answer)
                    self._ui.guess_status(True)
                else:
                    self._ui.guess_status(False)
                    answers = set() # clear the answers so that no points are given!
                    dead = True

            # wait for End-of-round
            current = len(answers) * (len(answers) + 1) // 2
            player['score'] += current
            self._ui.status(player['name'], current, player['score'])
            self._ui.clear()
        return True # all ok

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
    score = 150
    players_short = ["Filip", "Jirka"]
    players_family = ["Filip", "Jirka", "Jitka", "Jim"]
    players_alone = ["Jirka"]
    players_avatars = ["Jirka", "Karel", "Heretik", "Charlie"]
    ui = ConsoleUi()
    game = Game(Db(ui), ui, players_alone, score)
    game.play()
