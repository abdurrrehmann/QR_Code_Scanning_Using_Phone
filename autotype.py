import pyautogui
import time
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allows pc.html to send HTTP requests to this local script

@app.route('/type', methods=['POST'])
def handle_scan():
    data = request.json
    text = data.get('text', '')
    
    if text:
        # Give a 100ms pause to ensure focus before typing
        time.sleep(0.1)
        
        # Simulate typing directly into whatever window/field is focused
        pyautogui.write(text, interval=0.01)
        pyautogui.press('enter') # Automatically press Enter (moves to next Excel row/line)
        
        print(f"Typed: {text}")
        return {"status": "success", "typed": text}, 200
        
    return {"status": "error", "message": "No text provided"}, 400

if __name__ == '__main__':
    print("=" * 50)
    print("🚀 Auto-Type Helper is ACTIVE and LISTENING!")
    print("Focus any input field (Excel, Word, Notepad, etc.)")
    print("Press Ctrl+C in this terminal to stop.")
    print("=" * 50)
    
    # Keeps the script running continuously on port 5000
    app.run(host='127.0.0.1', port=5000)