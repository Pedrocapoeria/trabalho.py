lista = [7, 5, 1, 8, 3]
n = len(lista)
minimo = lista[0]
for i in range(n):
    if lista[i] < minimo:
        minimo = lista[i]
    print(minimo)

    lista = [7, 5, 1, 8, 3]

    def selection_sort(lista):
        n = len(lista)
        for i in range(n-1):
            min_index = i
            for j in range(i + 1, n):
                if lista[j] < lista[min_index]:
                    min_index = j
            lista[i], lista[min_index] = lista[min_index], lista[i]
        return lista
    
    sorted_list = selection_sort(lista)
    print(sorted_list)