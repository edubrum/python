#List introduction classs

def indexing():
    animal = ['monkey','dog','bird','dragon']
    for i in range(-1*len(animal),len(animal)):
        print('The string animal position ['+ str(i) + '] contains: ' + animal[i])
    print('Checking if monkey is an existing animal: ' + str('monkey' in animal))
    print('Checking if panda is an existing animal: ' + str('panda' in animal))

def listOfList():
    pokemon = [ ['Groudon','Rayquaza'], ['Kyogre','Rayquaza'], ['Groudon','Kyogre','Rayquaza']]
    for i in range(0,len(pokemon)):
        for j in range(len(pokemon[i])):
            print('The Pokemon[' + str(i) + ']['+ str(j) + '] is: ' + pokemon[i][j])

def slices():
    animal = ['monkey','dog','bird','dragon']
    print('Using slices of Animal array[1:3] = '+ str(animal[1:3]))
    print('Using slices of Animal array[-2:2] = '+ str(animal[-2:2]))
    del animal[1]
    print('Animal position [1] got deleted: ' + str(animal))

def listing():
    counter = list(range(100))
    print('Counter is: ' + str(counter))
    print('Position 6 of counter: '+ str(counter[5]))
    counter2 = list(range(0,100,4))
    print('Counter using step = 4 : ' + str(counter2))

def multipleAssignments():
    garfield = ['cat', 'orange', 'fat']
    species,color,weight = garfield
    print('Garfield is: ' + str(garfield))
    print('Species is:' + str(species))
    print('Color is:' + str(color))
    print('Weight is:' + str(weight))

def switchingValues():
    a = 'Apple'
    b = 'Banana'
    print('Before swtching /// A: ' + str(a) + ' B: ' + str(b))
    a,b = b,a
    print('After swtching /// A: ' + str(a) + ' B: ' + str(b))

def main():
    indexing()
    listOfList()
    slices()
    listing()
    multipleAssignments()
    switchingValues()

main()
