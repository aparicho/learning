def fixList(stuff):
    sentence = ''
    for index, item in enumerate(stuff):
        if index == len(stuff)-1:
            sentence += 'and ' + item
        else:
            sentence += item + ', '
    print(sentence)

spam = ['apples', 'bananas', 'tofu', 'cats', 'zombies']
fixList(spam)

            
