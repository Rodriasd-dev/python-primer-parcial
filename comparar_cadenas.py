def ordenar_lexicograficamente(cadena):
    #Definimos una lista
    listaLetras=[]
    #Definimos una variable en donde se va a guardar la nueva cadena
    nuevaCadena=""

    #Recorro la cadena letra por letra y las guardo en la lista
    for letra in cadena:
        listaLetras.append(letra)

    #Ordeno el array de manera ascendente
    listaLetras.sort()

    #Recorro el diccionario e itero las letras en la variable de nuevaCadena
    for i in listaLetras:
        nuevaCadena += i

    #Retorno la nueva cadena
    return nuevaCadena


def comparar_cadenas_lexicograficas(cadena1,cadena2):
    #Ordeno la primera cadena
    cadena1_ordenada = ordenar_lexicograficamente(cadena1)

    #Ordeno la segunda cadena
    cadena2_ordenada = ordenar_lexicograficamente(cadena2)

    #Si la primera cadena es menor que la segunda cadena entonces retorna -1
    if cadena1_ordenada < cadena2_ordenada:
        return -1
    
    #Si la segunda cadena es menor que la primera cadena entonces retorna 1
    if cadena2_ordenada < cadena1_ordenada:
        return 1

    #Retorno 0 ya que son iguales
    return 0

print(comparar_cadenas_lexicograficas("abc","abd"))
