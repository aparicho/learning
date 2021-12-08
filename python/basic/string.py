name = 'Al'
age = 4000

print(r'That is Carol\'s cat.')
print('''Dear Alice,

Eve's cat has been arrested for catnapping, cat burglary, and extortion.

Sincerely,
Bob''')
print('Dear Alice,\n\nEve\'s cat has been arrested for catnapping, cat burglary, and extortion.\n\nSincerely,\nBob')
print('My name is %s. I am %s years old.' % (name, age))
print(f'My name is {name}. Next year I will be {age + 1}.')

print('How are you?')
feeling = input()
if feeling.lower() == 'great':
    print('I feel great too.')
else:
    print('I hope the rest of your day is good.')