import numpy as np

#start variables
a = b = xSquare = tSquare = xt = xy = ty = 0.0000
x = y = t = []

#prepare matrix coeficients
def sum():
    for i in range(len(y)):
        xSquare += (x[i])²
        tSquare += (t[i])²
        xt = x[i]*t[i]
        xy = x[i]*y[i]
        ty = t[i]*y[i]

def calc():
    denominator = np.array([xSquare, xt],[xt, tSquare])#creates left matrix
    denomiator = np.linalg.inv(denominator)#make inverse matrix
    res = np.dot(denominator,([xy],[ty]))#multiply the matrices
    a = res[0]
    b = res[1]

def plot():

def main():
    sum()
    calc()

main()
