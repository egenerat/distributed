import socket
import os

server_address = '/tmp/uds_socket'

# Unlink the socket if it already exists
try:
    os.unlink(server_address)
except OSError:
    if os.path.exists(server_address):
        raise

# Create a socket
try:
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
except socket.error:
    print 'Failed to create socket'
    sys.exit()
sock.bind(server_address)

# Allow 5 connections
sock.listen(5)

while True:
    clientSocket, addr = sock.accept()
    print("Received a connection")
    clientSocket.close()
