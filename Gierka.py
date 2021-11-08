# To prosty programik przeniesiony z IDLE
# Prosty program powitalny - proszący o imie i wiek oraz wyświetlający coś tam
# inicjowanie zmiennych
import sys

myName = ''
myage = 0

print('Cześć!')
while not myName:  # Pętla wymusza podanie jakiegoś imienia
    print('Jak masz na imię?')  # Prośba o podanie imienia
    myName = input()

if myName == 'exit':  # jeśli podałeś jako imię exit to nastąpi przerwanie programu
    print('No to kończymy')
    sys.exit()

if myName == 'Irek':
    print('Czołem szefie!')
else:
    print('Miło Cię poznać, ' + myName + '!')

if len(myName) == 1:
    print('Twoje imię ma ' + str(len(myName)) + ' znak!')
else:
    print('Twoje imię ma ' + str(len(myName)) + ' znaków!')

print('Ile masz lat?')
myAge = input()
# tutaj można zastosować od razu konwersję na liczbę myAge = int(input())
# tyle, że trzeba by wiedzieć jak dodać obsługę błędów, żeby nie wywalało programu


if myName == 'Irek':
    print('=/=')
elif int(myAge) > 10000:  # Warunek uruchamiany tylko jeśli nie jesteś Irkiem
    print('Stary jak świat')
elif int(myAge) > 1000:  # Warunek uruchamiany tylko jeśli nie jesteś Irkiem
    print('To wampir!')
elif int(myAge) == 47:  # Warunek uruchamiany tylko jeśli nie jesteś Irkiem
    print('Masz tyle lat co Irek!')
# na końcu może być jeszcze dodatkowy else

if myName == 'Irek' and int(myAge) == 47:
    print('Prawdziwy Irek!')

if int(myAge) >= 100:
    print('Serio? Coś ściemniasz')
else:
    print('To za rok będziesz mieć ' + str(int(myAge) + 1) + ' lat.')

# Nowa czesc - z petlą WHILE
print()
print('==================')
print()
petelka = 1

while petelka <= 5:
    print('Za ' + str(petelka) + ' lat bedziesz miał lat: ' + str(int(myAge) + petelka))
    petelka = petelka + 1

# Nowa czesc - z petlą bardziej rzobudowaną
print()
print('====== Rozbudowana WHILE ============')
print()
petelka = 1

while petelka <= 5:
    if petelka == 1:
        print('Za ' + str(petelka) + ' rok bedziesz miał lat: ' + str(int(myAge) + petelka))
    elif petelka == 2:
        print('Za ' + str(petelka) + ' lata bedziesz miał lat: ' + str(int(myAge) + petelka))
    elif petelka == 3:
        print('Za ' + str(petelka) + ' lata bedziesz miał lat: ' + str(int(myAge) + petelka))
    elif petelka == 4:
        print('Za ' + str(petelka) + ' lata bedziesz miał lat: ' + str(int(myAge) + petelka))
    else:
        print('Za ' + str(petelka) + ' lat bedziesz miał lat: ' + str(int(myAge) + petelka))
    petelka = petelka + 1

# I leciki z pętką for
print()
print('====== Petelka FOR ============')
print()
for i in range(4):
    print('Przejście pętli numer: ' + str(i) + ' !')
    print('----')
print('I na tym koniec')

# sumowanie wszystkich liczb
total = 0
for num in range(101):  # liczymy do 100
    total = total + num
    # print(total) - kontrolne wyświetlanie przebiegu pętlki for
print(total)

# for z więcej prarametrami range

print()
print('====== Petelka FOR ============')
print()
for z in range(0, 10, 2):
    print(z)

print()
print('====== Petelka FOR ============')
print()
for z in range(10, 0, -1):
    print(z)

