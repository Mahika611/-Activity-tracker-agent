# src/activity_monitor.py
from pynput import mouse, keyboard
import time

class ActivityMonitor:
    def __init__(self):
        self.last_activity_time = time.time()
        self.keyboard_listener = keyboard.Listener(on_press=self.on_key_press)
        self.mouse_listener = mouse.Listener(on_move=self.on_mouse_move)
        
    def on_key_press(self, key):
        self.last_activity_time = time.time()
        print(f"Key pressed: {key}, Last activity time updated.")
        
    def on_mouse_move(self, x, y):
        self.last_activity_time = time.time()
        print(f"Mouse moved: {x}, {y}, Last activity time updated.")

    def start_monitoring(self):
        self.keyboard_listener.start()
        self.mouse_listener.start()
        
    def stop_monitoring(self):
        self.keyboard_listener.stop()
        self.mouse_listener.stop()

    def get_last_activity_time(self):
        return self.last_activity_time
