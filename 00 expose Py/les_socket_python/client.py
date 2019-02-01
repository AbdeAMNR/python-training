import socket

host = "localhost"  # localhost = 172.0.0.1 server address
port = 12345  # random , prefer to use port over 1023

sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sk.connect((host, port))
print("Connection on {}".format(port))
try:
    while True:
        myTxt = input('-->')
        sk.send(myTxt.encode())
        respons = sk.recv(255)
        if respons != "":
            print("server :", respons.decode('utf8'))
finally:
    sk.close()
