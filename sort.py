lista = [3, 4, 1, 8, 5, 10, 15]
def bubble_sort(lista):
    n = len (lista)
    for j in range(n-1):
        for i in range(n-1):
            if lista [i] > lista [i+1]:
            #troca acontece
                lista [i], lista [i+1] = lista [i+1], lista[i]
    return lista
#este código está completo
mostrar_lista = bubble_sort(lista) 
print(mostrar_lista)