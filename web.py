import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)
while True:
print(data.decode(),end='')
if len(data) < 1:
break
data = mysock.recv(512)
mysock.close()

sudo apt-get install python-mysqldb