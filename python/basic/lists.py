import random
cat = ['fat', 'gray', 'loud']
size, color, disposition = cat
print (color, disposition, size)

supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
for index, item in enumerate(supplies):
    print('Index ' + str(index) + ' in supplies is: ' + item)

print(random.choice(supplies))
print(random.choice(supplies))
print(random.choice(supplies))
print(random.choice(supplies))
random.shuffle(supplies)
cat.insert(1,'Hello')
cat.append('plop')
print(cat)
