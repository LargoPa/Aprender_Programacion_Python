
lista = list(["Hola","Rodrigo",35,45,True])

#agrega uno al final de la lista
lista.append("JAJAJA")

#agrega uno en donde especifiquemos
lista.insert(2,"Chupala")

#agrega varios al final de la lista
lista.extend([False,20230])

#eliminando un elemento de la lista por su indice
#-1 para eliminar el ultimo, el -2 el anteultimo y asi
lista.pop(3)

#removiendo un elemento por su valor
lista.remove("Chupala")

#eliminando todos los elementos de la lista
#lista.clear()

lista2= list([242,421,4,1241,5,9,True,False,True])

#ordenando la lista de forma ascendente
#si se usa .sort(reverse=true) lo ordena de forma descendente 
lista2.sort()

#invitiendo los elementos de una lista 
#(sirve para cualquier lista sea ordenada o no)
lista2.reverse


print(lista2)