#!/bin/python

import math
import os
import random
import re
import sys


print("Hello")
x = 1
if x == 1:
	#indented four spaces
	print("x is 1")

__name__ == "__main__"	
if __name__ == '__main__':
    print("Name is:" + __name__)

def perm(l):
        # Compute the list of all permutations of l
    if len(l) <= 1:
                  return [l]
    r = []
    for i in range(len(l)):
             s = l[:i] + l[i+1:]
             p = perm(s)
             for x in p:
              r.append(l[i:i+1] + x)
    return r
l = [1,2,3,4]
print(perm(l))
    

