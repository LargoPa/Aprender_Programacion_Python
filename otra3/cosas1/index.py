import time
from plyer import notification

if __name__ == '__main__':
    notification.notify(title="Alerta de prueba", message="Esto es el cuerdo de la notificacion", timeout=10)
    time.sleep(10)