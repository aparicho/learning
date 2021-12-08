allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1, 'pretzels': 15}}

def totalBrought(guests, item):
    numBrought = 0
    for k, v in guests.items():
        numBrought = numBrought + v.get(item, 0)
    return numBrought

lista = []
print(allGuests)
print('Number of things being brought:')
for key, value in allGuests.items():
    for key2, value2 in value.items():
        if str(key2) not in lista:
            lista.append(str(key2)) 
            print(' - ' + str(key2) + '       ' + str(totalBrought(allGuests, str(key2))))