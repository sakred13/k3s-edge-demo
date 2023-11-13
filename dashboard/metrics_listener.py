import asyncio
import socket
import websockets

# Global variable to store the latest metrics
latest_metrics = ""

async def handle_connection(websocket, path):
    try:
        while True:
            # Send the latest metrics data to the connected client
            await websocket.send(latest_metrics)
            await asyncio.sleep(3)  # Send data every 3 seconds
    except websockets.exceptions.ConnectionClosedError:
        pass

def start_listener(port):
    # Create a socket and bind to the specified port
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', port))  # Listen on all available network interfaces
    server_socket.listen()

    print(f"Listening for connections on port {port}...")

    asyncio.get_event_loop().run_until_complete(
        websockets.serve(handle_connection, '0.0.0.0', 8765)  # WebSocket server port
    )

    asyncio.get_event_loop().run_forever()

if __name__ == "__main__":
    # Define the port to listen on (should match the port in your client application)
    listen_port = 8888  # Replace with the actual port you want to use

    start_listener(listen_port)
