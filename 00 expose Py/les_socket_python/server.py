import socket

sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sk.bind(('', 12345))  # ''--> the server get the client ip addressin this case localhost ; 12345 the port used
sk.listen(2)
sk.settimeout(200)  # 200 sec before the server stop listening
clt, address = sk.accept()
print("{} connected".format(address))
try:
    while True:
        response = clt.recv(1024)  # ready to receive 1024o=ko from the client
        if response != "":
            print("client :", response.decode('utf8'))  # show client message
        servTxt = input('-->')  # write a message
        #  print("me the server :", servTxt)
        clt.send(servTxt.encode())  # send the message to the client

finally:
    clt.close()
    sk.close()
