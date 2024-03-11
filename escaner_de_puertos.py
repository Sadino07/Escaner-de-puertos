import socket

ip = input('ingrese ip a escanear: ')

for puerto in range(1, 65535):
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)
    
    result = sock.connect_ex((ip, puerto))
    
    if (result == 0):{
         print('puerto abierto: ' + str(puerto))}
    else:{
        print('puerto cerrado o filtrado: ' + str(puerto))
    }
        
        
    sock.close()