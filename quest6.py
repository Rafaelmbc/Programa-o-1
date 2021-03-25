nome="Rafael"

def lista(nome):
    dic = {x : [x for x in range(7) ] for x in nome}   
    print(dic) 
lista(nome)    
def dicionario(nome):
    dic = {x : [x for x in range(10) if x %2 == 0 ] for x in nome}
    print(dic)

dicionario(nome)  