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
        print('Connected by', address)
        while True:
            rec_data = pickle.loads(conn.recv(1024))
            if not rec_data:
                break
if hashlib.md5(rec_data['data']).digest() == rec_data['checksum']:
    print("Data is correct.")
else:
    print("Data is corrupted.")
print("Number:", rec_data['data'])
print("Checksum:", rec_data['checksum'])


