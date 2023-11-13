import socket
import cv2
import numpy as np
import time

# Function to send metrics to a remote server
def send_metrics(metrics_data, server_ip, server_port):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((server_ip, server_port))
        client_socket.sendall(metrics_data.encode())
        client_socket.close()
    except Exception as e:
        print(f"Failed to send metrics: {e}")

def process_video(connection, metrics_server_ip, metrics_server_port):
    # This is a placeholder for the video processing logic
    frame_count = 0
    cap = cv2.VideoCapture(0)  # Open a video capture device (you can change the index or file path)

    while True:
        # Read a frame from the video capture
        ret, frame = cap.read()
        if not ret:
            break

        frame_count += 1
        print(f"Received frame {frame_count}")

        # Get video resolution and frame rate
        height, width, _ = frame.shape
        fps = cap.get(cv2.CAP_PROP_FPS)

        # Send resolution and frame rate as metrics
        metrics_data = f"Frame {frame_count} metrics: Resolution={width}x{height}, FrameRate={fps} fps"
        send_metrics(metrics_data, metrics_server_ip, metrics_server_port)

        # Process the frame (you can add your processing logic here)

    cap.release()
    connection.close()

def start_server(port, metrics_server_ip, metrics_server_port):
    # Create a socket and bind to the port
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', port))
    server_socket.listen()

    print(f"Listening for connections on port {port}...")

    # Accept a connection
    connection, client_address = server_socket.accept()
    print(f"Connection from {client_address}")

    process_video(connection, metrics_server_ip, metrics_server_port)

if __name__ == "__main__":
    # Define the port to listen on
    listen_port = 80  # Replace with the actual port you want to use

    # Define the metrics server IP and port
    metrics_server_ip = '3.15.154.36'
    metrics_server_port = 8888

    start_server(listen_port, metrics_server_ip, metrics_server_port)
