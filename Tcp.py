import socket
import threading

"""Maximum number of clients that can be connected to the server
"""
limit = 200
"""Dictionary storing client connections.
"""
clients = {}
"""List to store client connections in order of their rank.
"""
ranks = [None] * limit
"""Locking to ensure only one thread can modify the shared data structures at a time
"""
lock = threading.Lock()

def handle_client(conn, address, clients, ranks, lock):
    rank = None
    
    """LOcking the shared ds while we modify them
    """
    with lock:
        if len(clients) < limit:
            rank = len(clients)
            clients[conn] = rank
            ranks[rank] = conn
            print(f"Accepted client {address} with rank {rank}")
        else:
            print(f"Rejected client {address}: limit reached")
            conn.close()
            return

    """Listening  message form client
    """
    while True:
        data = conn.recv(1024).decode()
        
        if not data:
            break
        
        """breaking out of loop when client disconnects
        """
        
        """message splits into two parts
        """
        parts = data.split()
        cmd = parts[0]
        
    """Hadnling the EXEC command where another client requests to another client to execute a command
    """
    if cmd == "EXEC":
            target_rank = int(parts[1])
            if target_rank < rank:
                target_conn = ranks[target_rank]
                target_conn.send(f"EXEC {rank} {' '.join(parts[2:])}".encode())
            else:
                conn.send(f"ERROR {rank} rank too high".encode())
    else:
            conn.send(f"ERROR {rank} unknown command".encode())

    """removing clients connection and rank while adjusting ranksnof remaining clients
    """
    with lock:
        del clients[conn]
        del ranks[rank]
        for i in range(rank, len(ranks)):
            clients[ranks[i]] = i
            ranks[i] = ranks[i+1]
        del ranks[len(ranks)]
        print(f"Closed connection to {address} with rank {rank}")
        
    """Close the connection
    """
    conn.close()

    """Starting server and listening to incoming connections
    """
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(("localhost", 5000))
    s.listen()
    print("Listening on localhost:5000")
    while True:
        conn, address = s.accept()
        print(f"Accepted connection from {address}")
        t = threading.Thread(target=handle_client, args=(conn, address, clients, ranks, lock))
        t.start()
