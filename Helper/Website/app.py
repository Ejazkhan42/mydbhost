from flask import Flask, render_template
from flask_socketio import SocketIO
import base64
import pyautogui

app = Flask(__name__)
socketio = SocketIO(app)

@socketio.on('request_frame')
def handle_request_frame():
    # Capture the entire screen using pyautogui
    screenshot = capture_screen()

    # Encode the image in base64 for sending through WebSocket
    img_data = base64.b64encode(screenshot).decode('utf-8')

    # Emit the image data to the connected clients
    socketio.emit('frame', {'img_data': img_data})

def capture_screen():
    # Capture the entire screen using pyautogui
    screenshot = pyautogui.screenshot()

    # Resize the screenshot to 800x600
    screenshot = screenshot.resize((800, 600))

    # Convert the screenshot to bytes
    img_bytes = screenshot.tobytes()

    return img_bytes

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    socketio.run(app, debug=True)
