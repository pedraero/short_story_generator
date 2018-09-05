from os import walk
import re
import os
from moviepy.editor import VideoFileClip, concatenate_videoclips
import random


def choose_folder():
    cwd = os.getcwd()
    for (root, dirs, files) in walk(cwd):
        print(dirs)
    folder = input("Whats the name the folder your videos are in:\n")
    return folder


def find_movies(folder_name):
    f = []
    cwd = os.getcwd()
    for (root, dirs, files) in walk(f"{cwd}/{folder_name}"):
        for movie in files:
            f.append(movie)
    return f


def create_movie():
    print("Clips must have at least 5 seconds to work")
    max_seconds = int(input("Whats the Max amount of seconds?\n"))
    min_seconds = int(input("Whats the Min amount of seconds?\n"))
    folder_name = choose_folder()
    video_name = input("Whats the name of your movie:\n")
    files = find_movies(folder_name)
    clip_list = []
    time = 0
    for movie in files:
        clip = VideoFileClip(f"{folder_name}/{movie}")
        duration = clip.duration
        duration = int(duration)
        if duration < max_seconds:
            continue
        else:
            endtime = random.randint(max_seconds, duration)
            starttime = endtime - random.randint(min_seconds, max_seconds)
            clip_cut = VideoFileClip(f"{folder_name}/{movie}").subclip(starttime, endtime)
            clip_list.append(clip_cut)
            time = time + (endtime - starttime)
    final_clip = concatenate_videoclips(
        clip_list, method="compose", transition=None)

    final_clip.write_videofile(f"{video_name}.mp4")


create_movie()
