# Programik zapaiętujący daty urodzin bazujący na słowniku
import introOutro

introOutro.intro()

birthdays = {'Alicja': '1 kwietnia', 'Bob': '12 grudnia', 'Karol': '4 marca'}

while True:
    print('Podaj imię: (pozostaw puste, aby zakończyć program)')
    name = input()
    if name == '':
        break
    if name in birthdays:
        print(birthdays[name] + ' to dzień urodzin o imieniu: ' + name + '.')
    else:
        print('Nie znaleziono informacji o urodzinach osoby o imieniu: ' + name + '.')
        print('Kiedy przypadają te urodziny?')
        bday = input()
        birthdays[name] = bday
        print('Data urodzin została zaktualizowana')

# metoda values() dla słownika zwraca wszystkie wartości ze słownika
# może być wykorzystana w pętli for, ale nie jest listą - tak jak i poniższe dwie
# metoda keys() robi analogicznie dla kluczy
# metoda items() wyświetla pary klucz-wartość
# można wyniki tych 3 metod zamienić na liste podstawiając do funkcji list()

print('No to podsumowanie:')
print('Wyświetlmy wszytkie daty urodzin:')
for k in birthdays.values():
    print(k)

print('Wyświetlmy wszystkie imiona:')
for i in birthdays.keys():
    print(i)

print('Wyświetlmy cały kalendarz:')
for j in birthdays.items():
    print(j)

print(list(birthdays.values()))

# przypisanie do dwóch zmiennych klucza i wartości ze słownika

for m, n in birthdays.items():
    print('Klucz: ' + m + ', wartość: ' + n + '.')

introOutro.outro()
