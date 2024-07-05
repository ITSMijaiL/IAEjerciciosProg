
#5.- Mergesort.
#* Entrada: una lista de números A, rangos de ordenamiento (lo, hi)
#* Salida: una nueva lista A’ ordenada.

def merge(left: list, right: list):
    #Aqui uso pop() para emular la pseudo-funcion "rest" del algoritmo, 
    #que significa que es el resto de la lista
    #Lo que se hace es extraer el primer item de la lista y 
    #shiftear o añadir el resto de los items de esta lista a ella misma
    #Por eso, lo equivalente en python seria pop()
    res = []
    while len(left)!=0 and len(right)!=0:
        if left[0] <= right[0]:
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))
    while len(left)!=0:
        res.append(left.pop(0))
    while len(right)!=0:
        res.append(right.pop(0))
    return res

def mergeSort(A: list, rango: str = "lo"):
    if len(A)<=1: return A
    left = []
    right = []
    for i in range(len(A)):
        x = A[i]
        if i < (len(A)/2):
            left.append(x)
        else:
            right.append(x)
    left = mergeSort(left)
    right = mergeSort(right)
    r = merge(left, right)
    if rango=="lo":
        return r
    elif rango=="hi":
        r.reverse()
        return r

import random
def generar_lista(tamano: int, maximo_int: int):
    res = []
    for i in range(tamano):
        res.append(random.randrange(maximo_int))
    return res

#mayor a menor
print(mergeSort(generar_lista(10, 50), "hi"))
print()
#menor a mayor
print(mergeSort(generar_lista(10, 50), "lo"))
