#!F:/python files/youtubepython/network socket programming/python
#this is the server.py file

import socket

s = socket.socket()

host  = socket.gethostname()

port = 12345

s.bind(host,port)

s.listen()

while True:
    c, addr = s.accept()
    print('your decice is connected')
    c.send('Thank you for connecting')
    c.close()
    
    
