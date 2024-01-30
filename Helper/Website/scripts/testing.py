# Import necessary modules
import time
from flask_socketio import socketio
from selenium import webdriver

def demo():
    driver = webdriver.Chrome()
    driver.get('https://www.google.com')

    try:
        while True:
            # Capture screenshot as base64 encoded image
            screenshot = driver.get_screenshot_as_base64()

            # Emit the screenshot to the client
            socketio.emit('screenshot', {'image': screenshot})

            # Add a delay to control the frequency of screenshots (adjust as needed)
            time.sleep(1)

    except Exception as e:
        print(f"Error in Selenium script: {str(e)}")
    finally:
        driver.quit()
