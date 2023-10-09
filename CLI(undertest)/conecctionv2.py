import socket
from shared_variables import ESP32_CAM_IP, ESP32_CAM_PORT

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




