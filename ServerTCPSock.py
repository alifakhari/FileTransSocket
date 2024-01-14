import socket
s = socket.socket()
s.bind(("localhost", 5000))

print('Listening to port ...')
s.listen(1)
c,a = s.accept()
filetodown = open("img.png", "wb")
while True:
   print("Receiving....")
   data = c.recv(1024)
   #print(data)
   if data.endswith(b"DONE"):
           print("Done Receiving.")
           break
   filetodown.write(data)
filetodown.close()
c.send(b"Thank you for connecting.")
c.shutdown(2)
c.close()
s.close()
#Done :)
