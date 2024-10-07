# src/screenshot_handler.py
import pyautogui
from PIL import Image, ImageFilter
import time

class ScreenshotHandler:
    def __init__(self, interval=300, blur=False):
        self.interval = interval
        self.blur = blur

    def take_screenshot(self):
        screenshot = pyautogui.screenshot()
        if self.blur:
            screenshot = screenshot.filter(ImageFilter.GaussianBlur(radius=15))
        timestamp = int(time.time())
        filename = f"screenshot_{timestamp}.png"
        screenshot.save(filename)
        print(f"Screenshot saved: {filename}")
        return filename
    
    def start_screenshot_cycle(self):
        while True:
            filename = self.take_screenshot()
            time.sleep(self.interval)
