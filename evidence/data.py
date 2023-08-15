import boto3

class S3ImgUploader:
    def __init__(self, file):
        self.file = file

    def upload(self):
        s3_client = boto3.client(
            's3',
            aws_access_key_id     = env('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key = env('AWS_SECRET_ACCESS_KEY')
        )
        url = 'img'+'/'+uuid.uuid1().hex
        
        s3_client.upload_fileobj(
            self.file, 
            "bucket_name", 
            url, 
            ExtraArgs={
                "ContentType": self.file.content_type
            }
        )
        return url