import socket
import threading #do not wite for other codes. handling stuff in separate threads for each client so client is not waiting for other clients 

HEADER = 64 # how many bites are sending from each client 
# send 64 bites from client 1 and send 64 bites from client 2 and waite client 1 to sent secound part of the messege 
PORT = 5050 #poet must be above 4000 
SERVER = socket.gethostbyname(socket.gethostname()) # geting the local IP address. SERVER = "192.168.112.1"

print(SERVER)
print(socket.gethostname()) #DESKTOP-MGHMP89 - our server name 

ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSEGE = "!DISCONNECT" # after getting all messeges from client, we need to desconnect

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#make a socket (going to alow us to conect a divice to other connection). 
# socket.AF_INET - family of socket. tells to the socket what type of IP address are we going to accept for specific connections
# SOCK_STREAM - streaming data through the socket 

server.bind(ADDR) # when we bind a socket we can use ADDR

def handle_client(conn, addr): #define hendle_client as a funtion. conn - connection- allow us to the connection the object (addr)
    print(f"[NEW CONNECTION] {addr} connected." ) #more client connect paralaly //

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT) # how many bytes we want to reseve from the client # decode = everytime when we got a messege, we need to encode it in to byte format 
        if msg_length:
            msg_length = int(msg_length) # convet messege to intiger 
            msg = conn.recv(msg_length).decode(FORMAT) # then, we reseve next messege
            if msg == DISCONNECT_MESSEGE:
                connected = False

        print(f"[{addr}] {msg}") #print the address ans messege form the client

    conn.close() #close the current cunnection 





def start(): #starts the socket server for us 
    server.listen()    # alow our server to lisning our connections and hannling and passing to client which is run in a new thread
    print(f"[LISTENNING] Server is listening on {SERVER}") #we can see what IP address runing on 

    while True:
        conn, addr = server.accept() # waite new connection to the server. when new connection to the server, we will store the address(ip) of the connection.  
        thread = threading.Thread(target=handle_client, args=(conn, addr)) #macking a new thread 
        thread.start() #start the thread 
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() -1}") #tells how many threads are active in this process
        

print("[STARTING] server is sarting...")
start()
