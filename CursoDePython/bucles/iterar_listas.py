
animales=["gato","perro","loro","cocodrilo","pez"]
numeros = [52,16,14,72]

#for animal in animales:
#    print(f"Ahora la variable animal es igual a: {animal}")


#for numero,animal in zip(animales,numeros):
#    print(f"Recorriendo lista 1: {numero}")
#    print(f"Recorriendo la lista 2: {animal}")
    

#forma NO optima     
#for num in range(len(numeros)):
#   print(num)


#forma Optima
for num in enumerate(numeros):
    print(num[1])