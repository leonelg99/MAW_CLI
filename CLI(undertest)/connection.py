import socket
from shared_variables import ESP32_CAM_IP, ESP32_CAM_PORT, SERVER_IP, SERVER_PORT
from interfaz import WINDOW,add_message
from zeroconf import ServiceInfo, Zeroconf

def obtener_ipv4():
    hostname = socket.gethostname()
    ipv4 = socket.gethostbyname(hostname)
    return ipv4

def makeMessage(data,data2,data3):
    message= "cmd:"+str(data)+":"+str(data2)+":"+str(data3)+"\n"  
    return message.encode()

def sendMessage(data,data2,data3):
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
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((ESP32_CAM_IP,ESP32_CAM_PORT))
            s.sendall("get:0:0:0\n".encode())
            data = s.recv(1024).decode()
            if(data is not ""):
                add_message(data,"normal")
            else: print("No data")
    except Exception as e:
        add_message("Error al recibir comando: "+str(e),"error")
    finally:
        s.close()
    