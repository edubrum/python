import random




def getResponse(dumb):
	while dumb == True:
			try:
				guess = int(input())
				dumb = False
				return guess
			except ValueError:
				print('Enter a number, you idiot!')
			
				
def main():
	dumb = True
	goodGuess = False
	print("The Guessing Game")
	print('You have 5 attempts do guess the number I am thinking!')
	number = random.randint(1,10)
	for i in range(6):
		print('Attempt: '+ str(i+1)  +'. Say your guess: ')
		while goodGuess == False:
			guess = getResponse(dumb)
			if (guess <= 10) and (guess >= 1):
				goodGuess = True
				if guess == number:
					print('You did it!!! Congratutlation!!')
					break
			else:
				print('Enter a valid number you idiot!')
				goodGuess = False
	print('You have used all your attempts, try again.')
	
main()

