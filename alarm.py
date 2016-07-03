#!/usr/bin/env python

from config import CONFIG

import datetime
from os import popen, path
import pygame
import random
from time import sleep

# FilePath -> Bool
def is_playable_music_file(filename):
  return filename.endswith('.mp3')

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

# () -> Bool
song_is_playing = pygame.mixer.music.get_busy

# () -> Bool
def alarm_time():
  for day_name in day_names(day_of_week()):
    if (day_name, hour(), minute()) in CONFIG['alarms']:
      return True

  return False

# () -> [FilePath]
def random_playlist():
  artist = select_subdirectory(CONFIG['music_path'])
  album = select_subdirectory(artist)
  return directory_to_playlist(album)

# [FilePath] -> [FilePath]
def pop_and_play(playlist):
  song = playlist[0]
  pygame.mixer.music.load(song)
  pygame.mixer.music.play()
  return playlist[1:]

playlist = []
pygame.init()

while True:
  sleep(1)
  if not playlist and alarm_time():
    playlist = random_playlist()
  elif playlist and not song_is_playing():
    print 'playing'
    playlist = pop_and_play(playlist)
