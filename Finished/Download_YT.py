from pytube import YouTube
import os
from shutil import copy2

VIDEO_SAVE_DIRECTORY = "Video"
AUDIO_SAVE_DIRECTORY = "Audio"
CUR_DIR = os.getcwd()

def download(video_url, x):
    video = YouTube(video_url)
    vid = video.streams.get_highest_resolution()
    filename = f'{video.author} - {video.title}.mp4'
    cur_dir = os.path.join(CUR_DIR, VIDEO_SAVE_DIRECTORY, filename)

    try:
        vid.download(VIDEO_SAVE_DIRECTORY, filename=filename)
    except Exception:
        print("Failed to download video")
        return 

    for i in range(x - 1):
        name, ext = os.path.splitext(cur_dir)
        name = name + f' ({i + 2})' + ext
        copy2(cur_dir, name)

    print(f"Video was downloaded successfully: {cur_dir}")

def download_audio(video_url, x):
    video = YouTube(video_url)
    audio = video.streams.filter(only_audio = True).first()
    filename = f'{video.author} - {video.title}.mp3'
    cur_dir = os.path.join(CUR_DIR, AUDIO_SAVE_DIRECTORY, filename)

    try:
        audio.download(AUDIO_SAVE_DIRECTORY, filename=filename)
    except Exception:
        print("Failed to download audio")
        return 
    
    for i in range(x - 1):
        name, ext = os.path.splitext(cur_dir)
        name = name + f' ({i + 2})' + ext
        copy2(cur_dir, name)

    print(f"Audio was downloaded successfully: {cur_dir}")

if __name__ == "__main__":
    lol = 1000
    for _ in range(lol):
        inp = input("Please, write YouTube link (also add '-a' if you want only audio or number of copies): ")
        sinp = inp.split()
        audio = False
        num = 1
        
        for i in sinp:
            match i:
                case "-a":
                    audio = True
                case other:
                    try:
                        num = int(i)
                    except ValueError:
                        link = i
        
        if audio:
            download_audio(link, num)
        else:
            download(link, num)

        print()

# https://youtu.be/4ptq4CE2pxA
# https://www.youtube.com/watch?v=_OLrjAWzUR0
# https://www.youtube.com/watch?v=rUt7qOHwh1s