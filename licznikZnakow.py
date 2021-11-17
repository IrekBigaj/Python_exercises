# Program wykorzystujący słownik i zliczający ilośc znaków w tekście
import pprint # biblioteka ma jakos ladniej przentowac dane - do sprawdzenia

message = 'Był jasny, zimny dzień kwietniowy i zegary biły trzynastą'
count = {}

for characterCount in message:
    count.setdefault(characterCount, 0)
    count[characterCount] = count[characterCount] + 1
print(count)

print('Podaj dowolny tekst i naciśnij enter:')
message = input()
countCharacters = {}
for characterCountText in message:
    countCharacters.setdefault(characterCountText, 0)
    countCharacters[characterCountText] = countCharacters[characterCountText] + 1
print(countCharacters)
print('nowa metoda:')
pprint.pprint(countCharacters) # klucze są posortowane alfabetycznie

for m, n in countCharacters.items():
    print('Litera: ' + m + ' występuje w tekście: ' + str(n) + ' razy.')


# This function count characters in given text and print them
# Two parameters, first - given test
# Second - response language
def print_how_many_characters(text_to_check, language):
    count_characters_from_text = {}
    for characterCounting in text_to_check:
        count_characters_from_text.setdefault(characterCounting, 0)
        count_characters_from_text[characterCounting] = count_characters_from_text[characterCounting] + 1
    # print(countCharactersFromText)

    if language == 1 or language == '1':
        for key, value in count_characters_from_text.items():
            print('Litera: ' + key + ' występuje w tekście: ' + str(value) + ' razy.')
    else:
        for key, value in count_characters_from_text.items():
            print('Character: ' + key + ' exists in given test: ' + str(value) + ' times.')
# end of function


print_how_many_characters('Srututu pęczek z drutu', '')
print_how_many_characters('Pies i kot', 1)
print_how_many_characters('gżegżółka', '1')
