#import sys
#import os
#import math
import random
#the funcion above coul be replaced with: 	from random import *
#its funcitons would be like: randomint(x,y), instead or random.randint(x,y)
def rand(lower,upper):
	print('You are generationg a random number between: '+ str(lower) + " and " + str(upper))
	print('The random number generated is: '+ str(random.randint(lower,upper)))
	
def main():
	print('Insert the lower boundary: ')
	lower = int(input())
	print('Insert the upper boundary: ')
	upper = int(input())
	rand(lower,upper)	
	
main()
