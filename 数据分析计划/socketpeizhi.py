import socket
def tongxintcpfuwu():
    x = socket.socket()
    x.bind(("127.0.0.1",14414))
    while True:
       x.listen(1)
       conn,address = x.accept()
       print(address)
       conn.sendall(bytes("Hello! A_dmin!!",encoding="utf-8"))
       conn.close()
def tongxinudpfuwu():
    soc1=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    soc1.bind(('0.0.0.0',7788))
    while True:
        recive, sender_info = soc1.recvfrom(1024)
        recive = recive.decode("utf-8")
        break
    soc1.close()
    return recive
def tongxinudpfasong(data):
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    localaddr = ("0.0.0.0",788) 
    udp_socket.bind(localaddr)
    sendadd=("0.0.0.0",7788)
    while True:
        udp_socket.sendto(data,sendadd)
        udp_socket.close()
        
def tongxintcpfasong(ip):
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_addr = (ip,81)
    tcp_socket.connect(server_addr)
    while True:
        data = tcp_socket.recv(1024)
        print(data)
        with open('new.wmv','wb') as fout:
            fout.write(data)
