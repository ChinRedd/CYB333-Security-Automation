# client.py
# Basic TCP client for the CYB333 Midterm Exam

import socket

# Server configuration
HOST = "127.0.0.1"
PORT = 5000


def start_client():
    """Connect to the server and exchange a message."""

    # Create a TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        print(f"Connecting to server at {HOST}:{PORT}...")

        # Establish a connection to the server
        client_socket.connect((HOST, PORT))

        print("Connected to server successfully!")

        # Send a message to the server
        message = "Hello from the client!"
        client_socket.sendall(message.encode("utf-8"))

        print(f"Message sent: {message}")

        # Receive the server's response
        response = client_socket.recv(1024).decode("utf-8")

        print(f"Server response: {response}")

    except ConnectionRefusedError:
        print("Connection failed: The server is not running.")

    except OSError as error:
        print(f"Client error: {error}")

    finally:
        # Close the client socket
        client_socket.close()
        print("Client socket closed.")


if __name__ == "__main__":
    start_client()