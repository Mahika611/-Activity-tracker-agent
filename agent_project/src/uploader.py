# src/uploader.py
import boto3
import os

class Uploader:
    def __init__(self, bucket_name, aws_access_key, aws_secret_key):
        self.s3_client = boto3.client('s3', 
                                      aws_access_key_id=aws_access_key, 
                                      aws_secret_access_key=aws_secret_key)
        self.bucket_name = bucket_name

    def upload_file(self, file_path):
        try:
            file_name = os.path.basename(file_path)
            self.s3_client.upload_file(file_path, self.bucket_name, file_name)
            print(f"File {file_name} uploaded to bucket {self.bucket_name}")
        except Exception as e:
            print(f"Failed to upload {file_path}: {str(e)}")
