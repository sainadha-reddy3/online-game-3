import socket
from _thread import*
import sys

server = "255.255.255.0"
port = 5555
 
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
    s.blind((server,port))

except socket.error as e:
    str(e)

s.listen(2)
print("waiting foe a connection, server started")

def threaded_client(conn):
    conn.send(str.encode("connected"))
    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")
            if not data:
                print("Disconnected")
                break
            else:
                print("Recieved:", reply)
                print("sending:", reply)
  

            conn.sendall(str.encode(reply))
        expect:
        break
while True:
    conn, addr = s.accept()
    print("connected to:",addr)

    start_new_thread(threaded_client, (conn,))
