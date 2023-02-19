import os
from googleapiclient.discovery import build
import json

api_key: str = os.getenv('YT_API_KEY')
youtube = build('youtube', 'v3', developerKey=api_key)

channel_id = 'UC1eFXmJNkjITxPFWTy6RsWg'
channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
print(json.dumps(channel, indent=2, ensure_ascii=False))


class Channel:
    def __init__(self, id):
        self.id = id

    def print_info(self):
        channel_id = self.id
        channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        return print(json.dumps(channel, indent=2, ensure_ascii=False))


chn1 = Channel("UC2Ru64PHqW4FxoP0xhQRvJg")
chn1.print_info()
