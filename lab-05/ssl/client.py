import socket
import ssl
import threading

# Thông tin server
server_address = ('localhost', 12345)


def receive_data(ssl_socket):
    try:
        while True:
            data = ssl_socket.recv(1024)
            if not data:
                break
            print("\nNhận:", data.decode('utf-8'))
            # In lại dòng nhắc nhập tin nhắn sau khi nhận dữ liệu từ server để giao diện không bị đè chữ
            print("Nhập tin nhắn: ", end="", flush=True)
    except:
        pass
    finally:
        ssl_socket.close()
        print("\nKết nối đã đóng.")


# Tạo socket client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Tạo SSL context
# Thay thế ssl.PROTOCOL_TLS (đã lỗi thời) bằng ssl.PROTOCOL_TLS_CLIENT
context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)

# Cấu hình bỏ qua việc xác thực chứng chỉ (Do dùng chứng chỉ tự ký - Self-signed)

context.check_hostname = False
context.verify_mode = ssl.CERT_NONE
# Thiết lập kết nối SSL
ssl_socket = context.wrap_socket(client_socket, server_hostname='localhost')
ssl_socket.connect(server_address)

# Bắt đầu một luồng để nhận dữ liệu từ server
receive_thread = threading.Thread(target=receive_data, args=(ssl_socket,))
receive_thread.start()

# Gửi dữ liệu lên server
try:
    while True:
        message = input("Nhập tin nhắn: ")
        if not message:
            continue
        ssl_socket.send(message.encode('utf-8'))
except (KeyboardInterrupt, SystemExit):
    # Xử lý khi người dùng nhấn Ctrl+C để thoát chương trình một cách mượt mà
    print("\nĐang thoát chương trình...")
except Exception as e:
    print(f"\nCó lỗi xảy ra: {e}")
finally:
    ssl_socket.close()