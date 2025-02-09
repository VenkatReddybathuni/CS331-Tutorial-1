import socket
from task_processor import process_task

def main():
    HOST = 'localhost'
    PORT = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    
    print(f"Single-process server listening on {HOST}:{PORT}")

    try:
        while True:
            client_socket, address = server_socket.accept()
            print(f"Connected to client: {address}")
            
            try:
                while True:
                    data = client_socket.recv(1024).decode()
                    if not data:
                        break
                        
                    result = process_task(data)
                    client_socket.send(result.encode())
            except:
                pass
            finally:
                client_socket.close()
                print(f"Connection closed with {address}")
                
    except KeyboardInterrupt:
        print("\nServer terminated by user")
    finally:
        server_socket.close()

if __name__ == "__main__":
    main()
