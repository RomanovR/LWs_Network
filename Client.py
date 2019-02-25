import socket
import pickle
import hashlib
from random import random


HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

# Данные к отправке
data = random()
data = str(data).encode('utf-8')
print('Data to send: ', data)
# Контрольная сумма
checksum = hashlib.md5(data).digest()
# Сериализация данных
to_send = pickle.dumps({'data': data, 'checksum': checksum})

print('Connecting...')
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(to_send)
    print('Sent.')

