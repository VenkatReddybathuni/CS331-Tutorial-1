import socket
import multiprocessing
from task_processor import process_task

def handle_client(client_socket, address):
    try:
        while True:
            data = client_socket.recv(1024).decode()
            if not data:
                break
                
            result = process_task(data)
            client_socket.send(result.encode())
    finally:
        client_socket.close()
        print(f"Connection closed with {address}")

def main():
    HOST = 'localhost'
    PORT = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    
    print(f"Multi-process server listening on {HOST}:{PORT}")

    try:
        while True:
            client_socket, address = server_socket.accept()
            print(f"Connected to client: {address}")
            
            # Create a new process for each client connection
            process = multiprocessing.Process(target=handle_client, args=(client_socket, address))
            process.daemon = True  # Make process daemon so it exits when the main process exits
            process.start()
            
            # Close the client socket in the main process to avoid resource leaks
            client_socket.close()
                
    except KeyboardInterrupt:
        print("\nServer terminated by user")
    finally:
        server_socket.close()

if __name__ == "__main__":
    main()
















# import socket
# from task_processor import process_task
# import os

# def handle_client(client_socket, address):
#     try:
#         while True:
#             data = client_socket.recv(1024).decode()
#             if not data:
#                 break
                
#             result = process_task(data)
#             client_socket.send(result.encode())
#     finally:
#         client_socket.close()
#         print(f"Connection closed with {address}")

# def main():
#     HOST = 'localhost'
#     PORT = 12345

#     server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#     server_socket.bind((HOST, PORT))
#     server_socket.listen(5)
    
#     print(f"Multi-process server listening on {HOST}:{PORT}")

#     try:
#         while True:
#             client_socket, address = server_socket.accept()
#             print(f"Connected to client: {address}")
            
#             pid = os.fork()
#             if pid == 0:  # Child process
#                 server_socket.close()
#                 handle_client(client_socket, address)
#                 os._exit(0)
#             else:  # Parent process
#                 client_socket.close()
                
#     except KeyboardInterrupt:
#         print("\nServer terminated by user")
#     finally:
#         server_socket.close()

# if __name__ == "__main__":
#     main()
