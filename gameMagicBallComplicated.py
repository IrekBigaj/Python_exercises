#gra MagicBall z wykorzystaniem tablic
import random

#wywołanie funkcji z innego pliku - intro  - sam wymyśliłem :)
from introOutro import intro
intro()

print('Magiczna kula daje Ci odpowiedź na Twoje pytanie. Odpowiedź to:')
messages = ['To pewne','Zdecydowanie tak','Tak','Niejasna odpowiedź','Zapytaj później','Skoncentruj sie','Nie!','Nie wygląda to dobrze','Bardzo wątpliwe']

print(messages[random.randint(0,len(messages)-1)])

#wywołanie funkcji z innego pliku - outro - sam wymyśliłem :)
from introOutro import outro
outro()