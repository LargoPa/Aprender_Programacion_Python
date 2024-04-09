
#creando mi propia excepcion personalizada
class MiExcepcion(Exception):
    def __init__(self,err):
        print(f"Impresionante, cometiste el siguiente error: {err}")

#lanzando mi propia excepcion        
#raise MiExcepcion("Jajajajja")

#manejandola
try:
    raise MiExcepcion("jajajajjaa,ezzz")
except:
    print("Como vas a cometer eso washo")

        