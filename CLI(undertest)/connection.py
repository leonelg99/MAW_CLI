import socket
from shared_variables import ESP32_CAM_IP, ESP32_CAM_PORT, SERVER_IP, SERVER_PORT
from interfaz import WINDOW,add_message

def obtener_ipv4():
    hostname = socket.gethostname()
    ipv4 = socket.gethostbyname(hostname)
    return ipv4

def makeMessage(data,data2,data3):
    message= "cmd:"+str(data)+":"+str(data2)+":"+str(data3)+"\n"  
    return message.encode()

def sendIP(IP):
    while True:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((ESP32_CAM_IP, ESP32_CAM_PORT))
                s.sendall(IP.encode())
                # Esperar una respuesta del servidor
                response = s.recv(1024)  # Ajusta el tamaño del búfer según tus necesidades
            # Si recibimos una respuesta, cortar el bucle y manejarla
                if response:
                    handle_response(response.decode())
                    break
        except Exception as e:
            add_message("Error al enviar IP: " + str(e), "error")

def sendMessage(data,data2,data3):
    print("SM")
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
         s.connect((ESP32_CAM_IP,ESP32_CAM_PORT))
         s.sendall(makeMessage(data,data2,data3))
         print(s.recv(1024))
    except Exception as e:
       add_message("Error al enviar comando: "+str(e),"error")
    finally:
        s.close()  


def reciveMessages():
   with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((SERVER_IP, SERVER_PORT))
        server.listen()
        
        while True:
            client_socket, client_address = server.accept()

            data = client_socket.recv(1024)
            if not data:
                break
            message=data.decode()
            add_message(message,"info")
            client_socket.close()
