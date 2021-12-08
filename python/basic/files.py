from pathlib import Path
import shelve
#p = Path('spam.txt')
#p.write_text('Hello, world!')
#p.read_text()
#helloFile = open(Path.home() / 'hello.txt')
#print(helloFile.read())
#helloFile.readlines()

baconFile = open('bacon.txt', 'w')   
baconFile.write('Hello, world!\n')
baconFile.close()

baconFile = open('bacon.txt', 'a')
baconFile.write('''Bacon is not a vegetable.
Bla bla bla
Plop''')
baconFile.close()

baconFile = open('bacon.txt')
content = baconFile.read()
baconFile.close()
print(content)


shelfFile = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()

shelfFile = shelve.open('mydata')
type(shelfFile)
print(shelfFile['cats'])
print(list(shelfFile.keys()))
print(list(shelfFile.values()))
shelfFile.close()