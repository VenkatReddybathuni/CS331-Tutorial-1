import socket
import sys

def display_menu():
    print("\n=== Task Processing Menu ===")
    print("1. Change case of a string")
    print("2. Evaluate mathematical expression")
    print("3. Reverse a string")
    print("4. Exit")
    return input("Enter your choice (1-4): ")

def main():
    HOST = 'localhost'
    PORT = 12345

    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((HOST, PORT))
        
        while True:
            choice = display_menu()
            
            if choice == '4':
                print("Exiting...")
                break
                
            if choice in ['1', '2', '3']:
                data = input("Enter input string: ")
                message = f"{choice}:{data}"
                client_socket.send(message.encode())
                
                response = client_socket.recv(1024).decode()
                print(f"Server response: {response}")
            else:
                print("Invalid choice! Please try again.")

    except ConnectionRefusedError:
        print("Server is not running!")
    except KeyboardInterrupt:
        print("\nClient terminated by user")
    finally:
        client_socket.close()

if __name__ == "__main__":
    main()
