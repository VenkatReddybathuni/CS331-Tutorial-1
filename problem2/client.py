import socket
import time
from constants import HOST, PORT, TEST_STRING

def run_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((HOST, PORT))
        client.send(TEST_STRING.encode())
        response = client.recv(1024).decode()
        print(f"Received: {response}")
    finally:
        client.close()

if __name__ == "__main__":
    run_client()
