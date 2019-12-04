import pickle
import smtplib
import socket
import ssl
import sys

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 49001  # Port to listen


def getmessage():
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
                    sys.exit()
                else:
                    print('To:', data['To'])
                    print('Theme:', data['Theme'])
                    print('Message:', data['Mail'])
                    data = (data['To'], data['Theme'], data['Mail'])
                    smtp_server = "smtp.gmail.com"
                    port = 587  # For starttls
                    sender_email = "example@mail.com"
                    password = "pass"
                    receiver_email = data[0]  # Enter receiver address
                    message = data[2]

                    # Create a secure SSL context
                    context = ssl.create_default_context()

                    # Try to log in to server and send email
                    try:
                        server = smtplib.SMTP(smtp_server, port)
                        server.ehlo()  # Can be omitted
                        server.starttls(context=context)  # Secure the connection
                        server.ehlo()  # Can be omitted
                        server.login(sender_email, password)
                        server.sendmail(sender_email, receiver_email, message)
                        print('Sent to gmail.')
                    except Exception as e:
                        # Print any error messages
                        print(e)
                    finally:
                        server.quit()


def sendingmail(data):
    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    sender_email = "example@mail.com"
    password = "pass"
    receiver_email = data[0]  # Enter receiver address
    message = data[2]

    # Create a secure SSL context
    context = ssl.create_default_context()

    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()  # Can be omitted
        server.starttls(context=context)  # Secure the connection
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
    except Exception as e:
        # Print any error messages
        print(e)
    finally:
        server.quit()


def main():
    getmessage()


main()
