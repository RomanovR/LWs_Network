import socket
import pickle

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        usr_in = input('Data to send(S - to exit):')
        if usr_in == 'S':
            break
        pickle_data = pickle.dumps(usr_in)
        s.sendall(pickle_data)