#One of my fisrt attempts to learn python

# Contents aproached on this file:
#	1. variable types
#	2. casting variables
#	3. function delcaration and call
#	4. little about boolean operators	

def checkIsEdu(myName):
	if (myName == 'Edu') or (myName == 'edu') or (myName == 'eduardo') or (myName == 'Eduardo' ):
		print('You really are the Sys Admin here!')
	else:
		print('You shouldn\'t be here')
		
def checkAge(myAge):
	if myAge >= 21:
		print('You are not lying!')
	elif (myAge >= 18) and (myAge < 21):
		print("You are a lyar but stll can drive!")
	else:
		print('Why are you here?') 

def main():
	print('Hello Word')
	print('What is your name?')
	myName = input()
	print('Welcome, '+ myName + '!'*int(len(myName)))
	checkIsEdu(myName)
	print('Your name have: ' + str(len(myName)) + ' letters!')
	print('What is your age?')
	myAge = input()
	checkAge(int(myAge))
	print('You will be ' + str(int(myAge) + 1) + ' next year!')
	bolsomitoIsGoodPresident = False
	edLeiteIsGoodGovernor = True
	print('Bolsonaro is a good president? ' + str(bolsomitoIsGoodPresident) + '.')
	print('Ed Leite is a good governor? ' + str(edLeiteIsGoodGovernor) + '.')
	print('Bolsonaro is a bad president? ' + str( not bolsomitoIsGoodPresident) + '.')
	print('Ed Leite is a bad governor? ' + str(not edLeiteIsGoodGovernor) + '.')
	
main()
