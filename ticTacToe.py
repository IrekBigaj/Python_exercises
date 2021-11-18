# Gra w kółko i krzyżyk
import introOutro

introOutro.intro_program('Kółko i krzyżyk')

the_game_board = {'top-Left': ' ', 'top-Middle': ' ', 'top-Right': ' ',
                  'middle-Left': ' ', 'middle-Middle': ' ', 'middle-Right': ' ',
                  'down-Left': ' ', 'down-Middle': ' ', 'down-Right': ' '}


# Funkcja wyswietlajaca plansze
def print_board(board):
    print(board['top-Left'] + '|' + board['top-Middle'] + '|' + board['top-Right'])
    print('-+-+-')
    print(board['middle-Left'] + '|' + board['middle-Middle'] + '|' + board['middle-Right'])
    print('-+-+-')
    print(board['down-Left'] + '|' + board['down-Middle'] + '|' + board['down-Right'])
# TODO: TicTacToe - zastanów się czy nie zmienić nazewnictwa pól dla łatwiejszego grania


turn = 'X'

for i in range(9):
    print_board(the_game_board)
    print('Ruch gracza ' + turn + ' . W którym polu stawiasz znak?')
    move = input()
    the_game_board[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
print_board(the_game_board)

# TODO: TicTacToe - dodaj sprawdzanie błędnych wpisów lokalizacji,
# TODO: TicTacToe - zablokuj możliwość wpisywania tam gdzie są dane
# TODO: TicTacToe - dodaj sprawdzanie wyniku gry
