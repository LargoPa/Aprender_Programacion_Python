
def sumar_dos():
    while True:
        a=input("Numero 1: ")
        b=input("Numero 2: ")
        try:
            return int(a)+int(b)
        except:
            print("Salame, te pedi 2 numeros.")

print(sumar_dos())
