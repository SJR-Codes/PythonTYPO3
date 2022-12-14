def tupleFind(a: tuple):
    '''Small helper function to sort list with tuples second var'''
    return a[1]

def vanhin(lista: list) -> str:
    '''Find oldest person on tuples-list and return their name'''

    #change tuples list to dictionary
    #new = {lista[i][0]: lista[i][1] for i in range(len(lista))}    
    #print(new)
    #return min(new, key=new.get)

    #using lambda
    #new = min(lista, key=lambda x: x[1])
    #return(new[0])

    #using own func
    new = min(lista, key=tupleFind)
    return(new[0])

def vanhemmat(lista:list, year:int) -> list:
    '''Returns list of people who are older than given year'''
    new = [i[0] for i in lista if tupleFind(i) < year]
    #print(new)
    return(new)



h1 = ("Arto", 1977)
h2 = ("Einari", 1985)
h3 = ("Maija", 1953)
h4 = ("Essi", 1997)
hlista = [h1, h2, h3, h4]

print("Vanhin henkilö: ", vanhin(hlista))
#vanhin(hlista)

vanhemmat_henkilot = vanhemmat(hlista, 1979)
print("Vanhemmat henkilöt:", vanhemmat_henkilot)