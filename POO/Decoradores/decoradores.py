
def decorador(funcion):
    def funcion_modificada():
        print("Antes de llamar a la funcion")
        funcion()
        print("Despues de llamar a la funcion")
    return funcion_modificada

#def saludo():
#    print("Hola washo")
#saludo_modificado = decorador(saludo)
#saludo_modificado()

@decorador
def saludo():
    print("hola pa")
    
saludo()



