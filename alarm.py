#!/usr/bin/env python

from config import CONFIG

import datetime
from os import popen, path
import random
from time import sleep

# [String]
PLAYABLE_MUSIC_EXTENSIONS = ['.mp3'] # does wma work?

# FilePath -> Bool
def is_playable_music_file(filename):
  return len([i for i in PLAYABLE_MUSIC_EXTENSIONS if filename.endswith(i)])

# () -> Int
day_of_week = datetime.datetime.today().weekday
# () -> Int
hour = lambda: datetime.datetime.today().hour
# () -> Int
minute = lambda: datetime.datetime.today().minute

# FilePath -> [FilePath]
def ls(directory):
  return [file for file in popen('ls "%s"' % directory).read().split('\n') if file]

# FilePath -> [FilePath]
def directory_to_playlist(directory):
  filenames = ls(directory)
  music_files = filter(is_playable_music_file, filenames)
  return [path.join(directory, music_file) for music_file in music_files]

# FilePath -> FilePath]
def select_subdirectory(directory):
  return path.join(directory, random.choice(ls(directory)))

# Int -> [String]
def day_names(day):
  return [
    ['monday', 'weekdays'],
    ['tuesday', 'weekdays'],
    ['wednesday', 'weekdays'],
    ['thursday', 'weekdays'],
    ['friday', 'weekdays'],
    ['saturday', 'weekend'],
    ['sunday', 'weekend']
  ][day]

while True:
  sleep(1)
  artist = select_subdirectory(CONFIG['music_path'])
  album = select_subdirectory(artist)
  playlist = directory_to_playlist(album)
  print album
  print playlist
#  print directory_to_playlist('/home/michael/Audio/Music/Sufjan Stevens/Illinois')
#  for day_name in day_names(day_of_week()):
#    if (day_name, hour(), minute()) in CONFIG['alarms']:
#      print 'alarm hit'
