import socket

server_address = '/tmp/uds_socket'

def sendMessage(message):
	s = socket.socket(socket.AF_UNIX)
	s.settimeout(1)
	s.connect(server_address)
	s.send(message)
	s.close()

sendMessage("Hello world")
