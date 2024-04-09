
nombres = ["Rodrigo","Lucas","Pedro","Juan","Roberto","Nicolás"]
apellidos = ["De Pol","Beltran","Rabiot","Pastor","Garcia","Largo"]

#agregar esta informacion en un txt de forma optima

with open("archivos_problemas_resueltos\\problemaTXT\\nombres_y_apellidos.txt",'w',encoding="UTF-8") as archivo:
    archivo.writelines("\nLos datos son:\n\n")
    [archivo.writelines(f"Nombre: {n}\nApellido: {a}\n------------\n") for n,a in zip(nombres,apellidos)]


#[archivo.writelines(f"Nombre: {n}\nApellido: {a}\n------------\n") for n,a in zip(nombres,apellidos)]
#es lo mismo que hacer esto pero en una sola linea
#for n,a in zip(nombres,apellidos):
#    [archivo.writelines(f"Nombre: {n}\nApellido: {a}\n------------\n")