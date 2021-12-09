# Materialy ze szkolenia live dot. ML, analizy plików i procesu
# ocena sentymentu komentarzy na bazie 25 tys plików
# dane trzeba wyczyścić - np. pozbuć się niepotrzebnych znaków

# wczytanie danych
# wcześniej wczytanie wszystkich plików

import glob

pos_files = glob.glob('data/alImdb/train/pos/*.txt')  # znajduje wszystkie pliki w katalogu i o wzorcu
# print(pos_files)  # wyświetli bardzo dużo nazw plików - z pozytywnymi komentarzami
words_count_pos = {}  # slowo -> liczba pozytywnych opinii z tym slowem

for file in pos_files:  # dla każdego pliku pos_files[:1] - tylko 1 plik wowczas
    with open(file) as stream:
        content = stream.read()  # odczytuje tresc pliku
    words = content.lower().replace('<br />', ' ').split()  # czyszczenie danych oraz dzielenei na slowa (split dzielone spacjami - domyslne)
    # print(words)
    for word in set(words):  # set to zbiór z danymi bez powtórzeń, bo chcemy liczyć tylko w ilu ocenach wystąpiło
        words_count_pos[word] = words_count_pos.get(word, 0) + 1

# print(words_count_pos)
#for word, counter in words_count_pos.items()
#    print(word, '->', counter)

# to samo dla negatywnych

neg_files = glob.glob('data/alImdb/train/neg/*.txt')  # znajduje wszystkie pliki w katalogu i o wzorcu
# print(pos_files)  # wyświetli bardzo dużo nazw plików - z negatywnymi komentarzami
words_count_neg = {}  # slowo -> liczba negatywnych opinii z tym slowem

for file in neg_files:  # dla każdego pliku neg_files[:1] - tylko 1 plik wowczas
    with open(file) as stream:
        content = stream.read()  # odczytuje tresc pliku
    words = content.lower().replace('<br />', ' ').split()  # czyszczenie danych oraz dzielenei na slowa (split dzielone spacjami - domyslne)
    # print(words)
    for word in set(words):  # set to zbiór z danymi bez powtórzeń, bo chcemy liczyć tylko w ilu ocenach wystąpiło
        words_count_neg[word] = words_count_neg.get(word, 0) + 1

# wyliczanie sentymentu nowego zdania - podanego przez usera
sentence = input("podaj komentarz do oceny sentymentu: ")
words = sentence.lower().replace('<br />', ' ').split()
sentence_sentiment = 0.0
# sentyment slowa - ile jest pozytywnych opinii z tym slowem, i ile jest negatywnych opinii z tym slowem
for word in words:
    # print(word)
    #positive = words_count_pos[word] # jesli slowa nie będzie, to program wyswietli błąd trzeba to obejsc
    positive = words_count_pos.get(word, 0)
    negative = words_count_neg.get(word, 0)

    # sentyment słowa w zakresie od -1.0 do + 1.0
    # 50 poz i 50 negatyw -> sentyment 0.0
    # 100 poz i 0 negatyw -> sentyment 1.0

    all_ = positive + negative
    if all_ == 0:
        sentiment = 0.0
    else:
        sentiment = (positive - negative) / all_

    sentence_sentiment += sentiment
    print(word, sentiment)

sentence_sentiment /= len(words)

if sentence_sentiment > 0:
    label = 'positive'
else:
    label = 'negative'
print('this sentence is ' + label + '. sentiment: ' + sentence_sentiment)



# sentyment zdanai to srednia arytmentyczna sentymentu wszystkich slow




