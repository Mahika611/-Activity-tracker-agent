# src/error_manager.py
import os
import time

class ErrorManager:
    def __init__(self):
        self.failed_uploads = []

    def log_failed_upload(self, file_path):
        print(f"Logging failed upload: {file_path}")
        self.failed_uploads.append(file_path)

    def retry_failed_uploads(self, uploader):
        while self.failed_uploads:
            file_path = self.failed_uploads.pop(0)
            if os.path.exists(file_path):
                uploader.upload_file(file_path)
            else:
                print(f"File {file_path} no longer exists.")
