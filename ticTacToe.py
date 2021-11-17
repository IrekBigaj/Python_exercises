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


print_board(the_game_board)
