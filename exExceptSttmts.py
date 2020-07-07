
def div42by(divide42by):
	try:
		return 42 / divide42by
	except ZeroDivisionError:
		print('You tried to divide by zero...')
		
def numCats():
	print('HOw many cats do you have?')
	try:
		numberCats = int(input())
		if numberCats >= 4 :
			print('Are you a old crazy witch?')
		else:
			print('That is not that many cats.')
	except ValueError:
		print('Enter a fucking NUMBER, you idiot' + '!'*5)
	
def main():
	print(div42by(2))
	print(div42by(12))	
	print(div42by(0))	
	print(div42by(1))	
	numCats()
main()
