
from pytube import Playlist
import os
import re


class FileUtility:
    @staticmethod
    def make_valid_filename(s):
        # Replace invalid characters with underscores
        s = re.sub(r'[\\/:*?"<>|,.\']', '', s)
        return s


class VideoDownloader:
    def __init__(self, playlist_url):
        self.playlist = Playlist(playlist_url)
        self.num = 1

    def download_videos(self):
        print('Number of videos in playlist: %s' % len(self.playlist.video_urls))

        for video in self.playlist.videos:
            # Replace the title with a valid filename
            file_name = FileUtility.make_valid_filename(video.title)
            print(self.num, " ", file_name)

            # Check if the file exists in the directory
            if not os.path.exists(f"{file_name}.mp4"):
                try:
                    print("Downloading")
                    video.streams.get_highest_resolution().download()
                except Exception as e:
                    print(e)
            else:
                print("File exists, skipping the Video.")
            self.num += 1

        print("done")


if __name__ == "__main__":
    playlist_url = 'https://www.youtube.com/playlist?list=PLgH5QX0i9K3o8Y-CKhmyodbfHAc9VSVOv'
    video_downloader = VideoDownloader(playlist_url)
    video_downloader.download_videos()
