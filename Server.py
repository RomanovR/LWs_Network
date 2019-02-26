import sys
import socket
import pickle
import hashlib
from random import random

# For the receiving socket.
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 49001  # Port to listen on (non-privileged ports are > 1023)

#For the transmitting socket
HOST_3 = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT_3 = 49002  # Port to listen on (non-privileged ports are > 1023)


def main():
    print("Waiting for connect...")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, address = s.accept()
        with conn:
            print('Connected by ', address)
            while True:
                data_rec = conn.recv(1024)
                if not data_rec:
                    break
                try:
                    data = pickle.loads(data_rec)
                    if hashlib.md5(data['data']).digest() != data['checksum']:
                        raise ValueError
                except pickle.UnpicklingError:
                    print("Received incorrect data.")
                    sys.exit()
                except ValueError:
                    print("Incorrect checksum, data is corrupted.")
                    sys.exit()
                else:
                    print("Number:", float(data['data']))

                    # Data to send.
                    data_add = random()
                    print('Data to send: ', float(data['data']), ', ', data_add)
                    data_add = str(data_add).encode('utf-8')

                    checksum = hashlib.md5(data['data'] + data_add).digest()
                    print(checksum)
                    # Serialization data + checksum.
                    to_send = pickle.dumps({'1': data['data'], '2': data_add, 'checksum': checksum})

                    print('Connecting...')
                    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s_to_third:
                        try:
                            s_to_third.connect((HOST, PORT))
                        except ConnectionRefusedError:
                            print('Connection refused.')
                        else:
                            s_to_third.sendall(to_send)
                            print('Sent.')


main()
