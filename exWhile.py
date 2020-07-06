#Contents aproached on this program:
#	1.While loops 
#	2.For loops
#	3.Funtions

def whileMatrix():
	print('Define the size of the matrix you wanna build:')
	size = input()
	i = 0
	while i < int(size):
		print("* "*int(size))
		i = i + 1

def forSum():
	total = 0
	#range upper limit is the integer inside - 1
	#range lower limit is suposed to be 1
	for num in range(101):
		total = total + num
	print("The sum of 1 to 100 is: " + str(total))

def main():
	whileMatrix()
	forSum()
	
main()
