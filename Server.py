import socket
import pickle
import hashlib
from random import random

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

print("Waiting for connect...")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, address = s.accept()
    with conn:
        print('Connected by ', address)
        x = 5
        while True:
            data_rec = conn.recv(1024)
            if not data_rec:
                break
            try:
                data = pickle.loads(data_rec)
                if hashlib.md5(data['data']).digest() != data['checksum']:
                    print("Data is corrupted.")
                    
                print("Number:", float(data['data']))
            except pickle.UnpicklingError:
                print("Received incorrect data.")




