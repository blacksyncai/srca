import socket
from datetime import datetime

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 8000))
server.listen(5)
print("TCP server listening on port 8000...")

while True:
    conn, addr = server.accept()
    print(f"Watch connected: {addr}")
    while True:
        data = conn.recv(1024).decode('utf-8', errors='ignore')
        if not data:
            break
        print(f"Received: {data}")
        if "AP00" in data:
            response = f"IW*BP00*,{datetime.utcnow().strftime('%Y%m%d%H%M%S')},3#"
            conn.send(response.encode())elif "APHP" in data:
            conn.send(b"IWBPHP#")
    conn.close()
    