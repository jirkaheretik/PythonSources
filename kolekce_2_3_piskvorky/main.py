"""
/*  _____ _______         _                      _
 * |_   _|__   __|       | |                    | |
 *   | |    | |_ __   ___| |___      _____  _ __| | __  ___ ____
 *   | |    | | '_ \ / _ \ __\ \ /\ / / _ \| '__| |/ / / __|_  /
 *  _| |_   | | | | |  __/ |_ \ V  V / (_) | |  |   < | (__ / /
 * |_____|  |_|_| |_|\___|\__| \_/\_/ \___/|_|  |_|\_(_)___/___|
 *
 *                      ___ ___ ___
 *                     | . |  _| . |  LICENCE
 *                     |  _|_| |___|
 *                     |_|
 *
 *    REKVALIFIKAČNÍ KURZY  <>  PROGRAMOVÁNÍ  <>  IT KARIÉRA
 *
 * Tento zdrojový kód je součástí profesionálních IT kurzů na
 * WWW.ITNETWORK.CZ
 *
 * Kód spadá pod licenci PRO obsahu a vznikl díky podpoře
 * našich členů. Je určen pouze pro osobní užití a nesmí být šířen.
 * Více informací na http://www.itnetwork.cz/licence
 */
"""
def draw_board(board):
    print("  1 2 3 4 5 6 7 8 9")
    for i in range(9):
        row = str(i + 1) + " "
        for j in range(9):
            row += board[i][j] + " "
        print(row)


def get_move(player, board):
    """Získá tah hráče"""
    print()
    if player == "O":
        print("Na řadě je hráč s kolečky")
    else:
        print("Na řadě je hráč s křížky")
    while True:
        x = input("Zadej pozici X kam chceš táhnout: ")
        y = input("Zadej pozici Y kam chceš táhnout: ")
        if not (x.isdigit() and y.isdigit()):
            print("Zadej prosím celé číslo.")
        elif int(x) not in range(1, 10) or int(y) not in range(1, 10):
            print("Neplatná pozice, zadej ji prosím znovu.")
        elif board[int(y) - 1][int(x) - 1] != " ":
            print("Neplatná pozice, zadej ji prosím znovu.")
        else:
            return f"{x},{y}"


def is_valid_move(move):
    """Zkontroluje, zda je tah platný"""
    if len(move) != 3:
        return False
    if move[1] != ",":
        return False
    try:
        x = int(move[0])
        y = int(move[2])
    except ValueError:
        return False
    if x < 1 or x > 9 or y < 1 or y > 9:
        return False
    return True


def is_winner(board, player):
    """Zkontroluje, zda hráč vyhrál"""
    # horizontální kontrola
    for i in range(9):
        for j in range(5):
            if board[i][j] == player and board[i][j + 1] == player and board[i][j + 2] == player and board[i][
                j + 3] == player and board[i][j + 4] == player:
                return True
    # vertikální kontrola
    for i in range(5):
        for j in range(9):
            if board[i][j] == player and board[i + 1][j] == player and board[i + 2][j] == player and board[i + 3][
                j] == player and board[i + 4][j] == player:
                return True
    # kontrola hlavní diagonály
    for i in range(5):
        for j in range(5):
            if board[i][j] == player and board[i + 1][j + 1] == player and board[i + 2][j + 2] == player and \
                    board[i + 3][j + 3] == player and board[i + 4][j + 4] == player:
                return True
    # kontrola vedlejší diagonály
    for i in range(5):
        for j in range(4, 9):
            if board[i][j] == player and board[i + 1][j - 1] == player and board[i + 2][j - 2] == player and \
                    board[i + 3][j - 3] == player and board[i + 4][j - 4] == player:
                return True
    return False


def is_board_full(board):
    for row in board:
        for spot in row:
            if spot == ' ':
                return False
    return True


def play_game():
    # Vytvoření hrací desky
    board = []
    for i in range(9):
        board.append([" "] * 9)

    # Vypsání prázdné hrací desky
    draw_board(board)

    # Hráč, který je na řadě jako první
    current_player = "X"

    # Hlavní smyčka hry
    while True:
        # Získání tahů hráče
        move = get_move(current_player, board)
        while not is_valid_move(move):
            move = get_move(current_player, board)

        # Zpracování tahu na hrací desce
        x, y = map(int, move.split(","))
        board[y - 1][x - 1] = current_player

        # Vypsání aktualizované hrací desky
        draw_board(board)

        # Kontrola, zda hráč vyhrál
        if is_winner(board, current_player):
            if current_player == "O":
                print("Vyhrál hráč s kolečky.")
            else:
                print("Vyhrál hráč s křížky.")
            break

        # Kontrola, zda došlo k remíze
        if is_board_full(board):
            print("Remíza!")
            break

        # Předání tahu dalšímu hráči
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"


play_game()