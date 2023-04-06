import config as cfg
import pyperclip

import download


def video_audio():
    return int(input('Download video or audio? (1: Video, 2: Audio): '))


def check_yt_link(link):
    if link is not None and "youtube.com" in link:
        return True
    else:
        return False


def check_playlist_link(link):
    if 'playlist' in link:
        # Playlist link
        return True
    else:
        return False


if __name__ == "__main__":
    print('\nYoutube Downloader\n')
    video_link = None
    if cfg.auto_paste is True:
        video_link = pyperclip.paste()
    else:
        video_link = input("Enter the video link: ")
    is_yt = check_yt_link(video_link)
    is_playlist = check_playlist_link(video_link)
    if is_yt is False:
        print('URL not valid')
        quit(1)
    else:
        choice = video_audio()
        if is_playlist is True:
            # Playlist
            d = download.Download(video_link, choice, True)
            d.playlist_download()
        else:
            d = download.Download(video_link, choice, False)
            if choice == 1:
                d.download_video()
            elif choice == 2:
                d.download_audio()
            else:
                print('Option not valid!')
