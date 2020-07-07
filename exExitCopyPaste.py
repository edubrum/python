import sys
import pyperclip

def main():
	name = 'Eduardo'
	print('Hello')
	pyperclip.copy('Hello'+ name)
	var = pyperclip.paste()
	print("The text copyed from terminal is: "+ var)

	print('This text should be', end='')
	print(' in differnt lines!')
	print('Previously'+'wasan\'t'+'blank-spaces'+'here')
	print('Now-it'+'has','blank-spaces','here',sep=' ')
	sys.exit()
	#the print bellow will never hapen because sys.exit() terminated the program
	print('Goodbye')
	
main()
