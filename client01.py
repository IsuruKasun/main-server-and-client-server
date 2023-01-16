import socket


HEADER = 64 # how many bites are sending from each client 
# send 64 bites from client 1 and send 64 bites from client 2 and waite client 1 to sent secound part of the messege 
PORT = 5050 #poet must be above 4000 
FORMAT = 'utf-8'
DISCONNECT_MESSEGE = "!DISCONNECT" # after getting all messeges from client, we need to desconnect
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)



