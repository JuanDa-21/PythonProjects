numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Definimos la función
def clasificar_numeros(lista_de_numeros):
    # Creamos las listas vacías DENTRO de la función
    pares = []
    impares = []

    # Usamos un bucle 'for' para recorrer CADA número de la lista
    for numero in lista_de_numeros:
        # Usamos el operador módulo (%) para saber si el número es par
        if numero % 2 == 0:
            # Si el residuo es 0, es par. Lo añadimos a la lista 'pares'
            pares.append(numero)
        else:
            # Si no, es impar. Lo añadimos a la lista 'impares'
            impares.append(numero)

    # Devolvemos una lista que contiene ambas listas
    return [pares, impares]
