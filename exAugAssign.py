import math



def isDiv(num):
    print('Insert the power of 2 which will divide the number: ')
    div = input()
    print('The Binary division of: ' + num + ' by ' + div + ' is' + str(binDiv(num,div)) )

def binDiv(num, div):
    return num >>= math.log2(div)

menu={
    '*': isMult(),
    '/':'isDiv()',
    2:'Tuesday',
    3:'Wednesday',
            4:'Thursday',
            5:'Friday',
            6:'Saturday'
            }

def main():
    print('This is the binary calculator')
    primt('Insert the numerator: ')
    num = input()
    print('Chose the operation you want to permort with: ' num)
    print('*\t/\t%\t&\t|')

    isDiv(num)



main()
