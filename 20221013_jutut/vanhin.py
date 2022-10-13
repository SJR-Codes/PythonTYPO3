def vanhin(lista: list) -> str:
    '''Find oldest person on tuples-list and return their name'''

    #change tuples list to dictionary
    new = {lista[i][0]: lista[i][1] for i in range(len(lista))}    
    #print(new)
    return min(new, key=new.get)

h1 = ("Arto", 1977)
h2 = ("Einari", 1985)
h3 = ("Maija", 1953)
h4 = ("Essi", 1997)
hlista = [h1, h2, h3, h4]

print("Vanhin henkilö: ", vanhin(hlista))
#vanhin(hlista)