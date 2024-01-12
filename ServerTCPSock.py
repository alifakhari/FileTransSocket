import socket
s = socket.socket()
s.bind(("localhost", 50000))

print('Listening to port ...')
s.listen(1)
c,a = s.accept()
filetodown = open("img.png", "wb")
while True:
   print("Receiving....")
   data = c.recv(1024)
   if data == b"DONE":
           print("Done Receiving.")
           break
   filetodown.write(data)
filetodown.close()
c.send("Thank you for connecting.")
c.shutdown(2)
c.close()
s.close()
#Done :)
