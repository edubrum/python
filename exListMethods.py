def showAfter(kantoStarters):
    print('The Kanto Starter Pokemons are: ', end = '')
    for i in range(len(kantoStarters)):
        if i == len(kantoStarters) - 1:
            print(kantoStarters[i])
        else:
            print(kantoStarters[i]+ ' ', end='')
def showNum(mess):
    for i in range(len(mess)):
        if i == len(mess) - 1:
            print(str(mess[i]))
        else:
            print(str(mess[i])+ ' ', end='')

def indexFunc():
    kantoStarters = ['bulbasaur','charmander','squirtle']
    for i in range(len(kantoStarters)):
        print('The  index from starters are: ' + str(kantoStarters.index(kantoStarters[i])))

def appendFunc():
    kantoStarters = ['bulbasaur','charmander']
    print('Uncomplete list of starters are: ', end = '')
    for i in range(len(kantoStarters)):
        print(kantoStarters[i]+ ' ', end='')
    kantoStarters.append('squirtle')
    print('\nSquirtle was appended')
    showAfter(kantoStarters)

def appendAll():
    kantoStarters = []
    print('Kantostarters are an empty list now: ')
    print(str(kantoStarters))
    print('Inserting all starters on a previously NULL list')
    kantoStarters.append('bulbasaur')
    kantoStarters.append('charmander')
    kantoStarters.append('squirtle')
    print('Printing all inserted pokemons:')
    showAfter(kantoStarters)


def insertFunc():
    kantoStarters = ['charmander','squirtle']
    print('Uncomplete list of starters: ', end='')
    for i in range(len(kantoStarters)):
        print(kantoStarters[i]+ ' ', end='')
    kantoStarters.insert(0,'bulbasaur')
    print('\nBulbasaur was inserted at: '+ str(0))
    showAfter(kantoStarters)

def removeFunc():
    kantoStarters = ['bulbasaur','charmander','squirtle','mew']
    print('This are list KAnto Starters before removing: ')
    showAfter(kantoStarters)
    kantoStarters.remove('mew')
    print('This are the KAnto starters after removind Mew')
    showAfter(kantoStarters)

def sortFunc():
    mess = [1,-4,7,2,-23,5,9,4,-6]
    print('This are the numbers before being sorted: ', end='')
    showNum(mess)
    mess.sort()
    print('This are the numbers after being sorted: ', end='')
    showNum(mess)
    messNames = ['eduardo', 'joanna', 'ana', 'jessica','angela']
    print('This are the Names before being sorted: ', end='')
    showNum(messNames)
    messNames.sort()
    print('This are the Names after being sorted: ', end='')
    showNum(messNames)
    messNames.sort(reverse=True)
    print('This are the Names after being sorted in a downscale: ', end='')
    showNum(messNames)

def sortLetters():
    mess = ['A','z','b','a','B','Z']
    print('This are the letters before being sorted: ', end='')
    showNum(mess)
    mess.sort(key=str.lower)
    print('This are the letters after being sorted: ', end='')
    showNum(mess)

def main():
    indexFunc()
    appendFunc()
    insertFunc()
    appendAll()
    removeFunc()
    sortFunc()
    sortLetters()

main()
