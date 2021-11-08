# prosty program z tablicami

#wywołanie funkcji z innego pliku - intro  - sam wymyśliłem :)
from introOutro import intro
intro()

catNames = []
while True:
    print('Podaj imię kota numer ' + str(len(catNames) + 1) + ' (albo nic nie wpisuj i naciśnij Enter aby zakończyć)')
    name = input()
    if name == '':
        break
    catNames = catNames + [name]  # rozszerzanie listy - konkatencaja z nową wartością

print('Oto imiona kotów:')
for name in catNames:
    print(' - ' + name)

# sprawdzenie czy kod jest na liście

print('Jakiego kota szukasz? Podaj imię:')
findCat = input()
if findCat not in catNames:
    print('Nie mamy kota o imieniu: ' + findCat + '.')
else:
    print('Tak. ' + findCat + ' to mój kot!')

# Sprawdzanie czy w tabeli znajduje się wartość z listy, jeśli tak to podajemy jej pozycję
try:
    print('Kot o imieniu ' + findCat + ' ma indeks ' + str(catNames.index(findCat)) + ' w tabeli')

except ValueError:
    print('Brak takiego kota więc Ci nie podam jego indeksu')

# kolejna część

print('--- Inna czesc  ---')

supplies = ['długopisy', 'segregatory', 'zszywacze', 'zeszyty']

for i in range(len(supplies)):  # wykonujemy pętlę tyle razy ile jest elementów w pętli
    print('Indeks: ' + str(i) + ' na liście to: ' + supplies[i])

if 'długopisy' in supplies:
    print('Mamy długopisy!')

if 'rowery' not in supplies:
    print('Nie mamy rowerów!')

# dodawanie do listy z użyciem metody append
print('-------------------')
print('Po dodaniu do listy nowej pozycji mamy')
supplies.append('ołówki')
print(supplies)
#dodanie wartości do listy z użyciem metody insert - rozsunięcie pozycji
print('-------------------')
print('Przed dodaniem pozycji mamy:')
print(supplies)
print('Po zamianie pozycji mamy:')
supplies.insert(0,'super długopisy')
print(supplies)

#usuwanie pozycji z listy z użyciem remove - zsunięcie tego miejsca
print('-------------------')
print('Przed usunięciem pozycji mamy:')
print(supplies)
print('Po usunięciu pozycji mamy:')
supplies.remove('zeszyty')
print(supplies)

try:
    supplies.remove('sdsd')
except ValueError:
    print('Brak wartości do usunięcia w słowniku')
except:
    print('Nieznany błąd')

# inny sposób obsługi roznych błędów
try:
    supplies.remove('sdsd')
except (ValueError, TypeError) as error:
    #handle(error) # might log or have some other default behavior...
    print('to błąd')

# sortowanie wartości na liście
print('-------------------')
print('Przed posortowaniem mamy:')
print(supplies)
print('Po posortowaniu mamy:')
# supplies.sort() - to sortowanie wg Ascii a my chcemy alfabetycznie
supplies.sort(key=str.lower) #str.lower wszystkie litery zamieni na małe na potrzeby sortowania
print(supplies)
print('A teraz malejąco')
supplies.sort(reverse=True, key=str.lower) #str.lower wszystkie litery zamieni na małe na potrzeby sortowania
print(supplies)


#wywołanie funkcji z innego pliku - outro - sam wymyśliłem :)
from introOutro import outro
outro()
