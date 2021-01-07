import socket
import threading
import os
import time

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print("\t\t\t\t------------------------------")
print("\t\t\t\t########## Chat App ##########")
print("\t\t\t\t------------------------------")
serverip = input("\n\t\tEnter Your IP : ")
serverport = 1111

clientip = input("\n\t\tEnter Your Friends IP : ")
clientport = 1111

s.bind( (serverip, serverport) )

def send():
    while True:
        msg = input("Your Message: ").encode()
        s.sendto(msg,(clientip,clientport))
        if msg.decode() == "exit" or msg.decode() == "quit":
            os._exit(1)

def recv():
        msg = s.recvfrom(1024)
        if msg[0].decode() == "quit" or msg[0].decode() == "exit":
            os._exit(1)
        print('\n\t\t\t\t\t\tReceived Msg: '+ msg[0].decode())
        time.sleep(10)


t1 = threading.Thread(target=recv)
t1.start()
    
t1 = threading.Thread(target=send)
t1.start()

while True:
    t2 = threading.Thread(target=recv)
    t2.start()
