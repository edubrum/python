import copy

def inserting(var):
    var.append('Added data')

def main():
    print('Treating variables as pointers:')
    var = [ 'Tennis',
            'Baseball',
            'Basketball']
    print('Var is'+ str(var))
    iant = var
    inserting(var)
    print('Iant after iserting on var: ' + str(iant))

    print('Not treating variables as pointer anymore:')
    iant = copy.deepcopy(var)
    print('Inserting new value on var')
    inserting(var)
    print('Content of var: ' + str(var) + \
            '\nContent of iant' + str(iant))

main()
