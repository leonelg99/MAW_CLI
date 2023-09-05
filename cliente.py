import pygame
import socket
import cv2

# Configuración de la conexión Wi-Fi
SERVER_IP = "192.168.1.100"  # Cambia esto por la dirección IP del MCU
SERVER_PORT = 12345  # Puerto de escucha en el MCU
SERVER_PASSWD = "MAW12345"  # Contraseña de la conexión Wi-Fi

# Inicializar pygame
pygame.init()

# Inicializar el joystick
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)  # Selecciona el primer joystick
joystick.init()

# Inicializar la conexión al servidor
#client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#client_socket.connect((SERVER_IP, SERVER_PORT))
#client_socket.recv(1024)  # Recibe el mensaje de bienvenida del MCU

#Crea la ventana de la camara
cv2.namedWindow("MAW CAM", cv2.WINDOW_GUI_EXPANDED)
#when there is no video show not_signal.jpg 
img = cv2.imread("not_signal.jpg")
cv2.imshow("MAW CAM", img)

# Inicializa la captura de video desde la cámara (cambia el número de cámara según corresponda)
cap = cv2.VideoCapture(0)

#KEYS:
#0: 1
#1: 2
#2: 3
#3: 4
#4: L1
#5: R1
#6: L2
#7: R2
#8: Select
#9: Start
#10: Stick Izquierdo
#11: Stick Derecho
### STICK DERECHO
#### A3: Arriva: de 0.0 a -1.0
####     Abajo: de 0.0 a 1.0
#### A2: Izquierda: de 0.0 a -1.0
####     Derecha: de 0.0 a 1.0
### STICK IZQUIERDO 
#### A1: Arriva: de 0.0 a -1.0
####     Abajo: de 0.0 a 1.0
#### A0: Izquierda: de 0.0 a -1.0
####     Derecha: de 0.0 a 1.0




while True:
    #if ESC is pressed terminate the program
    key = cv2.waitKey(1)
    if key == 27:
        break
    #if the window is closed terminate the program
    if cv2.getWindowProperty("MAW CAM", cv2.WND_PROP_VISIBLE) < 1:
        break
    try:
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                button = event.button
                print(button)
                # Envía el número del botón presionado al MCU
                #client_socket.send(str(button).encode())
            elif event.type == pygame.JOYAXISMOTION:
                axis = event.axis
                value = round((event.value)*100)
                # Envía el valor del eje al MCU (puedes personalizar esta parte)
                data = f"A{axis}:{value}"
                print(data)
                #client_socket.send(data.encode())
        
               #delay 100ms
    except KeyboardInterrupt:
        pass
    
    ##CAMARA
    try:
        ret, frame = cap.read() # Captura un cuadro de video
        cv2.imshow("MAW CAM", frame)
    except:
        pass
     #pygame.time.delay(50)

    


   



#client_socket.close()
pygame.quit()