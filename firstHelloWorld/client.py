import socket

HOST = ""       # remote computer (localhost)
PORT = 33333    # port on the remote computer

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

sock.send("PALINDROM")
result = sock.recv(1024)

sock.close()

print "Received: ", result
