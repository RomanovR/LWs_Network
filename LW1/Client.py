import socket
import pickle
import hashlib
from random import random

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 49001        # The port used by the server

# Startup order:
# 1. Recipient.py(third app)
# 2. Server.py(second app)
# 3. Client.py(first app)


def main():
    print('First app.')
    # Данные к отправке
    data = random()
    print('Data to send: ', data)
    data = str(data).encode('utf-8')
    # Контрольная сумма
    checksum = hashlib.md5(data).digest()
    # Сериализация данных
    to_send = pickle.dumps({'data': data, 'checksum': checksum})

    print('Connecting...')
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((HOST, PORT))
        except ConnectionRefusedError:
            print('Connection refused.')
        else:
            s.sendall(to_send)
            print('Sent.')


main()
