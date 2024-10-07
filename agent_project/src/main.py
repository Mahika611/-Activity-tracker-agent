# src/main.py
import yaml
from screenshot_handler import ScreenshotHandler
from uploader import Uploader
from activity_monitor import ActivityMonitor
from error_manager import ErrorManager
import time

# Load config
with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

# Initialize components
screenshot_handler = ScreenshotHandler(interval=config['screenshot']['interval'],
                                       blur=config['screenshot']['blur'])
uploader = Uploader(bucket_name=config['aws']['bucket_name'],
                    aws_access_key=config['aws']['access_key'],
                    aws_secret_key=config['aws']['secret_key'])
error_manager = ErrorManager()
activity_monitor = ActivityMonitor()

# Start activity monitoring and screenshot taking
activity_monitor.start_monitoring()

# Main loop
try:
    while True:
        # Take screenshots and upload
        screenshot_file = screenshot_handler.take_screenshot()
        try:
            uploader.upload_file(screenshot_file)
        except Exception as e:
            error_manager.log_failed_upload(screenshot_file)
        
        # Retry any failed uploads
        error_manager.retry_failed_uploads(uploader)
        
        time.sleep(config['screenshot']['interval'])
finally:
    activity_monitor.stop_monitoring()
