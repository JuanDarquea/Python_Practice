import socket
import requests

def main_socket():
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect(('data.pr4e.org', 80))
    cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
    mysock.send(cmd)
    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        print(data.decode(), end='')
    mysock.close()

def main_request():
    r = requests.get("http://data.pr4e.org/romeo.txt")
    print(r.text)

if __name__ == "__main__":
    main_socket()
    print()
    main_request()
