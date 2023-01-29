import threading
import socket

limit = 200
clients = []
ranks =  [i for i in range[limit]]

def handle_client(conn, addr):
    """Checking if the number of clinets has reached the limit
    """
    if len(clients) >= limit:
        conn.send(f"Server is full, try later".encode())
        conn.close()
        return
    