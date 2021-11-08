# program z importowaniem fukci z innych bibliotek - takich jak math czy random

import random, sys, os, math  # importujemy 4 biblioteki dodatkowe

# można importować w formacie from random import *. i wówczas nie używa się nazwy biblioteki przy wywołaniu, ale zmniejsza to czytelność

print('--- Losowe liczby --')

for i in range(5):
    print(random.randint(1, 10))


# -------jedziemy dalej z funkcją

###########################################################
# Funkcja author() - Ma za zadanie wyświetlić dane autora #
###########################################################
def author():
    print('----------------------------')
    print('-  Program KOSTKA FORTUNY  -')
    print('----------------------------')
    print('-    by Alien Software     -')
    print('----------------------------')
    print('-      Copyright 2021      -')
    print('----------------------------')
    print()
    print()


###########################################################
# koniec funkcji author() #################################
###########################################################

###########################################################
# Funkcja genAnswer() - ma za zadanie wyświetlić ##########
# interprentacje dla podanego numeru na kostce ############
###########################################################
def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'To pewne!'
    elif answerNumber == 2:
        return 'Zdecydowanie tak!'
    elif answerNumber == 3:
        return 'Tak'
    elif answerNumber == 4:
        return 'Spróbuj ponownie'
    elif answerNumber == 5:
        return 'Nie'
    elif answerNumber == 6:
        return 'To zależy'
        # zamiast return mógłbyś zaktualizować zmienną globalną np. global Odpowiedz = 'To zależy'


###########################################################
# koniec funkcji getAnswer() ##############################
###########################################################

###########################################################
# Funkcja 'Podaj liczbę z kostki' #########################
###########################################################
def whatNumberOnDice():
    print('Pomyśl pytanie jakie chcesz zadać.')
    print('Rzuć kostką i wpisz jaka liczba wypadła na kostce?')
    print('Jeśli nie masz już pytań to napisz 0, żeby zakończyć program!')
    myDice = input()

    try:
        myDice = int(myDice)
    except ValueError:
        print('Błąd - nie podałeś liczby - ValueError. Zegnaj kolego! Do następnego razu!')
        sys.exit()
    except TypeError:
        print('Błąd - nie podałeś liczby - TypeError. Zegnaj kolego! Do następnego razu!')
        sys.exit()

    if myDice == 0:
        print('Żegnaj kolego! Do następnego razu!')
        sys.exit()

    if myDice < 1:
        print('Za mała liczba. Z niej nic nie wywróżymy. Kończymy program!')
        sys.exit()
    elif myDice > 6:
        print('Za duża liczba. Z niej nic nie wywróżymy. Kończymy program!')
        sys.exit()
    else:
        print('Liczba poprawna. Zobaczmy co kula odpowie!')
        return myDice


###########################################################
# koniec funkcji WhatNumerbOnDice() #######################
###########################################################

# r = random.randint(1,6) - losowało wartość kostki - zamieniłem na podawanie przez kogoś wartości, zeby potrenować

###########################################################
# Program właściwy ########################################
###########################################################

author()  # Wywołanie stopki

while True:
    fortune = getAnswer(whatNumberOnDice())
    print('Kostka przyszłości daje ci odpowiedź: ')
    print('     => ' + fortune)
    print('No to kolejne pytanie i kolejny rzut kostką!')
    print()

# do przechwytywania wyjątków try oraz except


# KONIEC PROGRAMU -- THIS IS THE END --
