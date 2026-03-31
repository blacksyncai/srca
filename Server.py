import socket
import os
import requests
from datetime import datetime

SUPABASE_URL = "https://wsulilnrvnetrdwtsbto.supabase.co"
SUPABASE_KEY = "sb_secret_fwv55Ybpo5mXbU7xzkLjKg_hC-ILuzz"

port = int(os.environ.get('PORT', 8000))
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('0.0.0.0', port))
server.listen(5)
print(f"TCP server listening on port {port}...")

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
conn.send(response.encode())
elif "APHP" in data:
parts = data.split(',')
hr = int(parts[1]) if len(parts​​​​​​​​​​​​​​​​
