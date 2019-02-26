import sys
import socket
import pickle
import hashlib

'''
 Есть три приложения, первое отправляет случайное число и его хэш, второе получает
хэш от хэша склеивания с новым случайным числом, и отправляет этот хэш, случайное
число и новое случайное число на третье приложение.Третье приложение
проверяет правильность полученных чисел.
'''

# For the receiving socket.
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 49002  # Port to listen on (non-privileged ports are > 1023)

# Startup order:
# 1. Recipient.py(third app)
# 2. Server.py(second app)
# 3. Client.py(first app)


def main():
    print('Third app.')
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
                    if hashlib.md5(data['1'] + data['2']).digest() != data['checksum']:
                        raise ValueError
                except pickle.UnpicklingError:
                    print("Received incorrect data.")
                    sys.exit()
                except ValueError:
                    print("Incorrect checksum, data is corrupted.")
                    sys.exit()
                else:
                    print("Received data:", float(data['1']), ', ', float(data['2']))


main()
