import socket
import sys

HOST = "127.0.0.1"
PORT = 8090

def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)

    print(f"Server đang lắng nghe tại {HOST}:{PORT}...")

    conn, addr = server_socket.accept()
    print("Client đã kết nối:", addr)

    data = conn.recv(1024).decode("utf-8")
    print("Server nhận được:", data)

    message = "From SERVER TCP"
    conn.send(message.encode("utf-8"))
    print("Server đã gửi:", message)

    conn.close()
    server_socket.close()

def run_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    message = "From CLIENT TCP"
    client_socket.send(message.encode("utf-8"))
    print("Client đã gửi:", message)

    data = client_socket.recv(1024).decode("utf-8")
    print("Client nhận được:", data)

    client_socket.close()

if __name__ == "__main__":
    mode = input("Chọn chế độ server/client: ").lower()

    if mode == "server":
        run_server()
    elif mode == "client":
        run_client()
    else:
        print("Vui lòng nhập server hoặc client.")