import socket

HOST = "127.0.0.1"
PORT = 8091

def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)

    print(f"Server đang lắng nghe tại {HOST}:{PORT}...")

    conn, addr = server_socket.accept()
    print("Client đã kết nối:", addr)

    data = conn.recv(1024).decode("utf-8")
    print("Server nhận được:", data)

    try:
        a, b = map(int, data.split())
        result = f"Tổng của {a} + {b} = {a + b}"
    except:
        result = "Dữ liệu không hợp lệ. Hãy nhập 2 số nguyên."

    conn.send(result.encode("utf-8"))

    conn.close()
    server_socket.close()

def run_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    a = input("Nhập số nguyên a: ")
    b = input("Nhập số nguyên b: ")

    message = a + " " + b
    client_socket.send(message.encode("utf-8"))

    data = client_socket.recv(1024).decode("utf-8")
    print("Kết quả từ server:", data)

    client_socket.close()

if __name__ == "__main__":
    mode = input("Chọn chế độ server/client: ").lower()

    if mode == "server":
        run_server()
    elif mode == "client":
        run_client()
    else:
        print("Vui lòng nhập server hoặc client.")