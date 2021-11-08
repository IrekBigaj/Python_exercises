# Simple game - Guess the number
import random, sys


###########################################################
# Funkcja intro() - Ma za zadanie wyświetlić formatkę     #
# startową i dane autora                                  #
###########################################################
def intro():
    print('----------------------------')
    print('|  Program ZGADNIJ LICZBĘ  |')
    print('|                          |')
    print('|                          |')
    print('|    by Alien Software     |')
    print('|      Copyright 2021      |')
    print('----------------------------')
    print()
    print()


###########################################################
# koniec funkcji intro() #################################
###########################################################

###########################################################
# Funkcja outro() - Stopka końcowa #
###########################################################
def outro():
    print('----------------------------')
    print('|  Program ZGADNIJ LICZBĘ  |')
    print('|                          |')
    print('|    Dzięki za zabawę      |')
    print('|   Zapraszamy ponownie    |')
    print('|                          |')
    print('|    by Alien Software     |')
    print('|      Copyright 2021      |')
    print('----------------------------')
    print()
    print()


###########################################################
# koniec funkcji outro() #################################
###########################################################


###########################################################
# Program właściwy ########################################
###########################################################

intro()
print('Wybierz poziom trudności:')
print(' 1 - łatwy')
print(' 2 - normalny')
print(' 3 - trudny')
print('Na każdym poziomie masz tylko 6 prób zgadnięcia liczby!')

# Pobranie liczby z kontrolą błędów

try:
    getGameLevel = int(input())
except ValueError:
    print('!!! BŁĄD - nie podałeś liczby. Żegnaj kolego! Do następnego razu!')
    outro()
    sys.exit()
except TypeError:
    print('!!! BŁĄD - nie podałeś liczby. Żegnaj kolego! Do następnego razu!')
    outro()
    sys.exit()

if getGameLevel == 1:
    LavelMaxNumber = 20
    maxGuessesNumber = 6
elif getGameLevel == 2:
    LavelMaxNumber = 100
    maxGuessesNumber = 6
elif getGameLevel == 3:
    LavelMaxNumber = 1000
    maxGuessesNumber = 6
else:
    print('!!! BŁĄD. Wybrałeś zły poziom. Żegnaj kolego! Do następnego razu!')
    outro()
    sys.exit()

# Losowanie liczby w danej grze
mySecretNumber = random.randint(1, LavelMaxNumber)

print()
print('Mam na myśli jakąś liczbę z zakresu od 1 do ' + str(LavelMaxNumber))

# Właściwy mechaniz gry

for guessesTaken in range(1, maxGuessesNumber + 1):
    print()
    print('Próba numer: ' + str(guessesTaken) + '. Spróbuj odgadnąć liczbę!')

    # Pobranie liczby z kontrolą błędów

    try:
        getGuess = int(input())
    except ValueError:
        print('!!! BŁĄD - nie podałeś liczby. Żegnaj kolego! Do następnego razu!')
        outro()
        sys.exit()
    except TypeError:
        print('!!! BŁĄD - nie podałeś liczby. Żegnaj kolego! Do następnego razu!')
        outro()
        sys.exit()

    if getGuess < mySecretNumber:
        if (maxGuessesNumber - guessesTaken) > 0:
            print(
                'Podana liczba jest za mała. Zostało Ci już tylko: ' + str(maxGuessesNumber - guessesTaken) + ' prób!')
        else:
            print('Podana liczba jest za mała. Nie masz już więcej prób. Sorki.')
    elif getGuess > mySecretNumber:
        if (maxGuessesNumber - guessesTaken) > 0:
            print(
                'Podana liczba jest za duża. Zostało Ci już tylko: ' + str(maxGuessesNumber - guessesTaken) + ' prób!')
        else:
            print('Podana liczba jest za duża. Nie masz już więcej prób. Sorki.')
    else:
        break  # wyjście z pętli jeśli odgadnięto

if getGuess == mySecretNumber:
    print('Doskonale! Odgadłeś liczbę w ciągu ' + str(guessesTaken) + ' prób!')
else:
    print('Nie udało się. Liczba, którą miałem na myśli to ' + str(mySecretNumber))

outro()

