import socket
from shared_variables import ESP32_CAM_IP, ESP32_CAM_PORT

def sendMessage():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((ESP32_CAM_IP,ESP32_CAM_PORT))
        message = "Connection Successful"
        s.sendall(message.encode())
        dat=s.recv(1024)
        print(dat)
        s.close()


sendMessage()