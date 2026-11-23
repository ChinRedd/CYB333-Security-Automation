# server.py
# Basic TCP server for the CYB333 Midterm Exam

import socket

# Server configuration
HOST = "127.0.0.1"
PORT = 5000


def start_server():
    """Create a server, accept a client, and exchange messages."""

    # Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Allow the port to be reused after the program closes
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # Bind the socket to the local address and port
        server_socket.bind((HOST, PORT))

        # Start listening for incoming connections
        server_socket.listen(1)
        print(f"Server listening on {HOST}:{PORT}")
        print("Waiting for a client connection...")

        # Accept an incoming connection
        client_socket, client_address = server_socket.accept()

        print(f"Connected to client: {client_address}")

        with client_socket:
            # Receive a message from the client
            message = client_socket.recv(1024).decode("utf-8")

            if message:
                print(f"Client message: {message}")

                # Send a response back to the client
                response = "Message received successfully!"
                client_socket.sendall(response.encode("utf-8"))

                print(f"Server response sent: {response}")

        print("Client disconnected.")
        print("Server shutting down.")

    except OSError as error:
        print(f"Server error: {error}")

    finally:
        # Close the server socket
        server_socket.close()
        print("Server socket closed.")


if __name__ == "__main__":
    start_server()