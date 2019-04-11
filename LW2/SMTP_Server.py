import socket
import pickle
#import smtplib, ssl

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 49001  # Port to listen on (non-privileged ports are > 1023)

port = 465  # For SSL
password = input("Type your password and press enter: ")

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
            except pickle.UnpicklingError:
                print("Received incorrect data.")
            else:
                print('To:', data['To'])
                print('Theme:', data['Theme'])
                print('Message:', data['Mail'])
