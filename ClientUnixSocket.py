import socket
import os
import time


ttime = time.time()
# Set the path for the Unix socket
socket_path = '/tmp/my_socket'

# Create the Unix socket client
client = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

# Connect to the server
client.connect(socket_path)

# Send a message to the server
message = 'Hello from the client!'
client.sendall(message.encode())

###########
filetosend = open("image.rar", "rb")
data = filetosend.read(1024)
i=0
while data:
    #i +=1
    #print(f"Sending... Chunk {i}")
    client.send(data)
    data = filetosend.read(1024)
filetosend.close()
client.send(b"DONE")
print(f"Done Sending... in {time.time()-ttime}")
#####


# Receive a response from the server
response = client.recv(1024)
print(f'Received response: {response.decode()}')

# Close the connection
client.close()