import sys
def collatz(number):
	if number % 2 == 0:
		number //= 2
	elif number % 2 == 1:
		number = 3 * number + 1
		
	print (str(number))
	return number

print ('Please enter an integer')
try:
        number = int(input())
except:
        print ('Value must be an integer')
        sys.exit()
while True:
        number = collatz(number)
        if number == 1:
                break
        else:
                continue
    
		
