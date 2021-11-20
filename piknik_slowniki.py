# Program with dictionaries in dictionaries

allGuests = {'Alicja': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Karol': {'cups': 3, 'apple pies': 1, 'apples': 5}
             }


def total_brought(guests, item):
    num_brought = 0
    for k, v in guests.items():
        num_brought = num_brought + v.get(item, 0)
    return num_brought


print('Liczba przyniesionych produktów:')
print('- jabłka: ' + str(total_brought(allGuests, 'apples')))
print('- kubki: ' + str(total_brought(allGuests, 'cups')))
print('- ciastka: ' + str(total_brought(allGuests, 'cakes')))
print('- kanapki z szynką: ' + str(total_brought(allGuests, 'ham sandwiches')))
print('- jabłecznik: ' + str(total_brought(allGuests, 'apple pies')))


# zadanie dodatkowe:


def display_inventory(inventory):
    print('')
    print('Inwentarz: ')
    item_total = 0
    for k, v in inventory.items():
        print('     - ' + str(v) + ' ' + k)
        item_total = item_total + v
    print('Calkowita liczba przedmiotów: ' + str(item_total))


all_items = {'lina': 1, 'pochodnia': 6, 'złote monety': 42, 'sztylet': 1, 'strzała': 12}

display_inventory(all_items)

# zadanie dodatkowe 2:


def add_to_inventory(inventory, added_items):
    print('')
    print('Smok miał: ')
    for k in range(len(added_items)):  # dla każdej rzeczy z dodanwanych
        print(added_items[k])
        for klucz, wartosc in inventory.items():  # dla każdej pozycji ze słownika
            if klucz == added_items[k]:  # jeśli wartość dodawana zgadza się z wartośćię ze słownika
                wartosc = wartosc + 1  # zwiększa ilośc sztuk o 1
                inventory[klucz] = wartosc  # aktualizuje wartość słownika
        inventory.setdefault(added_items[k], 1)  # dodaje wartość do słownika jeśli wcześniej nie było
    return inventory


dragon_loot = ['złote monety', 'sztylet', 'złote monety', 'złote monety', 'rubin', 'rubin', 'sztylet', 'kość']
inv = add_to_inventory(all_items, dragon_loot)
display_inventory(inv)
