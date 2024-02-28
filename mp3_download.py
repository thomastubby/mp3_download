import os
import sys
import re
from moviepy.editor import *
from pytube import YouTube
from pytube import Playlist

def DIVIDE():
    print("-------------------------------------------------")

def NORM_TITLE(unnorm):
    normed_value = re.sub(r'\W+\s', '', unnorm)
    return str(normed_value)

def GET_PLAYLIST():
    global playlist
    playlist_link=input("Paste the link to the YouTube playlist that you would like to download: ")
    DIVIDE()
    playlist = Playlist(playlist_link)

def SET_LOCATION():
    global download_location
    new_dir = NORM_TITLE(playlist.title)
    download_location = os.environ.get("USERPROFILE") + "\\Music\\" + new_dir

def DOWNLOAD_PLAYLIST():
    for video in playlist.videos:
        global normed_video
        normed_video = NORM_TITLE(video.title)
        if not os.path.isfile(normed_video):
            try:
                print("Downloading: " + normed_video)
                video.streams.first().download(output_path=download_location, filename=normed_video)
                CONVERT(normed_video)
                DIVIDE()
            except:
                print("DOWNLOAD FAILED: " + normed_video)
                DIVIDE()
                pass

def CREATE_FOLDER(dir):
     if not os.path.exists(dir):
          os.makedirs(dir)
          
def CONFIRM_DOWNLOAD():
    print("DOWNLOAD LOCATION: " + download_location + "\n" + "PLAYLIST NAME: " + playlist.title)
    confirmation = input("Would you like to download now? (Y/n)\n")
    CREATE_FOLDER(download_location)
    if confirmation == "y" or confirmation == "Y":
            DIVIDE()
            DOWNLOAD_PLAYLIST()
    else: sys.exit()

def CONVERT(mp4file):
    original_filename = download_location + "\\" + mp4file
    try:
        video_file = AudioFileClip(original_filename)
        video_file.write_audiofile(original_filename + ".mp3")
        video_file.close()
    except:
        print("CONVERT FAILED: " + original_filename)
        pass
    os.remove(original_filename)

##RUNTIME
GET_PLAYLIST()
SET_LOCATION()
CONFIRM_DOWNLOAD()