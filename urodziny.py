# Programik zapaiętujący daty urodzin bazujący na słowniku

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
