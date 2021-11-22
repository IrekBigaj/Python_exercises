###########################################################
# Funkcja intro() - Ma za zadanie wyświetlić formatkę     #
# startową i dane autora                                  #
###########################################################
def intro():
    print('----------------------------')
    print('|  Program przykładowy     |')
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


###################################################################
# Funkcja intro_program() - Ma za zadanie wyświetlić formatkę     #
# startową i dane autora                                          #
###################################################################
def intro_program(program_name):
    len(program_name)  # jak długa jest nazwa programu
    dlugosc = len(program_name)
    ile_znakow = dlugosc + 4 + 4
    min_ilosc_znakow = 28
    if ile_znakow < min_ilosc_znakow:
        ile_znakow = min_ilosc_znakow

    print("-"*ile_znakow)
    print("|" + " "*(ile_znakow-2) + "|")
    if dlugosc % 2 == 0 and ile_znakow <= min_ilosc_znakow:
        print("|" + " "*(int((ile_znakow-dlugosc-2)/2)) + program_name + " "*(int((ile_znakow-dlugosc-2)/2)) + "|")
        print("|" + " " * (ile_znakow - 2) + "|")
        print("|" + " " * (ile_znakow - 2) + "|")
        print("|" + " " * (int((ile_znakow - 18 - 2) / 2)) + " by Alien Software" + " " * (
            int((ile_znakow - 18 - 2) / 2)) + "|")
        print("|" + " " * (int((ile_znakow - 14 - 2) / 2)) + "Copyright 2021" + " " * (
            int((ile_znakow - 14 - 2) / 2)) + "|")
    elif dlugosc % 2 == 0 and ile_znakow > min_ilosc_znakow:
        print("|" + " "*(int((ile_znakow-dlugosc-2)/2)) + program_name + " "*(int((ile_znakow-dlugosc-2)/2)) + "|")
        print("|" + " " * (ile_znakow - 2) + "|")
        print("|" + " " * (ile_znakow - 2) + "|")
        print("|" + " " * (int((ile_znakow - 18 - 2) / 2)) + " by Alien Software" + " " * (
            int((ile_znakow - 18 - 2) / 2)) + "|")
        print("|" + " " * (int((ile_znakow - 14 - 2) / 2)) + "Copyright 2021" + " " * (
            int((ile_znakow - 14 - 2) / 2)) + "|")
    elif dlugosc % 2 != 0 and ile_znakow <= min_ilosc_znakow:
        print("|" + " "*(int((ile_znakow-dlugosc-2)/2+1)) + program_name + " "*(int((ile_znakow-dlugosc-2)/2)) + "|")
        print("|" + " " * (ile_znakow - 2) + "|")
        print("|" + " " * (ile_znakow - 2) + "|")
        print("|" + " " * (int((ile_znakow - 18 - 2) / 2)) + " by Alien Software" + " " * (
            int((ile_znakow - 18 - 2) / 2)) + "|")
        print("|" + " " * (int((ile_znakow - 14 - 2) / 2)) + "Copyright 2021" + " " * (
            int((ile_znakow - 14 - 2) / 2)) + "|")
    else:
        print("|" + " "*(int((ile_znakow-dlugosc-2)/2+1)) + program_name + " "*(int((ile_znakow-dlugosc-2-1)/2)) + "|")
        print("|" + " "*(ile_znakow-2) + "|")
        print("|" + " " * (ile_znakow - 2) + "|")
        print("|" + " " * (int((ile_znakow - 18 - 2) / 2)+1) + " by Alien Software" + " " * (
            int((ile_znakow - 18 - 2) / 2)) + "|")
        print("|" + " " * (int((ile_znakow - 14 - 2) / 2+1)) + "Copyright 2021" + " " * (
            int((ile_znakow - 14 - 2) / 2)) + "|")
    print("-"*ile_znakow)
    print("\n\n")
###########################################################
# koniec funkcji intro() #################################
###########################################################


###########################################################
# Funkcja outro() - Stopka końcowa #
###########################################################
def outro():
    print('----------------------------')
    print('|  Program przykładowy     |')
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
# TODO: @Irek - weź i zrób fajne intro i outro zamiast tego co jest

# intro_program("Żaba")
# intro_program("Żuk")
# intro_program("Żukowa żupa")
# intro_program("The Band Name Generator")
