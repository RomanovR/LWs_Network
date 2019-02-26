import sys
import socket
import pickle
import hashlib
from random import random

# For the receiving socket.
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 49001  # Port to listen on (non-privileged ports are > 1023)

# For the transmitting socket
HOST_3 = '127.0.0.1'
PORT_3 = 49002

# Startup order:
# 1. Recipient.py(third app)
# 2. Server.py(second app)
# 3. Client.py(first app)


def main():
    print('Second app.')
    print("Waiting for connect...")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, address = s.accept()
        with conn:
            print('Connected by', address)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                try:
                    data = pickle.loads(data)
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

                    # Serialization data, checksum.
                    to_send = pickle.dumps({'1': data['data'], '2': data_add, 'checksum': checksum})

                    print('Connecting...')
                    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s_to_third:
                        try:
                            s_to_third.connect((HOST_3, PORT_3))
                        except ConnectionRefusedError:
                            print('Connection refused.')
                        else:
                            s_to_third.sendall(to_send)
                            print('Sent.')


main()
