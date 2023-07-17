import asyncio
import websockets

async def handle_connection(websocket, path):
    # Handle the WebSocket connection
    try:
        while True:
            message = await websocket.recv()
            # Process the received message
            print(f"Received message: {message}")
            # Send a response back to the client
            response = f"Server received message: {message}"
            await websocket.send(response)
    except websockets.exceptions.ConnectionClosedError:
        print("Client disconnected")

# Set up the WebSocket server
start_server = websockets.serve(handle_connection, 'localhost', 8765)

# Start the server event loop
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
