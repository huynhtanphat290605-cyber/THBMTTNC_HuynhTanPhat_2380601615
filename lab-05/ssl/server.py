import socket
import ssl
import threading

# Thông tin server
server_address = ('localhost', 12345)

# Danh sách các client đã kết nối
clients = []


def handle_client(client_socket):
    # Thêm client vào danh sách
    clients.append(client_socket)
    
    try:
        print("Đã kết nối với:", client_socket.getpeername())
        
        # Nhận và gửi dữ liệu
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            print("Nhận:", data.decode('utf-8'))
            
            # Gửi dữ liệu đến tất cả các client khác
            # Tạo một bản sao của danh sách để tránh lỗi khi có client bị xóa giữa chừng
            for client in clients[:]:
                if client != client_socket:
                    try:
                        client.send(data)
                    except:
                        if client in clients:
                            clients.remove(client)
    except Exception as e:
        print(f"Lỗi khi xử lý client: {e}")
    finally:
        # Sử dụng khối try-except khi lấy peername để tránh crash nếu client ngắt kết nối đột ngột
        try:
            print("Đã ngắt kết nối:", client_socket.getpeername())
        except:
            print("Đã ngắt kết nối: (Không thể xác định peername)")
            
        if client_socket in clients:
            clients.remove(client_socket)
        client_socket.close()


# Tạo socket server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(server_address)
server_socket.listen(5)

print("Server đang chờ kết nối...")

# Lắng nghe các kết nối
while True:
    client_socket, client_address = server_socket.accept()
    
    try:
        # Tạo SSL context
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)  # Khuyên dùng thay cho PROTOCOL_TLS cũ
        context.load_cert_chain(
            certfile="./certificates/server-cert.crt",
            keyfile="./certificates/server-key.key"
        )
        
        # Thiết lập kết nối SSL
        ssl_socket = context.wrap_socket(client_socket, server_side=True)
        
        # Bắt đầu một luồng xử lý cho mỗi client
        client_thread = threading.Thread(target=handle_client, args=(ssl_socket,))
        client_thread.start()
        
    except Exception as e:
        print(f"Lỗi thiết lập SSL với client {client_address}: {e}")
        client_socket.close()