import pyinputplus as pyip
response = pyip.inputInt(prompt='Enter a number: ')
response = pyip.inputNum('>', min=4, lessThan=6)
response = pyip.inputNum('Enter num: ', greaterThan=4)
response = pyip.inputNum('Enter num: ', min=4)
response = pyip.inputNum(blank=True)
response = pyip.inputNum(timeout=10)
response = pyip.inputNum(limit=2, default='N/A')
response = pyip.inputNum(allowRegexes=[r'(I|V|X|L|C|D|M)+', r'zero'])
response = pyip.inputStr(allowRegexes=[r'caterpillar', 'category'], blockRegexes=[r'cat'])