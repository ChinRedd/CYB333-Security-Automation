# port_scanner.py
# Basic localhost port scanner for the CYB333 Midterm Exam

import socket
import time


def scan_port(host, port):
    """Check whether a port on localhost is accepting connections."""

    # Create a TCP socket
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Set a timeout to prevent waiting too long
    scanner.settimeout(1)

    try:
        # Attempt to connect to the specified port
        result = scanner.connect_ex((host, port))

        if result == 0:
            return "OPEN"
        else:
            return "CLOSED"

    except socket.error as error:
        print(f"Error scanning port {port}: {error}")
        return "ERROR"

    finally:
        # Always close the socket
        scanner.close()


def main():
    """Run the port scanner."""

    host = "127.0.0.1"

    print("=" * 40)
    print("CYB333 Localhost Port Scanner")
    print("=" * 40)
    print(f"Target: {host}")

    # Get the starting port
    try:
        start_port = int(input("Enter starting port (1-1024): "))
        end_port = int(input("Enter ending port (1-1024): "))

    except ValueError:
        print("Error: Port numbers must be integers.")
        return

    # Validate the port range
    if not (1 <= start_port <= 1024):
        print("Error: Starting port must be between 1 and 1024.")
        return

    if not (1 <= end_port <= 1024):
        print("Error: Ending port must be between 1 and 1024.")
        return

    if start_port > end_port:
        print("Error: Starting port cannot exceed ending port.")
        return

    print("\nStarting scan...")
    print("-" * 40)

    # Scan each port in the specified range
    for port in range(start_port, end_port + 1):

        status = scan_port(host, port)

        print(f"Port {port}: {status}")

        # Add a small delay between scans
        time.sleep(0.1)

    print("-" * 40)
    print("Scan complete.")


if __name__ == "__main__":
    main()