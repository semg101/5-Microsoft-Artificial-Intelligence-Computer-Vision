#pip install video_indexer
from video_indexer import VideoIndexer

CONFIG = {
    'SUBSCRIPTION_KEY': '1fe3959552704653a7c0ab804ce83249',
    'LOCATION': 'westus2',
    'ACCOUNT_ID': 'cbd4c0d6-efca-40a4-a34f-6eeeb4a22e9c'
}

vi = VideoIndexer(
    vi_subscription_key=CONFIG['SUBSCRIPTION_KEY'],
    vi_location=CONFIG['LOCATION'],
    vi_account_id=CONFIG['ACCOUNT_ID']
)


#
video_id = vi.upload_to_video_indexer(
   input_filename='video_indexer.mp4',
   video_name='video_indexer-name',  # identifier for video in Video Indexer platform, must be unique during indexing time
   video_language='English'
)

#
info = vi.get_video_info(
    video_id,
    video_language='English'
)