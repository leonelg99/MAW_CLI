import socket
from shared_variables import ESP32_CAM_IP, ESP32_CAM_PORT, SERVER_IP, SERVER_PORT
from interfaz import WINDOW,add_message


def makeMessage(data,data2):
    message= "cmd:"+str(data)+":"+str(data2)+"\n"  
    return message.encode()

def sendMessage(data,data2):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
         s.connect((ESP32_CAM_IP,ESP32_CAM_PORT))
         s.sendall(makeMessage(data,data2))
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
