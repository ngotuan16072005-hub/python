import socket
import threading
import tkinter as tk
from tkinter import scrolledtext

PORT = 8093
sock = None
conn = None
role = None

def receive_message(connection):
    while True:
        try:
            message = connection.recv(1024).decode("utf-8")
            if not message:
                break

            chat_box.insert(tk.END, "Đối phương: " + message + "\n")
            chat_box.see(tk.END)
        except:
            break

def send_message():
    global sock, conn, role

    message = entry_message.get()

    if message.strip() == "":
        return

    try:
        if role == "server":
            conn.send(message.encode("utf-8"))
        else:
            sock.send(message.encode("utf-8"))

        chat_box.insert(tk.END, "Bạn: " + message + "\n")
        chat_box.see(tk.END)
        entry_message.delete(0, tk.END)
    except:
        chat_box.insert(tk.END, "Lỗi: Chưa kết nối hoặc không gửi được tin nhắn.\n")
        chat_box.see(tk.END)

def start_server():
    global sock, conn, role

    role = "server"

    host = "0.0.0.0"

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, PORT))
    sock.listen(1)

    chat_box.insert(tk.END, f"Server đang chờ client tại port {PORT}...\n")
    chat_box.see(tk.END)

    conn, addr = sock.accept()

    chat_box.insert(tk.END, f"Client đã kết nối: {addr}\n")
    chat_box.see(tk.END)

    thread_receive = threading.Thread(target=receive_message, args=(conn,))
    thread_receive.daemon = True
    thread_receive.start()

def start_client():
    global sock, role

    role = "client"

    host = entry_ip.get().strip()

    if host == "":
        host = "127.0.0.1"

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, PORT))

        chat_box.insert(tk.END, f"Đã kết nối tới server {host}:{PORT}\n")
        chat_box.see(tk.END)

        thread_receive = threading.Thread(target=receive_message, args=(sock,))
        thread_receive.daemon = True
        thread_receive.start()
    except:
        chat_box.insert(tk.END, "Không thể kết nối tới server.\n")
        chat_box.see(tk.END)

def run_server_thread():
    thread_server = threading.Thread(target=start_server)
    thread_server.daemon = True
    thread_server.start()

def run_client_thread():
    thread_client = threading.Thread(target=start_client)
    thread_client.daemon = True
    thread_client.start()

root = tk.Tk()
root.title("TCP Chat GUI - Server / Client")

frame_top = tk.Frame(root)
frame_top.pack(pady=10)

label_ip = tk.Label(frame_top, text="IP Server:")
label_ip.pack(side=tk.LEFT)

entry_ip = tk.Entry(frame_top, width=20)
entry_ip.insert(0, "127.0.0.1")
entry_ip.pack(side=tk.LEFT, padx=5)

btn_server = tk.Button(frame_top, text="Chạy Server", command=run_server_thread)
btn_server.pack(side=tk.LEFT, padx=5)

btn_client = tk.Button(frame_top, text="Chạy Client", command=run_client_thread)
btn_client.pack(side=tk.LEFT, padx=5)

chat_box = scrolledtext.ScrolledText(root, width=60, height=20)
chat_box.pack(padx=10, pady=10)

frame_bottom = tk.Frame(root)
frame_bottom.pack(pady=10)

entry_message = tk.Entry(frame_bottom, width=45)
entry_message.pack(side=tk.LEFT, padx=5)

btn_send = tk.Button(frame_bottom, text="Gửi", command=send_message)
btn_send.pack(side=tk.LEFT, padx=5)

root.mainloop()