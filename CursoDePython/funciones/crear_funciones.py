
#creando una funcion simple
#def saludar():
#    print("Hola lucas, mi nombre es Rodrigo")    
#saludar()


#creando una funcion con parametros
#def saludar(nombre,sexo):
#    sexo = sexo.lower()
#    if(sexo=="mujer"):
#        adjetivo="reina"
#    elif(sexo=="hombre"):
#        adjetivo="rey"
#    else:
#        adjetivo="amor"
#    print(f"Hola {nombre} como estas {adjetivo}?")    
#saludar("Rodrigo","")


def crear_contrasenia_random(num):
    chars = "abcdefghij"
    #obtengo el primer numero de (num) y lo convierto en entero
    num=int((str(num))[0])
    c1=num-2
    c2=num
    c3=num-5
    contrasenia = (f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}")
    return contrasenia
    
password = crear_contrasenia_random(254)
print(password)



