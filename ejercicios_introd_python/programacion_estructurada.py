#2.- Diseñe una solución que determine si una cadena de paréntesis, llaves y
#corchetes es válida. Ejemplo:
#Entrada: (){[]()}
#Salida: Válido

stack = []
parentesis_abrir = "(,{,[".split(",")
parentesis_cerrar = "),},]".split(",")

#ventaja de experimentar haciendo tu propio parser para tu lenguaje de programacion xD
def interpretarParentesis(entrada: str):
    for c in entrada:
        if c in parentesis_abrir:
            stack.append(parentesis_abrir.index(c))
        elif c in parentesis_cerrar and parentesis_cerrar.index(c) in stack:
            stack.pop()
        else:
            return "Invalido"
    if len(stack)!=0:
        return "Invalido"
    return "Valido"

res = interpretarParentesis(input("Entrada: "))
print(res)
