import random
numberOfStreaks = 0
coin = []
for experimentNumber in range(1000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    
    coin.append(random.randint(0, 1)) 
    # Code that checks if there is a streak of 6 heads or tails in a row.
    if experimentNumber == 0:
        consecutiveFlip = 1
    elif consecutiveFlip == 0:
        consecutiveFlip += 1
    elif coin[experimentNumber] == coin[experimentNumber - 1]:
        consecutiveFlip +=1
    else:
        consecutiveFlip = 1
    if consecutiveFlip == 6:
        numberOfStreaks += 1
        consecutiveFlip = 0

print('Chance of streak: %s%%' % (numberOfStreaks / 100))
print(numberOfStreaks)
print(coin)
