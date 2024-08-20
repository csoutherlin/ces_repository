import socket

HOST = '127.0.0.1'
PORT = 8080

def make_request():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        request = "GET / HTTP/1.1\r\nHost: localhost\r\n\r\n"
        s.sendall(request.encode())

        response = b""
        while True:
            data = s.recv(1024)
            if not data:
                break
            response += data

    return response.decode()

if __name__ == '__main__':
    response = make_request()
    print(response)