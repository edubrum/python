#Dictionaries constains keys associated with values

import pprint

daysOfTheWeek = {'0':'Sunday',
                '1':'Monday',
                '2':'Tuesday',
                '3':'Wednesday',
                '4':'Thursday',
                '5':'Friday',
                '6':'Saturday'}

daysOfTheWeekInv = {'6':'Saturday',
                '5':'Friday',
                '4':'Thursday',
                '3':'Wednesday',
                '2':'Tuesday',
                '1':'Monday',
                '0':'Sunday'}

msg = 'O peito do pé do Pedro é preto'

lorem = '''Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum

Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32 '''

def keys(var):
        for i in range(len(var)):
            print('daysOfTheWeek['+ str(i) +'] Key is: ' + str(i) +' Value is: ' + var[str(i)])

def listing():
    print('Listing the keys:' + str(list(daysOfTheWeek.keys())) + \
        '\nListing the values:' + str(list(daysOfTheWeek.values())) + \
        '\nListing the items:' + str(list(daysOfTheWeek.items())))

def printingValuesByKey():
    for i in daysOfTheWeek.values():
        print(i)

def printingValueAndTheKey():
    for key,value in daysOfTheWeek.items():
        print(key,value)

def printingItems():
    for i in daysOfTheWeek.items():
        print(i)

def getAccess():
    for i in range(len(daysOfTheWeek)):
        print('Using get to return a value: ' + daysOfTheWeek.get(str(i),0))

def addingKeyValues():
    daysOfTheWeek.setdefault('7','Dreamday')
    printingValueAndTheKey()

def countingCharacters(message):
    #This function creates a dictionary of characters

    count = {}
    for character in message.lower():
        count.setdefault(character,0)
        count[character] = count[character] + 1
    print('Printing normally')
    print(count)
    print('Printng in a fancy layout')
    pprint.pprint(count)
    charVarCount = pprint.pformat(count)
    print(charVarCount)

def main():
    keys(daysOfTheWeek)
    keys(daysOfTheWeekInv)
    if daysOfTheWeek == daysOfTheWeekInv:
        print('Both Dictionaries have same keys in differrent orders' )
    listing()
    printingValuesByKey()
    printingValueAndTheKey()
    printingItems()
    getAccess()
    addingKeyValues()
    print('Small string:')
    countingCharacters(msg)
    print('Big string')
    countingCharacters(lorem)

main()
