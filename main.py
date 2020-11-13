import youtube_dl as yt
from youtube_dl.YoutubeDL import UnavailableVideoError, MaxDownloadsReached
from youtube_dl.utils import ExtractorError
from .options import ydl_opts


def grab(link):
    # Initialize the Downloader with YDL config options
    downloader = yt.YoutubeDL(ydl_opts)
    try:
        # Where the magic happens
        downloader.download([link])

    except UnavailableVideoError:
        print("Video is unavailable")

    except MaxDownloadsReached:
        print("Maximum number of downloaded files reached.")

    except ExtractorError:
        print("Not a valid link")

    finally:
        print("Finished")