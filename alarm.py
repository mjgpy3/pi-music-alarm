#!/usr/bin/env python

from config import CONFIG

import datetime
from time import sleep

day_of_week = datetime.datetime.today().weekday
hour = lambda: datetime.datetime.today().hour
minute = lambda: datetime.datetime.today().minute

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
  for day_name in day_names(day_of_week()):
    if (day_name, hour(), minute()) in CONFIG['alarms']:
      print 'alarm hit'
