import socket
import pickle
import hashlib
from random import random


HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

# Данные к отправке
data = random()
data = str(data).encode('utf-8')
# Контрольная сумма
checksum = hashlib.md5(data).digest()
print('data:', data)
print('checksum: ', checksum)
# Сериализация данных
to_send = pickle.dumps({'data': data, 'checksum': checksum})
print('Pickle data:', to_send)
print("Size of data to send: ", to_send.__sizeof__())

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(to_send)
