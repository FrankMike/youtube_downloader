# Download Class
import config as cfg
from pytube import YouTube, Playlist
import os
from pathlib import Path


class Download:

    def __init__(self, link, choice, is_playlist):
        self.link = link
        self.destination = str(Path.home() / cfg.destination)
        self.choice = choice
        if is_playlist is True:
            self.p = Playlist(self.link)
        else:
            self.yt = YouTube(self.link)

    def download_video(self):
        print('Video Download')
        res = int(input('Choose resolution (1: 1080p, 2: Highest resolution): '))
        try:
            print('Downloading...')
            if res == 1:
                self.yt.streams.filter(resolution='1080p', file_extension='mp4').first().download(self.destination)
            elif res == 2:
                self.yt.streams.get_highest_resolution().download(self.destination)
            else:
                print('Option not available')
        except ConnectionError:
            print('Connection error!')
        print('Download complete!')

    def download_audio(self):
        # Download Audio
        print('Audio Download\n')
        print('Downloading...')
        try:
            out_file = self.yt.streams.filter(only_audio=True).first().download(self.destination)
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
        except ConnectionError:
            print('Connection Error')
        print('Download complete!')

    def playlist_download(self):
        video_list = []
        for v in self.p.video_urls:
            video_list.append(v)
        download_choice = int(input('Download all playlist? (0: No, 1: Yes) '))
        # One video
        if download_choice == 0:
            video_name = input('Insert the video name: ')
            for v in video_list:
                if self.choice == 1:
                    if video_name in v:
                        self.download_video()
                elif self.choice == 2:
                    if video_name in v:
                        self.download_audio()
        # All videos
        elif download_choice == 1:
            for video in self.p.videos:
                if self.choice == 1:
                    video.streams.first().download(self.destination)
                elif self.choice == 2:
                    out_file = video.streams.filter(only_audio=True).first().download(self.destination)
                    base, ext = os.path.splitext(out_file)
                    new_file = base+'.mp3'
                    os.rename(out_file, new_file)



