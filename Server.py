import socket
import os
from datetime import datetime
import json
from supabase import create_client, Client

SUPABASE_URL = "https://wsulilnrvnetrdwtsbto.supabase.co"
SUPABASE_KEY = "sb_secret_fwv55Ybpo5mXbU7xzkLjKg_hC-ILuzz"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

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
hr = int(parts[1]) if len(parts) > 1 and parts[1] else None
sbp = int(parts[2]) if len(parts) > 2 and parts[2] else None
dbp = int(parts[3]) if len(parts) > 3 and parts[3] else None
spo2 = int(parts[4]) if len(parts) > 4 and parts[4] else None
bs = float(parts[5]) if len(parts) > 5
