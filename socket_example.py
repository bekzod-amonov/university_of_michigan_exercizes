import socket # for socket
import sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print ("Socket successfully created")
except socket.error as err:
    print ("socket creation failed with error %s" %(err))

# default port for socket
port = 55555
s.bind(('', port))
print('socket binded to %s' %(port))
s.listen(5)
print('socket is listening')

while True:
    c, addr = s.accept()
    print('Got connetion from', addr)
    c.send('Thank you for connecting'.encode())
    c.close()
    break

#try:
#    host_ip = socket.gethostbyname('www.google.com')
#except socket.gaierror:
#
#    # this means could not resolve the host
#    print ("there was an error resolving the host")
#    sys.exit()
#
# connecting to the server
#mysocket.connect((host_ip, port))
#
#print ("the socket has successfully connected to google")
