from classes import logger
from helpers import my_hook
import os

SAVE_PATH = '/'.join(os.getcwd().split('/')[:3]) + '/Downloads'

ydl_opts = {

        'outtmpl': SAVE_PATH + '/%(title)s.%(ext)s',
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
        'logger': logger.MyLogger(),
        'progress_hooks': [my_hook],
        'download_archive': 'archive',
        'verbose': True,
    }