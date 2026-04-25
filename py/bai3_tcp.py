import socket
import re

HOST = "127.0.0.1"
PORT = 8092

def is_valid_password(password):
    if len(password) < 6 or len(password) > 12:
        return False

    if not re.search("[a-z]", password):
        return False

    if not re.search("[0-9]", password):
        return False

    if not re.search("[A-Z]", password):
        return False

    if not re.search("[$#@]", password):
        return False

    return True

def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)

    print(f"Server đang lắng nghe tại {HOST}:{PORT}...")

    conn, addr = server_socket.accept()
    print("Client đã kết nối:", addr)

    data = conn.recv(4096).decode("utf-8")
    print("Server nhận được:", data)

    passwords = data.split(",")
    valid_passwords = []

    for password in passwords:
        password = password.strip()
        if is_valid_password(password):
            valid_passwords.append(password)

    result = ",".join(valid_passwords)

    conn.send(result.encode("utf-8"))

    conn.close()
    server_socket.close()

def run_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    passwords = input("Nhập các mật khẩu, cách nhau bởi dấu phẩy: ")

    client_socket.send(passwords.encode("utf-8"))

    result = client_socket.recv(4096).decode("utf-8")

    print("Các mật khẩu hợp lệ là:", result)

    client_socket.close()

if __name__ == "__main__":
    mode = input("Chọn chế độ server/client: ").lower()

    if mode == "server":
        run_server()
    elif mode == "client":
        run_client()
    else:
        print("Vui lòng nhập server hoặc client.")