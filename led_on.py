import socket

def Main():
    host = '192.168.178.60' # IP of the controller
    port = 5577

    s = socket.socket()
    s.connect((host, port))

    s.send('EF0177'.decode('hex')) # connect
    data = s.recv(1024)
    s.send('CC2333'.decode('hex')) # send command (turn on in this case)
    s.close() # disconnect

if __name__ == '__main__':
    Main()