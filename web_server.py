import socket
HOST = '127.0.0.1'
PORT = 8080

def handle_request(client):
    request = client.recv(1024)
    print(request.decode())

    response = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\nHello, World!"
    client.sendall(response.encode())
    client.close()

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(1)
        print(f"Listening on {HOST}:{PORT}...")

        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                handle_request(conn)

if __name__ == '__main__':
    start_server()