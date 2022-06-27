from socket import *
import sys

PLACE = ('localhost', 8888)


def client():
    with socket(AF_INET, SOCK_STREAM) as sock:  # CosnaTo COKeT TCP 8 KONETpyRUM NICh
        sock.connect(PLACE)
        while True:
            message = input("Your message :")
            sock.send(message.encode('utf-8'))
            receive = sock.recv(1024).decode('utf-8')
            print('Orber:', receive)


if __name__ == "__main__":
    client()