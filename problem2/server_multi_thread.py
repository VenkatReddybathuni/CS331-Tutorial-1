import socket
import time
from threading import Thread
from constants import HOST, PORT, DELAY_SECONDS

def handle_client(client_socket):
    data = client_socket.recv(1024).decode()
    time.sleep(DELAY_SECONDS)  # Simulate processing delay
    reversed_string = data[::-1]
    client_socket.send(reversed_string.encode())
    client_socket.close()

def run_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(5)
    print("Multi-threaded server is listening...")
    
    try:
        while True:
            client, addr = server.accept()
            print(f"Connected to {addr}")
            thread = Thread(target=handle_client, args=(client,))
            thread.daemon = True  # Make thread daemon so it exits when main thread exits
            thread.start()
    except KeyboardInterrupt:
        print("\nShutting down server...")
    finally:
        server.close()
        print("Server socket closed")

if __name__ == "__main__":
    run_server()
