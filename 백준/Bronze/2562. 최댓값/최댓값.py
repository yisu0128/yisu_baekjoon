lista = list()
for i in range(0,9):
    a = int(input())
    lista.append(a)
    
maxa = max(lista)
print(maxa)
print(lista.index(maxa)+1)
    
