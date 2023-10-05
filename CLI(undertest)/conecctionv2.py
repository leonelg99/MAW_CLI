import socket
from shared_variables import ESP32_CAM_IP, ESP32_CAM_PORT

def makeMessage(data,data2):
    #transform data and data2 to string


    message= "cmd:"+str(data)+":"+str(data2)+"\n"  
    return message.encode()

def sendMessage(data,data2):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((ESP32_CAM_IP,ESP32_CAM_PORT))
        s.sendall(makeMessage(data,data2))
        dat=s.recv(1024)
        print(dat)
        s.close()


